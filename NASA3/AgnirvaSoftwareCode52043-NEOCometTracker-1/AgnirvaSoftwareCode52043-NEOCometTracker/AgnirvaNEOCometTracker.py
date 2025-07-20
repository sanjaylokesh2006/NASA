import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sklearn.linear_model import LinearRegression
import numpy as np
from dateutil.relativedelta import relativedelta

# Mapping of display names to API body codes
BODY_CODES = {
    'Mercury': 'Merc',
    'Venus': 'Venus',
    'Earth': 'Earth',
    'Mars': 'Mars',
    'Jupiter': 'Juptr',
    'Saturn': 'Satrn',
    'Uranus': 'Urnus',
    'Neptune': 'Neptn',
    'Moon': 'Moon'
}

# Notification settings (would be stored in a database in production)
if 'notification_settings' not in st.session_state:
    st.session_state.notification_settings = {
        'email': '',
        'notification_threshold': 0.02,  # in AU
        'enabled': False,
        'last_notified': None
    }

# Function to fetch close approach data
def fetch_close_approaches(body_code='Earth', date_min='now', date_max='+60', dist_max='0.05', 
                          dist_unit='AU', limit=100, object_type='NEO'):
    url = 'https://ssd-api.jpl.nasa.gov/cad.api'
    params = {
        'body': body_code,
        'date-min': date_min,
        'date-max': date_max,
        'dist-max': f"{dist_max}{dist_unit}",
        'limit': limit
    }
    
    if object_type == 'NEO':
        params['neo'] = 'true'
    elif object_type == 'Comet':
        params['comet'] = 'true'
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        st.error(f"⚠️ HTTP error occurred: {http_err}")
        try:
            error_info = response.json()
            st.error(f"🔍 Error details: {error_info}")
        except ValueError:
            st.error("🔍 No additional error information provided.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Error fetching data from API: {e}")
        return None

# Function to parse the data
def parse_data(data):
    if data is None or data.get('count', 0) == 0:
        st.warning("⚠️ No close approaches found for the given parameters.")
        return pd.DataFrame()
    
    fields = data.get('fields', [])
    records = data.get('data', [])
    fd = pd.DataFrame(records, columns=fields)
    
    # Convert relevant columns to appropriate data types
    fd['cd'] = pd.to_datetime(fd['cd'], format='%Y-%b-%d %H:%M')
    fd['dist'] = pd.to_numeric(fd['dist'], errors='coerce')
    fd['v_rel'] = pd.to_numeric(fd['v_rel'], errors='coerce')
    fd['v_inf'] = pd.to_numeric(fd['v_inf'], errors='coerce')
    
    return fd

