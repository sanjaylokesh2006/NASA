import streamlit as st  # Import the Streamlit library for building web apps (Commented by Agnirva.com)
import requests  # Import the requests library for making HTTP requests (Commented by Agnirva.com)
import pandas as pd  # Import pandas for data manipulation and analysis (Commented by Agnirva.com)
from datetime import datetime, timedelta  # Import datetime and timedelta for handling dates and times (Commented by Agnirva.com)
import plotly.express as px  # Import Plotly Express for data visualization (Commented by Agnirva.com)

# Define event descriptions for glossary and explanations (Commented by Agnirva.com)
Agnirvaevent_descriptions = {  # Initialize a dictionary to store event descriptions (Commented by Agnirva.com)
    "CME": "Coronal Mass Ejection (CME): A massive burst of solar wind and magnetic fields rising above the solar corona.",  # Description for CME (Commented by Agnirva.com)
    "GST": "Geomagnetic Storm (GST): Disturbances in Earth's magnetosphere caused by solar wind shocks.",  # Description for GST (Commented by Agnirva.com)
    "FLR": "Solar Flare (FLR): A sudden flash of increased brightness on the Sun, usually observed near its surface.",  # Description for FLR (Commented by Agnirva.com)
    "SEP": "Solar Energetic Particle (SEP): High-energy particles emitted by the Sun, often associated with solar flares and CMEs.",  # Description for SEP (Commented by Agnirva.com)
    "IPS": "Interplanetary Shock (IPS): Shock waves traveling through space, often caused by CMEs or solar wind variations.",  # Description for IPS (Commented by Agnirva.com)
    "RBE": "Radiation Belt Enhancement (RBE): An increase in the density of charged particles in Earth's radiation belts.",  # Description for RBE (Commented by Agnirva.com)
    "MPC": "Magnetopause Crossing (MPC): When solar wind plasma crosses Earth's magnetopause, the boundary of the magnetosphere.",  # Description for MPC (Commented by Agnirva.com)
    "HSS": "High Speed Stream (HSS): Streams of fast-moving solar wind emanating from coronal holes on the Sun.",  # Description for HSS (Commented by Agnirva.com)
    "notifications": "Notifications: General alerts and updates related to various space weather events."  # Description for notifications (Commented by Agnirva.com)
}

# Define the CSS for space-themed design (Commented by Agnirva.com)
Agnirvaspace_theme_css = """
<style>
/* Background and text colors */  /* Commented by Agnirva.com */
body {  # Styling the body of the app (Commented by Agnirva.com)
    background-color: #0e1117;  # Set background color (Commented by Agnirva.com)
    color: #FAFAFA;  # Set text color (Commented by Agnirva.com)
    font-family: 'Arial', sans-serif;  # Set font family (Commented by Agnirva.com)
}
.sidebar .sidebar-content {  # Styling the sidebar content (Commented by Agnirva.com)
    background-color: #262730;  # Set sidebar background color (Commented by Agnirva.com)
    color: #FAFAFA;  # Set sidebar text color (Commented by Agnirva.com)
}
/* Remove the default Streamlit header */  /* Commented by Agnirva.com */
.css-1d391kg {  # Targeting specific CSS class (Commented by Agnirva.com)
    background-color: #0e1117;  # Set background color for header (Commented by Agnirva.com)
}
.css-1v3fvcr {  # Targeting another CSS class (Commented by Agnirva.com)
    color: #FAFAFA;  # Set text color (Commented by Agnirva.com)
}
.css-1adrfps.edgvbvh3 {  # Targeting nested CSS classes (Commented by Agnirva.com)
    background-color: #262730;  # Set background color (Commented by Agnirva.com)
}
/* Style for expander headers */  /* Commented by Agnirva.com */
.streamlit-expanderHeader {  # Styling expander headers (Commented by Agnirva.com)
    color: #1f77b4;  # Set color for expander headers (Commented by Agnirva.com)
}
</style>
"""  # End of CSS styles (Commented by Agnirva.com)

st.markdown(Agnirvaspace_theme_css, unsafe_allow_html=True)  # Apply the CSS styles to the Streamlit app (Commented by Agnirva.com)

