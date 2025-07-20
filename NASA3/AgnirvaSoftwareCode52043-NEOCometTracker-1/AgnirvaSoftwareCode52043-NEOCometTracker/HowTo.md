To run the provided Python code, follow these detailed step-by-step instructions. This guide is designed for individuals with no prior experience in coding or technology, ensuring that anyone can set up and use the application successfully.

---

### **1. Ensure You Have a Computer with Internet Access**

Before starting, make sure you have access to a desktop or laptop computer connected to the internet. You'll need internet access to download necessary software and to allow the application to fetch data from online APIs.

---

### **2. Install Python on Your Computer**

Python is a programming language that the provided code is written in. Follow the instructions below based on your operating system to install Python.

- **For Windows Users:**
  1. Open your web browser and go to the [Python Downloads Page](https://www.python.org/downloads/windows/).
  2. Click on the latest version of Python (e.g., Python 3.11.5).
  3. Scroll down to the "Files" section and download the **Windows installer** (either 64-bit or 32-bit, depending on your system).
  4. Once downloaded, open the installer.
  5. **Important:** During installation, check the box that says **"Add Python to PATH."**
  6. Click **"Install Now"** and follow the on-screen instructions to complete the installation.

- **For Mac Users:**
  1. Open your web browser and navigate to the [Python Downloads Page](https://www.python.org/downloads/mac-osx/).
  2. Click on the latest Python version to download the **macOS installer**.
  3. Once the download is complete, open the installer package.
  4. Follow the on-screen instructions to install Python.

- **For Linux Users:**
  - Most Linux distributions come with Python pre-installed. To check, open the Terminal and type:
    ```
    python3 --version
    ```
    If Python is not installed, you can install it using your distribution's package manager. For example, on Ubuntu:
    ```
    sudo apt update
    sudo apt install python3
    ```

---

### **3. Verify Python Installation**

After installation, ensure Python is installed correctly.

1. **Open the Command Prompt (Windows) or Terminal (Mac/Linux):**
   - **Windows:** Press `Win + R`, type `cmd`, and press Enter.
   - **Mac/Linux:** Open the Terminal application.

2. **Check Python Version:**
   - Type the following command and press Enter:
     ```
     python --version
     ```
     or
     ```
     python3 --version
     ```
   - You should see a response like `Python 3.x.x`. If you see an error, revisit the installation steps.

---

### **4. Install a Code Editor**

A code editor allows you to write and edit code easily. **Visual Studio Code (VS Code)** is a free and user-friendly option.

- **Download Visual Studio Code:**
  1. Go to the [VS Code Download Page](https://code.visualstudio.com/).
  2. Click on the download button for your operating system.
  3. Once downloaded, open the installer and follow the on-screen instructions to install VS Code.

---

### **5. Create a Project Folder**

Organizing your files is essential. Create a dedicated folder for this project.

1. **Choose a Location:**
   - You can create the folder on your Desktop or in your Documents.

2. **Create the Folder:**
   - **Windows:**
     - Right-click on the chosen location.
     - Select **"New"** > **"Folder."**
     - Name the folder, e.g., `AgnirvaApp`.
   - **Mac/Linux:**
     - Right-click or use the appropriate method to create a new folder.
     - Name it similarly, e.g., `AgnirvaApp`.

---

### **6. Open the Project Folder in VS Code**

1. **Launch VS Code:**
   - Open Visual Studio Code from your applications or programs menu.

2. **Open the Folder:**
   - Click on **"File"** in the top menu.
   - Select **"Open Folder..."**
   - Navigate to the `AgnirvaApp` folder you created and open it.

---

### **7. Create a Python File for the Code**

1. **Inside VS Code:**
   - Click on the **"New File"** icon or press `Ctrl + N` (Windows) or `Cmd + N` (Mac).
   
2. **Save the File:**
   - Click on **"File"** > **"Save As..."**
   - Navigate to the `AgnirvaApp` folder.
   - Name the file `app.py` and ensure it has the `.py` extension.
   - Click **"Save."**

---

### **8. Copy and Paste the Provided Code into `app.py`**

1. **Copy the Code:**
   - Select all the code you provided (from `import streamlit as st` to the end).
   - Right-click and choose **"Copy,"** or press `Ctrl + C` (Windows) or `Cmd + C` (Mac).

2. **Paste into `app.py`:**
   - Go back to VS Code with the `app.py` file open.
   - Click inside the file and paste the code by right-clicking and selecting **"Paste,"** or pressing `Ctrl + V` (Windows) or `Cmd + V` (Mac).

3. **Save the File:**
   - Click on **"File"** > **"Save,"** or press `Ctrl + S` (Windows) or `Cmd + S` (Mac).

---

### **9. Install Required Python Libraries**

The code relies on several Python libraries. Follow these steps to install them:

1. **Open the Terminal in VS Code:**
   - In VS Code, click on **"Terminal"** in the top menu.
   - Select **"New Terminal."**
   - A terminal window will appear at the bottom of VS Code.

2. **Create a Virtual Environment (Optional but Recommended):**
   - Virtual environments help manage project-specific dependencies.
   - **Create Virtual Environment:**
     ```
     python -m venv env
     ```
     or
     ```
     python3 -m venv env
     ```
   - **Activate Virtual Environment:**
     - **Windows:**
       ```
       env\Scripts\activate
       ```
     - **Mac/Linux:**
       ```
       source env/bin/activate
       ```
   - **Note:** After activation, your terminal prompt will change to indicate the virtual environment is active.

3. **Upgrade `pip`:**
   - Ensure you have the latest version of `pip`, the Python package manager.
     ```
     pip install --upgrade pip
     ```

4. **Install Required Libraries:**
   - Run the following command to install all necessary libraries at once:
     ```
     pip install streamlit requests pandas plotly statsmodels
     ```

---

### **10. Obtain a NASA API Key (Optional but Recommended)**

While the provided code uses NASA's API without an explicit API key, obtaining your own key can help avoid potential rate limits and ensure smoother operation.

1. **Visit NASA's API Portal:**
   - Go to the [NASA API Signup Page](https://api.nasa.gov/).

2. **Request an API Key:**
   - Fill out the required information, such as your name and email address.
   - Submit the form to receive your unique API key via email.

3. **Update the Code with Your API Key (If Needed):**
   - If the API requires an API key in the future, you can include it in the API request parameters within the code.
   - **Example:** Add a parameter like `'api_key': 'YOUR_API_KEY'` to the `Agnirvaparams` dictionary in the `Agnirvafetch_close_approaches` function.

4. **Note:** Currently, the code uses the default settings, and an API key may not be necessary. However, having your own key is beneficial for extended use.

---

### **11. Run the Streamlit Application**

Now that everything is set up, you can run the application.

1. **Ensure You're in the Project Folder:**
   - In the terminal, navigate to the `AgnirvaApp` folder if you're not already there.
     ```
     cd path_to_your_project_folder/AgnirvaApp
     ```
     Replace `path_to_your_project_folder` with the actual path.

2. **Run the Application:**
   - In the terminal, type the following command and press Enter:
     ```
     streamlit run app.py
     ```
   - **What Happens Next:**
     - Streamlit will start the application.
     - It may ask to open a browser window automatically. If it doesn't, look for a local URL in the terminal (e.g., `http://localhost:8501`) and open it in your web browser.

3. **Keep the Terminal Open:**
   - The application runs in the terminal. Keep it open while using the app.

---

### **12. Interact with the Application**

Once the application is running in your browser, here's how to use it:

1. **Welcome Screen:**
   - You'll see a title and a brief description of the **Asteroid and Comet Close Approaches Visualizer**.

2. **Sidebar Inputs:**
   - **Select Celestial Body:**
     - Choose a celestial body (e.g., Earth, Mars) from the dropdown menu to analyze close approaches to it.
   - **Date Range:**
     - **Start Date:** Pick the beginning date for your search.
     - **End Date Option:** Choose between specifying the number of days from the start date or selecting a specific end date.
     - **Maximum Distance:** Enter the maximum distance (in Astronomical Units or Lunar Distances) for close approaches.
   - **Object Type & Results:**
     - **Object Type:** Filter results by Near-Earth Objects (NEO), Comets, or Both.
     - **Number of Results to Fetch:** Specify how many records you want to retrieve.
   - **Fetch and Visualize Data:**
     - Click the **"🚀 Fetch and Visualize Data"** button to retrieve and display the data based on your inputs.

3. **Viewing Data:**
   - After fetching, a data table will display close approach information, including designation, date, distance, relative velocity, and infinity velocity.
   - You can download this data as a CSV file by clicking the **"📥 Download Data as CSV"** button.

4. **Visualization:**
   - A scatter plot visualizes the close approaches.
   - **Add Trendline:** If you have `statsmodels` installed, you can add a trendline by checking the **"✨ Add Trendline"** box.

5. **Information and Sources:**
   - At the bottom, you'll see information about the data source (JPL's SSD/CNEOS CAD API) and the creator (Agnirva).

---

### **13. Using the Application on Different Devices**

The application is designed to work on both desktop and mobile devices. However, for the best experience, using a desktop or laptop is recommended due to the screen size and interface elements.

---

### **14. Close the Application**

When you're done using the application:

1. **Stop the Application:**
   - Go to the terminal where the application is running.
   - Press `Ctrl + C` (Windows/Linux) or `Cmd + C` (Mac) to stop the Streamlit server.

2. **Deactivate the Virtual Environment (If Used):**
   - In the terminal, type:
     ```
     deactivate
     ```
   - Press Enter.

---

### **15. Reopen and Use the Application Again**

To use the application in the future:

1. **Open VS Code and Your Project Folder (`AgnirvaApp`).**

2. **Activate the Virtual Environment (If Used):**
   - **Windows:**
     ```
     env\Scripts\activate
     ```
   - **Mac/Linux:**
     ```
     source env/bin/activate
     ```

3. **Run the Application:**
   ```
   streamlit run app.py
   ```

---

By following these comprehensive steps, anyone can set up, run, and interact with the **Agnirva Asteroid & Comet Close Approaches Visualizer**, even without prior coding experience. Enjoy exploring celestial close approaches with your new application!