# Function to visualize the data using Plotly with optional trendline and prediction
def visualize_close_approaches(fd, body, add_trendline=False, show_prediction=False):
    if fd.empty:
        return
    
    # Prepare data for visualization
    plot_data = fd.copy()
    plot_data['date_ordinal'] = plot_data['cd'].apply(lambda x: x.toordinal())
    
    fig = px.scatter(
        plot_data,
        x='cd',
        y='dist',
        hover_data=['des', 'v_rel', 'v_inf'],
        labels={
            'cd': '📅 Date',
            'dist': f'📏 Distance ({st.session_state.get("dist_unit", "AU")})',
            'des': '🪐 Designation',
            'v_rel': '⚡ Relative Velocity (km/s)',
            'v_inf': '∞ Infinity Velocity (km/s)'
        },
        title=f'🔭 Close Approaches to {body}'
    )
    
    # Add trendline if requested
    if add_trendline:
        try:
            fig.update_traces(
                line_shape='linear',
                selector=dict(mode='lines'),
                line=dict(dash='dot', width=2)
            )
        except Exception as e:
            st.warning(f"⚠️ Could not add trendline: {e}")
    
    # Add prediction if requested
    if show_prediction and len(plot_data) >= 5:  # Need at least 5 points for prediction
        try:
            # Prepare data for linear regression
            X = plot_data['date_ordinal'].values.reshape(-1, 1)
            y = plot_data['dist'].values
            
            # Train model
            model = LinearRegression()
            model.fit(X, y)
            
            # Generate future dates (6 months ahead)
            last_date = plot_data['cd'].max()
            future_dates = [last_date + timedelta(days=30*i) for i in range(1, 7)]
            future_ordinals = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
            
            # Predict distances
            predicted_distances = model.predict(future_ordinals)
            
            # Add prediction to plot
            fig.add_scatter(
                x=future_dates,
                y=predicted_distances,
                mode='lines+markers',
                name='Predicted Approaches',
                line=dict(color='red', dash='dot'),
                marker=dict(color='red', symbol='diamond')
            )
            
            # Add confidence interval (simplified)
            y_err = (plot_data['dist'].std() / 2)  # Simplified error estimation
            fig.add_scatter(
                x=future_dates + future_dates[::-1],  # x coordinates for the polygon
                y=np.concatenate([predicted_distances + y_err, 
                                 (predicted_distances - y_err)[::-1]]),
                fill='toself',
                fillcolor='rgba(255,0,0,0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                hoverinfo='skip',
                name='Confidence Interval'
            )
            
        except Exception as e:
            st.warning(f"⚠️ Could not generate prediction: {e}")
    
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

# Function to send email notifications
def send_notification_email(recipient, subject, body):
    try:
        # Configure your email server settings here
        smtp_server = "smtp.example.com"
        smtp_port = 587
        sender_email = "notifications@agnirva.com"
        sender_password = "your_email_password"  # In production, use environment variables
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        st.error(f"⚠️ Failed to send notification: {e}")
        return False

# Function to check for close approaches that meet notification criteria
def check_for_notifications(fd, body_display):
    settings = st.session_state.notification_settings
    
    if not settings['enabled'] or not settings['email']:
        return
    
    # Get current time and filter for future events
    now = datetime.now()
    future_approaches = fd[fd['cd'] > now]
    
    if future_approaches.empty:
        return
    
    # Find approaches closer than threshold
    threshold = settings['notification_threshold']
    close_approaches = future_approaches[future_approaches['dist'] <= threshold]
    
    if close_approaches.empty:
        return
    
    # Check if we've already notified about these (simple deduplication)
    last_notified = settings.get('last_notified')
    if last_notified:
        close_approaches = close_approaches[close_approaches['cd'] > last_notified]
    
    if close_approaches.empty:
        return
    
    # Prepare notification
    subject = f"⚠️ Close Approach Alert: {len(close_approaches)} events near {body_display}"
    
    body = f"""Close Approach Alert for {body_display}:

The following celestial objects will make close approaches within {threshold} AU:

"""
    for _, row in close_approaches.iterrows():
        body += f"""
- {row['des']} on {row['cd'].strftime('%Y-%m-%d %H:%M')}
  Distance: {row['dist']} AU
  Velocity: {row['v_rel']} km/s
"""
    
    body += "\n\nThis is an automated notification from Agnirva NEO/Comet Tracker."
    
    # Send notification
    if send_notification_email(settings['email'], subject, body):
        st.session_state.notification_settings['last_notified'] = datetime.now()
        st.success(f"📧 Notification sent to {settings['email']}")
    else:
        st.error("Failed to send notification")