# Title and description (Commented by Agnirva.com)
st.title("🌌 Agnirva Space Weather Visualizer")  # Set the main title of the app (Commented by Agnirva.com)
st.markdown("""
This application visualizes space weather trends using NASA's DONKI API. 
Explore events like Coronal Mass Ejections (CME), Geomagnetic Storms (GST), Solar Flares (FLR), and more.
""")  # End of markdown description (Commented by Agnirva.com)

# Sidebar for user inputs (Commented by Agnirva.com)
st.sidebar.header("Configuration")  # Add a header to the sidebar (Commented by Agnirva.com)

# 1. NASA API Key input at the top (Commented by Agnirva.com)
Agnirvaapi_key = st.sidebar.text_input("Enter your NASA API Key:", value="DEMO_KEY")  # Input field for NASA API Key (Commented by Agnirva.com)

# 2. Event type selection (Commented by Agnirva.com)
Agnirvaevent_types = {  # Dictionary mapping event display names to their codes (Commented by Agnirva.com)
    "CME (Coronal Mass Ejection)": "CME",  # Mapping for CME (Commented by Agnirva.com)
    "GST (Geomagnetic Storm)": "GST",  # Mapping for GST (Commented by Agnirva.com)
    "FLR (Solar Flare)": "FLR",  # Mapping for FLR (Commented by Agnirva.com)
    "SEP (Solar Energetic Particle)": "SEP",  # Mapping for SEP (Commented by Agnirva.com)
    "IPS (Interplanetary Shock)": "IPS",  # Mapping for IPS (Commented by Agnirva.com)
    "RBE (Radiation Belt Enhancement)": "RBE",  # Mapping for RBE (Commented by Agnirva.com)
    "MPC (Magnetopause Crossing)": "MPC",  # Mapping for MPC (Commented by Agnirva.com)
    "HSS (High Speed Stream)": "HSS",  # Mapping for HSS (Commented by Agnirva.com)
    "Notifications": "notifications"  # Mapping for Notifications (Commented by Agnirva.com)
}

Agnirvaselected_event_display = st.sidebar.selectbox(  # Dropdown for selecting event type (Commented by Agnirva.com)
    "Select Space Weather Event Type:",  # Label for the dropdown (Commented by Agnirva.com)
    list(Agnirvaevent_types.keys()),  # List of event display names (Commented by Agnirva.com)
    format_func=lambda x: x  # Formatting function for display (Commented by Agnirva.com)
)

Agnirvaapi_endpoint = Agnirvaevent_types[Agnirvaselected_event_display]  # Get the selected event code (Commented by Agnirva.com)

# 3. Date range selection (Commented by Agnirva.com)
st.sidebar.markdown("### Date Range")  # Add a markdown header for date range (Commented by Agnirva.com)
Agnirvadefault_end_date = datetime.utcnow().date()  # Set default end date to today (Commented by Agnirva.com)
Agnirvadefault_start_date = Agnirvadefault_end_date - timedelta(days=30)  # Set default start date to 30 days ago (Commented by Agnirva.com)

Agnirvastart_date = st.sidebar.date_input("Start Date:", Agnirvadefault_start_date)  # Input for start date (Commented by Agnirva.com)
Agnirvaend_date = st.sidebar.date_input("End Date:", Agnirvadefault_end_date)  # Input for end date (Commented by Agnirva.com)

# Validate date range (Commented by Agnirva.com)
if Agnirvastart_date > Agnirvaend_date:  # Check if start date is after end date (Commented by Agnirva.com)
    st.sidebar.error("Error: End date must fall after start date.")  # Show error message if dates are invalid (Commented by Agnirva.com)

# 4. Fetch data button (Commented by Agnirva.com)
Agnirvafetch_button = st.sidebar.button("Fetch Data")  # Button to fetch data from API (Commented by Agnirva.com)

# 5. Event Information expandable section (Commented by Agnirva.com)
st.sidebar.markdown("### Event Information")  # Add a markdown header for event information (Commented by Agnirva.com)
with st.sidebar.expander("ℹ️ What is this event?"):  # Expander for event information (Commented by Agnirva.com)
    st.write(Agnirvaevent_descriptions.get(Agnirvaapi_endpoint, "No description available."))  # Display selected event description (Commented by Agnirva.com)

