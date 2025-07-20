To run this code, follow these detailed step-by-step instructions. This guide assumes no prior technical knowledge and breaks everything down as simply as possible.

---

### **1. Ensure You Have a Computer with Internet Access**
   - **Requirements**:
     - A desktop or laptop computer.
     - An active internet connection.
     - Administrative access to install software if necessary.

### **2. Install Python on Your Computer**
   Python is a programming language required to run this application.
   
   - **For Windows**:
     1. Open your web browser and go to the [Python Downloads Page](https://www.python.org/downloads/windows/).
     2. Click on the latest Python version (e.g., Python 3.11.x).
     3. Download the "Windows installer (64-bit)".
     4. Run the downloaded installer.
     5. **Important**: During installation, check the box that says **"Add Python to PATH"**.
     6. Click "Install Now" and follow the on-screen instructions.

   - **For Mac**:
     1. Open your web browser and navigate to the [Python Downloads Page](https://www.python.org/downloads/mac-osx/).
     2. Click on the latest Python version (e.g., Python 3.11.x).
     3. Download the "macOS installer".
     4. Run the downloaded installer and follow the on-screen instructions.

   - **For Linux**:
     Python often comes pre-installed on Linux distributions. To check, open the Terminal and type:
     ```
     python3 --version
     ```
     If Python is not installed, refer to your distribution’s package manager to install it. For example, on Ubuntu:
     ```
     sudo apt update
     sudo apt install python3 python3-pip
     ```

### **3. Verify Python Installation**
   - Open the **Command Prompt** on Windows or **Terminal** on Mac/Linux.
   - Type the following command and press Enter:
     ```
     python --version
     ```
     or
     ```
     python3 --version
     ```
   - You should see a response like `Python 3.11.x`. If not, revisit step 2 to ensure Python is correctly installed.

### **4. Install a Code Editor (Optional but Recommended)**
   A code editor helps in viewing and editing code files.
   
   - **Recommended Editor**: [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
     1. Go to the [VS Code Download Page](https://code.visualstudio.com/Download).
     2. Download the installer for your operating system.
     3. Run the installer and follow the prompts to install.

   - **Alternative Editors**:
     - **Notepad++** for Windows: [Download Here](https://notepad-plus-plus.org/downloads/)
     - **Sublime Text**: [Download Here](https://www.sublimetext.com/download)

### **5. Open Your Web Browser**
   You will need a web browser like **Google Chrome**, **Mozilla Firefox**, **Microsoft Edge**, or **Safari** to access the application once it's running.

### **6. Install Required Python Packages**
   The application relies on several Python libraries. These need to be installed using `pip`, Python’s package installer.

   - **Steps**:
     1. Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
     2. Type the following commands one by one, pressing Enter after each:
        ```
        pip install streamlit
        pip install requests
        pip install pandas
        pip install plotly
        ```
     3. Wait for each installation to complete. You should see messages indicating successful installations.

### **7. Obtain a NASA API Key (Optional)**
   The application uses NASA’s DONKI API to fetch space weather data. While the code uses a default `DEMO_KEY`, it has rate limits. For extended usage, obtaining a personal API key is recommended.

   - **How to Get a NASA API Key**:
     1. Open your web browser and navigate to the [NASA API Portal](https://api.nasa.gov/).
     2. Click on **"Sign Up"** or **"Get Started"**.
     3. Fill in the required information to create an account.
     4. After signing up, you will receive a unique **API Key** via email or directly on the website.
     5. **Note**: Keep your API key secure and do not share it publicly.

   - **Using the API Key**:
     - When running the application, you can enter your API key in the designated input field to replace the `DEMO_KEY` and avoid rate limits.

### **8. Prepare the Application Code**
   You need to save the provided Python code into a file on your computer.

   - **Steps**:
     1. Open your **Code Editor** (e.g., Visual Studio Code).
     2. Create a new file:
        - In VS Code: Click on **"File"** > **"New File"**.
     3. Copy the entire Python code provided (starting with `import streamlit as st` and ending with the last line of code).
     4. Paste the copied code into the new file in your editor.
     5. Save the file:
        - Click on **"File"** > **"Save As"**.
        - Name the file `space_weather_app.py` (ensure it ends with `.py`).
        - Choose a location that's easy to find, like the **Desktop** or a dedicated **Projects** folder.

### **9. Open Command Prompt or Terminal in the Code Directory**
   To run the application, you need to navigate to the folder where you saved the `space_weather_app.py` file.

   - **Steps**:
     1. **Locate the Folder**:
        - Navigate to the folder where you saved `space_weather_app.py` (e.g., Desktop).
     2. **Open Command Prompt/Terminal**:
        - **Windows**:
          - Click on the **Start** menu.
          - Type `cmd` and press Enter to open Command Prompt.
          - In Command Prompt, type:
            ```
            cd Desktop
            ```
            (Replace `Desktop` with your folder name if different.)
        - **Mac/Linux**:
          - Open **Terminal**.
          - Type:
            ```
            cd ~/Desktop
            ```
            (Replace `Desktop` with your folder name if different.)

### **10. Run the Streamlit Application**
   Now, you'll execute the Python script to launch the application.

   - **Steps**:
     1. In the Command Prompt or Terminal, ensure you are in the directory containing `space_weather_app.py`.
     2. Type the following command and press Enter:
        ```
        streamlit run space_weather_app.py
        ```
     3. The first time you run this, Streamlit may perform some setup tasks. Wait for it to complete.

### **11. Access the Application in Your Web Browser**
   After running the command, Streamlit will automatically open the application in your default web browser. If it doesn’t, follow these steps:

   - **Steps**:
     1. Look at the Command Prompt or Terminal window. You should see a message like:
        ```
        Local URL: http://localhost:8501
        Network URL: http://192.168.x.x:8501
        ```
     2. Open your web browser.
     3. Enter the **Local URL** (e.g., `http://localhost:8501`) into the address bar and press Enter.
     4. The **Agnirva Space Weather Visualizer** should now be visible.

### **12. Understand What the Application Does**
   The **Agnirva Space Weather Visualizer** is a web application that displays trends in space weather events using data from NASA's DONKI API. You can explore various events such as Coronal Mass Ejections (CME), Geomagnetic Storms (GST), Solar Flares (FLR), and more.

### **13. Configure the Application Settings**
   Use the sidebar on the left to customize your data visualization.

   - **Steps**:
     1. **Enter Your NASA API Key**:
        - In the sidebar, locate the input box labeled **"Enter your NASA API Key:"**.
        - If you have obtained a personal API key, enter it here. If not, the default `DEMO_KEY` will be used (note that this may have limited usage).
     2. **Select Space Weather Event Type**:
        - Click on the dropdown menu labeled **"Select Space Weather Event Type:"**.
        - Choose the event you are interested in, such as **CME (Coronal Mass Ejection)** or **GST (Geomagnetic Storm)**.
     3. **Set the Date Range**:
        - Below the event type, you'll see **"Start Date:"** and **"End Date:"**.
        - Click on each date picker to select the range of dates for which you want to view data.
        - **Note**: The start date must be before the end date. If not, an error message will appear.
     4. **Fetch Data**:
        - After configuring the above settings, click the **"Fetch Data"** button.
        - The application will retrieve the relevant data based on your selections.

### **14. Interact with the Data Visualizations**
   Once data is fetched, the application will display interactive plots and information.

   - **Features**:
     1. **Trend Graphs**:
        - Visual representations (line charts or bar charts) showing the number or intensity of selected space weather events over the chosen date range.
     2. **Event Information**:
        - Detailed descriptions of the selected space weather event type.
     3. **Raw Data**:
        - An expandable section labeled **"Show Raw Data"** where you can view the underlying data used for the visualizations.
     4. **Debugging Information**:
        - Another expandable section labeled **"Show Raw JSON Data for Debugging"** provides the raw JSON response from the NASA API, useful for advanced users or troubleshooting.

### **15. Utilize Additional Sidebar Sections**
   The sidebar contains helpful sections to enhance your understanding and usage of the app.

   - **Event Information**:
     - Click on the **"ℹ️ What is this event?"** expander to read more about the selected space weather event.
   
   - **Glossary**:
     - Expand the **"📖 View Glossary"** section to see definitions of all event types included in the application.
   
   - **Help**:
     - Click on the **"❓ How to Use This App"** expander for a step-by-step guide on using the application features.

### **16. Clear or Reset the Data**
   If you wish to change your selections or start over:

   - **Steps**:
     1. Modify any of the sidebar inputs (e.g., change the event type or date range).
     2. Click the **"Fetch Data"** button again to update the visualizations with new parameters.

### **17. Stop the Application**
   When you’re done using the application:

   - **Steps**:
     1. Return to the **Command Prompt** or **Terminal** where the application is running.
     2. Press `Ctrl+C` on your keyboard.
     3. Confirm the termination if prompted.

### **18. Troubleshooting Common Issues**
   - **Application Doesn’t Open in Browser**:
     - Ensure you have an active internet connection.
     - Verify that the Command Prompt or Terminal shows no error messages.
     - Manually enter the Local URL (e.g., `http://localhost:8501`) in your web browser.
   
   - **Error Fetching Data**:
     - Check if you entered a valid NASA API key.
     - Ensure the date range is correct and that data exists for those dates.
     - Verify your internet connection.

   - **Missing Python Packages**:
     - If you encounter errors related to missing packages, revisit step 6 to ensure all required libraries are installed.

### **19. Reopen and Use the Application Again**
   To use the application in the future:

   - **Steps**:
     1. Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
     2. Navigate to the directory containing `space_weather_app.py` using the `cd` command.
        ```
        cd path_to_your_directory
        ```
        Replace `path_to_your_directory` with the actual path (e.g., `cd Desktop`).
     3. Run the application with:
        ```
        streamlit run space_weather_app.py
        ```
     4. Access the application in your web browser as described in step 11.

---

By following these steps, anyone can successfully run and interact with the **Agnirva Space Weather Visualizer**, gaining insights into various space weather events using NASA’s data. This guide ensures that even individuals with no prior coding or technical experience can navigate and utilize the application effectively.