# Streamlit App
def main():
    st.set_page_config(page_title="🌌 Agnirva NEO/Comet Tracker", layout="wide")
    st.title("🌠 Agnirva NEO and Comet Tracker")
    st.markdown("""
    Welcome to the **NEO and Comet Tracker**! 🚀  
    Track close approaches of asteroids and comets with notifications and predictive analytics.
    """)
    
    # Sidebar for inputs
    st.sidebar.header("Input Parameters")
    
    # Celestial Body Selection
    body_display_options = list(BODY_CODES.keys())
    body_display = st.sidebar.selectbox(
        "🪐 Select Celestial Body",
        body_display_options,
        index=2,
        help="Choose the celestial body you want to analyze close approaches to."
    )
    body_code = BODY_CODES[body_display]
    
    # Date Range Selection
    st.sidebar.subheader("Date Range")
    today = datetime.today()
    default_end_date = today + timedelta(days=60)
    
    date_min = st.sidebar.date_input(
        "🔹 Start Date",
        value=today,
        min_value=datetime(1900, 1, 1),
        max_value=datetime(2100, 12, 31),
        help="Select the start date for the close approaches data."
    )
    
    date_max_option = st.sidebar.selectbox(
        "🔸 End Date Option",
        options=['Days from Start Date', 'Specific Date'],
        index=0,
        help="Choose how to specify the end date for the data range."
    )
    
    if date_max_option == 'Days from Start Date':
        days_from_start = st.sidebar.number_input(
            "📅 Number of Days from Start Date",
            min_value=1,
            max_value=36525,
            value=60,
            step=1,
            help="Specify the number of days from the start date to set the end date."
        )
        date_max = (datetime.combine(date_min, datetime.min.time()) + timedelta(days=days_from_start)).strftime('%Y-%m-%d')
    elif date_max_option == 'Specific Date':
        date_max_date = st.sidebar.date_input(
            "📅 End Date",
            value=default_end_date,
            min_value=date_min,
            max_value=datetime(2100, 12, 31),
            help="Select a specific end date for the close approaches data."
        )
        date_max = date_max_date.strftime('%Y-%m-%d')
    
    # Distance Unit Selection
    st.sidebar.subheader("Distance Parameters")
    dist_unit = st.sidebar.selectbox(
        "📐 Distance Unit",
        options=['AU', 'LD'],
        index=0,
        help="Choose the unit for maximum distance: Astronomical Units (AU) or Lunar Distances (LD)."
    )
    default_dist_max = '0.05' if dist_unit == 'AU' else '10'
    dist_max = st.sidebar.text_input(
        "🔝 Maximum Distance",
        value=default_dist_max,
        help=f"Set the maximum distance for close approaches in {dist_unit}."
    )
    
    # Object Type Filter
    st.sidebar.subheader("Object Type & Results")
    object_type = st.sidebar.selectbox(
        "☄️ Object Type",
        options=['NEO', 'Comet', 'Both'],
        index=0,
        help="Filter results by object type: Near-Earth Objects (NEO), Comets, or Both."
    )
    
    # Number of Results
    limit = st.sidebar.number_input(
        "📈 Number of Results to Fetch",
        min_value=1,
        max_value=1000,
        value=100,
        step=1,
        help="Specify how many close approach records to retrieve."
    )
    
    # Notification Settings
    st.sidebar.subheader("🔔 Notification Settings")
    st.session_state.notification_settings['email'] = st.sidebar.text_input(
        "📧 Notification Email",
        value=st.session_state.notification_settings['email'],
        help="Enter your email to receive alerts for close approaches."
    )
    
    st.session_state.notification_settings['notification_threshold'] = st.sidebar.number_input(
        "⚠️ Notify for Approaches Closer Than (AU)",
        min_value=0.0001,
        max_value=1.0,
        value=st.session_state.notification_settings['notification_threshold'],
        step=0.001,
        format="%.4f",
        help="Set the distance threshold for receiving notifications."
    )
    
    st.session_state.notification_settings['enabled'] = st.sidebar.checkbox(
        "Enable Notifications",
        value=st.session_state.notification_settings['enabled'],
        help="Enable or disable email notifications."
    )
    
    # Submit Button
    fetch_data = st.sidebar.button("🚀 Fetch and Visualize Data")
    
    if fetch_data:
        with st.spinner("⏳ Fetching data..."):
            if object_type in ['NEO', 'Comet']:
                data = fetch_close_approaches(
                    body_code=body_code,
                    date_min=date_min.strftime('%Y-%m-%d'),
                    date_max=date_max,
                    dist_max=dist_max,
                    dist_unit=dist_unit,
                    limit=limit,
                    object_type=object_type
                )
                fd = parse_data(data)
            elif object_type == 'Both':
                data_neo = fetch_close_approaches(
                    body_code=body_code,
                    date_min=date_min.strftime('%Y-%m-%d'),
                    date_max=date_max,
                    dist_max=dist_max,
                    dist_unit=dist_unit,
                    limit=limit,
                    object_type='NEO'
                )
                data_comet = fetch_close_approaches(
                    body_code=body_code,
                    date_min=date_min.strftime('%Y-%m-%d'),
                    date_max=date_max,
                    dist_max=dist_max,
                    dist_unit=dist_unit,
                    limit=limit,
                    object_type='Comet'
                )
                
                fd_neo = parse_data(data_neo)
                fd_comet = parse_data(data_comet)
                
                fd = pd.concat([fd_neo, fd_comet], ignore_index=True)
                fd.drop_duplicates(inplace=True)
        
        if not fd.empty:
            st.success(f"✅ Found {len(fd)} close approaches to **{body_display}**.")
            
            # Store DataFrame in Session State
            st.session_state['fd'] = fd
            st.session_state['body_display'] = body_display
            st.session_state['dist_unit'] = dist_unit
            
            # Check for notifications
            check_for_notifications(fd, body_display)
        else:
            st.session_state['fd'] = pd.DataFrame()
            st.session_state['body_display'] = body_display
            st.session_state['dist_unit'] = dist_unit
    
    # Check if data is available in session state
    if 'fd' in st.session_state and not st.session_state['fd'].empty:
        fd = st.session_state['fd']
        body_display = st.session_state['body_display']
        dist_unit = st.session_state['dist_unit']
        
        # Display the data table
        st.subheader("📊 Close Approach Data")
        st.dataframe(fd[['des', 'cd', 'dist', 'v_rel', 'v_inf']].rename(columns={
            'des': '🪐 Designation',
            'cd': '📅 Date',
            'dist': f'📏 Distance ({dist_unit})',
            'v_rel': '⚡ Relative Velocity (km/s)',
            'v_inf': '∞ Infinity Velocity (km/s)'
        }))
        
        # Download button for CSV
        csv = fd.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv,
            file_name='close_approaches_data.csv',
            mime='text/csv',
        )
        
        # Visualization options
        st.markdown("---")
        st.subheader("📈 Visualization")
        
        col1, col2 = st.columns(2)
        with col1:
            add_trendline = st.checkbox("✨ Add Trendline (Requires statsmodels)")
        with col2:
            show_prediction = st.checkbox("🔮 Show Predictive Analytics")
        
        # Visualization
        visualize_close_approaches(fd, body_display, add_trendline=add_trendline, show_prediction=show_prediction)
        
        # Explanation of predictive analytics
        if show_prediction:
            st.markdown("""
            **About Predictive Analytics:**
            - The red dotted line shows predicted close approaches based on linear regression of historical data
            - The shaded area represents a simplified confidence interval (not a true statistical confidence interval)
            - Predictions are based only on the currently loaded data and should not be considered authoritative
            - For accurate predictions, NASA's specialized orbit calculation tools should be used
            """)
    
    else:
        if fetch_data:
            st.info("ℹ️ No data available to display. Please adjust your search parameters.")
        else:
            st.info("🔍 Awaiting your search parameters. Use the sidebar to get started!")
    
    st.markdown("""
    ---
    **🛰️ Data Source:** JPL's SSD/CNEOS CAD API  
    **🛠️ Created by:** Agnirva
    """)

if __name__ == '__main__':
    main()