# 6. Glossary section (Commented by Agnirva.com)
st.sidebar.markdown("### Glossary")  # Add a markdown header for glossary (Commented by Agnirva.com)
with st.sidebar.expander("📖 View Glossary"):  # Expander for glossary terms (Commented by Agnirva.com)
    for term, description in Agnirvaevent_descriptions.items():  # Iterate over glossary terms (Commented by Agnirva.com)
        st.markdown(f"**{term}**: {description}")  # Display each term and its description (Commented by Agnirva.com)

# 7. Help section (Commented by Agnirva.com)
st.sidebar.markdown("### Help")  # Add a markdown header for help section (Commented by Agnirva.com)
with st.sidebar.expander("❓ How to Use This App"):  # Expander for help instructions (Commented by Agnirva.com)
    st.write("""
    1. **Enter API Key**: Provide your NASA API Key.
    2. **Select Event Type**: Choose the space weather event you're interested in.
    3. **Set Date Range**: Specify the start and end dates for the data visualization.
    4. **Fetch Data**: Click the "Fetch Data" button to retrieve and visualize the data.
    5. **View Details**: Expand the raw JSON data or raw data sections to inspect the data.
    6. **Explore**: Interact with the plots to learn more about specific events.
    """)  # End of help instructions (Commented by Agnirva.com)

# Function to fetch data from DONKI API (Commented by Agnirva.com)
@st.cache_data(ttl=3600)  # Cache the function to avoid redundant API calls (Commented by Agnirva.com)
def Agnirvafetch_space_weather(Agnirvaevent, Agnirvastart, Agnirvaend, Agnirvakey):  # Define function to fetch space weather data (Commented by Agnirva.com)
    Agnirvabase_url = f"https://api.nasa.gov/DONKI/{Agnirvaevent}"  # Construct the base URL for the API endpoint (Commented by Agnirva.com)
    Agnirvaparms = {  # Initialize parameters for the API request (Commented by Agnirva.com)
        "startDate": Agnirvastart.strftime("%Y-%m-%d"),  # Format start date (Commented by Agnirva.com)
        "endDate": Agnirvaend.strftime("%Y-%m-%d"),  # Format end date (Commented by Agnirva.com)
        "api_key": Agnirvakey  # Include the API key (Commented by Agnirva.com)
    }
    
    # Additional parameters for specific events (Commented by Agnirva.com)
    if Agnirvaevent == "CME":  # Check if the event is CME (Commented by Agnirva.com)
        Agnirvaparms.update({  # Update parameters with CME-specific options (Commented by Agnirva.com)
            "mostAccurateOnly": "true",  # Include only the most accurate data (Commented by Agnirva.com)
            "completeEntryOnly": "true",  # Include only complete entries (Commented by Agnirva.com)
            "speed": 500,  # Set speed parameter (Commented by Agnirva.com)
            "halfAngle": 30,  # Set half-angle parameter (Commented by Agnirva.com)
            "catalog": "ALL"  # Include all catalogs (Commented by Agnirva.com)
        })
    elif Agnirvaevent == "notifications":  # Check if the event is notifications (Commented by Agnirva.com)
        Agnirvaparms.update({  # Update parameters for notifications (Commented by Agnirva.com)
            "type": "all"  # Include all types of notifications (Commented by Agnirva.com)
        })
    
    Agnirvaresponse = requests.get(Agnirvabase_url, params=Agnirvaparms)  # Make the API request (Commented by Agnirva.com)
    
    if Agnirvaresponse.status_code == 200:  # Check if the request was successful (Commented by Agnirva.com)
        return Agnirvaresponse.json()  # Return the JSON response (Commented by Agnirva.com)
    else:  # If the request failed (Commented by Agnirva.com)
        st.error(f"Error fetching data: {Agnirvaresponse.status_code} - {Agnirvaresponse.text}")  # Display error message (Commented by Agnirva.com)
        return None  # Return None if there's an error (Commented by Agnirva.com)

# Proceed if Fetch Data button is clicked (Commented by Agnirva.com)
if Agnirvafetch_button:  # Check if the fetch data button was clicked (Commented by Agnirva.com)
    if not Agnirvaapi_key:  # Check if the API key is provided (Commented by Agnirva.com)
        st.error("Please enter your NASA API Key to proceed.")  # Prompt user to enter API key (Commented by Agnirva.com)
    else:  # If API key is provided (Commented by Agnirva.com)
        with st.spinner("Fetching data..."):  # Show a spinner while fetching data (Commented by Agnirva.com)
            Agnirvadata = Agnirvafetch_space_weather(Agnirvaapi_endpoint, Agnirvastart_date, Agnirvaend_date, Agnirvaapi_key)  # Fetch the data (Commented by Agnirva.com)
        
        if Agnirvadata:  # If data was fetched successfully (Commented by Agnirva.com)
            st.success("Data fetched successfully!")  # Display success message (Commented by Agnirva.com)
            
            # Show raw JSON data for debugging (Commented by Agnirva.com)
            with st.expander("Show Raw JSON Data for Debugging"):  # Expander to show raw JSON data (Commented by Agnirva.com)
                st.json(Agnirvadata)  # Display the raw JSON data (Commented by Agnirva.com)
            
            # Process data based on event type (Commented by Agnirva.com)
            if isinstance(Agnirvadata, list):  # Check if the data is a list (Commented by Agnirva.com)
                Agnirvadf = pd.json_normalize(Agnirvadata)  # Normalize JSON data into a DataFrame (Commented by Agnirva.com)
                
                # Define date field mapping (Commented by Agnirva.com)
                Agnirvadate_field_mapping = {  # Mapping of event types to their date fields (Commented by Agnirva.com)
                    "CME": "startTime",  # Date field for CME (Commented by Agnirva.com)
                    "GST": "startTime",  # Date field for GST (Commented by Agnirva.com)
                    "FLR": "beginTime",  # Date field for FLR (Commented by Agnirva.com)
                    "SEP": "eventTime",  # Date field for SEP (Commented by Agnirva.com)
                    "IPS": "eventTime",  # Date field for IPS (Commented by Agnirva.com)
                    "RBE": "eventTime",  # Date field for RBE (Commented by Agnirva.com)
                    "MPC": "eventTime",  # Date field for MPC (Commented by Agnirva.com)
                    "HSS": "eventTime",  # Date field for HSS (Commented by Agnirva.com)
                    "notifications": "messageIssueTime"  # Date field for notifications (Commented by Agnirva.com)
                }
                
                # Define y_label mapping (Commented by Agnirva.com)
                Agnirvay_label_mapping = {  # Mapping of event types to their y-axis labels (Commented by Agnirva.com)
                    "CME": "Number of CMEs",  # Y-label for CME (Commented by Agnirva.com)
                    "GST": "Average Kp Index",  # Y-label for GST (Commented by Agnirva.com)
                    "FLR": "Number of Solar Flares",  # Y-label for FLR (Commented by Agnirva.com)
                    "SEP": "Number of Solar Energetic Particles",  # Y-label for SEP (Commented by Agnirva.com)
                    "IPS": "Number of Interplanetary Shocks",  # Y-label for IPS (Commented by Agnirva.com)
                    "RBE": "Number of Radiation Belt Enhancements",  # Y-label for RBE (Commented by Agnirva.com)
                    "MPC": "Number of Magnetopause Crossings",  # Y-label for MPC (Commented by Agnirva.com)
                    "HSS": "Number of High Speed Streams",  # Y-label for HSS (Commented by Agnirva.com)
                    "notifications": "Number of Notifications"  # Y-label for notifications (Commented by Agnirva.com)
                }
                
                # Define y_label (Commented by Agnirva.com)
                Agnirvay_label = Agnirvay_label_mapping.get(Agnirvaapi_endpoint, "Count")  # Get the y-axis label based on event type (Commented by Agnirva.com)
                
                # Get the correct date field (Commented by Agnirva.com)
                Agnirvadate_field = Agnirvadate_field_mapping.get(Agnirvaapi_endpoint, None)  # Get the date field for the selected event (Commented by Agnirva.com)
                
                if Agnirvadate_field and Agnirvadate_field in Agnirvadf.columns:  # Check if the date field exists in the DataFrame (Commented by Agnirva.com)
                    Agnirvadf['date'] = pd.to_datetime(Agnirvadf[Agnirvadate_field], errors='coerce').dt.date  # Convert the date field to datetime and extract the date (Commented by Agnirva.com)
                else:  # If the specific date field is not found (Commented by Agnirva.com)
                    # Attempt to find a date field dynamically (Commented by Agnirva.com)
                    Agnirvapossible_keys = [col for col in Agnirvadf.columns if 'date' in col.lower() or 'time' in col.lower()]  # Search for columns containing 'date' or 'time' (Commented by Agnirva.com)
                    if Agnirvapossible_keys:  # If any possible date fields are found (Commented by Agnirva.com)
                        Agnirvadate_field = Agnirvapossible_keys[0]  # Use the first possible date field (Commented by Agnirva.com)
                        st.warning(f"Using '{Agnirvadate_field}' as the date field.")  # Warn the user about the chosen date field (Commented by Agnirva.com)
                        Agnirvadf['date'] = pd.to_datetime(Agnirvadf[Agnirvadate_field], errors='coerce').dt.date  # Convert to datetime and extract the date (Commented by Agnirva.com)
                    else:  # If no date fields are found (Commented by Agnirva.com)
                        st.error("No suitable date field found in the data.")  # Show error message (Commented by Agnirva.com)
                        Agnirvadf['date'] = pd.NaT  # Assign Not-a-Time if no date field is found (Commented by Agnirva.com)
                
                # Handle different event types (Commented by Agnirva.com)
                if Agnirvaapi_endpoint == "CME":  # If the event is CME (Commented by Agnirva.com)
                    # For CME, plot the number of CMEs per day (Commented by Agnirva.com)
                    Agnirvadf_grouped = Agnirvadf.groupby('date').size().reset_index(name='count')  # Group data by date and count CMEs (Commented by Agnirva.com)
                    
                    # Plotting with Plotly for interactivity (Commented by Agnirva.com)
                    st.markdown("### Selected Event Information")  # Add a markdown header (Commented by Agnirva.com)
                    st.write(Agnirvaevent_descriptions.get(Agnirvaapi_endpoint, "No description available."))  # Display event description (Commented by Agnirva.com)
                    
                    st.subheader(f"{Agnirvaselected_event_display} from {Agnirvastart_date} to {Agnirvaend_date}")  # Add a subheader with event and date range (Commented by Agnirva.com)
                    Agnirvafig = px.line(Agnirvadf_grouped, x='date', y='count', title=f"Trend of {Agnirvaselected_event_display} Over Time",  # Create a line plot for CME trend (Commented by Agnirva.com)
                                        labels={"date": "Date", "count": Agnirvay_label},  # Set axis labels (Commented by Agnirva.com)
                                        markers=True, template="plotly_dark")  # Add markers and set theme (Commented by Agnirva.com)
                    st.plotly_chart(Agnirvafig, use_container_width=True)  # Display the plotly chart (Commented by Agnirva.com)
                
                elif Agnirvaapi_endpoint == "GST":  # If the event is GST (Commented by Agnirva.com)
                    # For GST, plot the average Kp Index per day (Commented by Agnirva.com)
                    if 'allKpIndex' in Agnirvadf.columns:  # Check if 'allKpIndex' column exists (Commented by Agnirva.com)
                        Agnirvakp_df = Agnirvadf.explode('allKpIndex')  # Explode the 'allKpIndex' list into separate rows (Commented by Agnirva.com)
                        Agnirvakp_df = pd.json_normalize(Agnirvakp_df['allKpIndex'])  # Normalize the exploded JSON data (Commented by Agnirva.com)
                        Agnirvakp_df['date'] = pd.to_datetime(Agnirvakp_df['observedTime'], errors='coerce').dt.date  # Convert 'observedTime' to date (Commented by Agnirva.com)
                        Agnirvadf_grouped = Agnirvakp_df.groupby('date').agg({'kpIndex': 'mean'}).reset_index()  # Calculate average Kp Index per day (Commented by Agnirva.com)
                        
                        # Plotting with Plotly for interactivity (Commented by Agnirva.com)
                        st.markdown("### Selected Event Information")  # Add a markdown header (Commented by Agnirva.com)
                        st.write(Agnirvaevent_descriptions.get(Agnirvaapi_endpoint, "No description available."))  # Display event description (Commented by Agnirva.com)
                        
                        # Removed image display (Commented by Agnirva.com)
                        # if Agnirvaapi_endpoint in Agnirvaevent_images:
                        #     st.image(Agnirvaevent_images[Agnirvaapi_endpoint], use_container_width=True)
                        
                        st.subheader(f"{Agnirvaselected_event_display} Kp Index from {Agnirvastart_date} to {Agnirvaend_date}")  # Add a subheader with event and date range (Commented by Agnirva.com)
                        Agnirvafig = px.line(Agnirvadf_grouped, x='date', y='kpIndex', title=f"Average Kp Index of {Agnirvaselected_event_display} Over Time",  # Create a line plot for average Kp Index (Commented by Agnirva.com)
                                          labels={"date": "Date", "kpIndex": Agnirvay_label},  # Set axis labels (Commented by Agnirva.com)
                                          markers=True, template="plotly_dark")  # Add markers and set theme (Commented by Agnirva.com)
                        st.plotly_chart(Agnirvafig, use_container_width=True)  # Display the plotly chart (Commented by Agnirva.com)
                    else:  # If 'allKpIndex' data is not available (Commented by Agnirva.com)
                        st.error("No 'allKpIndex' data available to plot.")  # Show error message (Commented by Agnirva.com)
                
                elif Agnirvaapi_endpoint == "notifications":  # If the event is notifications (Commented by Agnirva.com)
                    # For Notifications, plot the number of notifications per day (Commented by Agnirva.com)
                    Agnirvadf_grouped = Agnirvadf.groupby('date').size().reset_index(name='count')  # Group data by date and count notifications (Commented by Agnirva.com)
                    
                    # Plotting with Plotly for interactivity (Commented by Agnirva.com)
                    st.markdown("### Selected Event Information")  # Add a markdown header (Commented by Agnirva.com)
                    st.write(Agnirvaevent_descriptions.get(Agnirvaapi_endpoint, "No description available."))  # Display event description (Commented by Agnirva.com)
                    
                    st.subheader(f"{Agnirvaselected_event_display} from {Agnirvastart_date} to {Agnirvaend_date}")  # Add a subheader with event and date range (Commented by Agnirva.com)
                    Agnirvafig = px.bar(Agnirvadf_grouped, x='date', y='count', title=f"Number of {Agnirvaselected_event_display} Over Time",  # Create a bar chart for notifications (Commented by Agnirva.com)
                                     labels={"date": "Date", "count": Agnirvay_label},  # Set axis labels (Commented by Agnirva.com)
                                     template="plotly_dark")  # Set the plot theme (Commented by Agnirva.com)
                    st.plotly_chart(Agnirvafig, use_container_width=True)  # Display the plotly chart (Commented by Agnirva.com)
                
                else:  # For other event types (Commented by Agnirva.com)
                    # For other event types, plot the count per day (Commented by Agnirva.com)
                    Agnirvadf_grouped = Agnirvadf.groupby('date').size().reset_index(name='count')  # Group data by date and count events (Commented by Agnirva.com)
                    
                    # Plotting with Plotly for interactivity (Commented by Agnirva.com)
                    st.markdown("### Selected Event Information")  # Add a markdown header (Commented by Agnirva.com)
                    st.write(Agnirvaevent_descriptions.get(Agnirvaapi_endpoint, "No description available."))  # Display event description (Commented by Agnirva.com)
                    
                    st.subheader(f"{Agnirvaselected_event_display} from {Agnirvastart_date} to {Agnirvaend_date}")  # Add a subheader with event and date range (Commented by Agnirva.com)
                    Agnirvafig = px.bar(Agnirvadf_grouped, x='date', y='count', title=f"Number of {Agnirvaselected_event_display} Over Time",  # Create a bar chart for event counts (Commented by Agnirva.com)
                                     labels={"date": "Date", "count": Agnirvay_label},  # Set axis labels (Commented by Agnirva.com)
                                     template="plotly_dark")  # Set the plot theme (Commented by Agnirva.com)
                    st.plotly_chart(Agnirvafig, use_container_width=True)  # Display the plotly chart (Commented by Agnirva.com)
                    
                # Show raw data (Commented by Agnirva.com)
                with st.expander("Show Raw Data"):  # Expander to show the raw DataFrame (Commented by Agnirva.com)
                    st.write(Agnirvadf)  # Display the raw DataFrame (Commented by Agnirva.com)
            else:  # If no data is available (Commented by Agnirva.com)
                st.write("No data available for the selected parameters.")  # Inform the user that no data is available (Commented by Agnirva.com)
