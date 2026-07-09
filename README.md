Real-Time E-Commerce Analytics & Monitoring Platform
This project is a real-time data aggregation, analytics, and system monitoring (SRE) platform designed for e-commerce environments. It continuously tracks business metrics alongside infrastructure health to simulate an enterprise-grade production environment.

Tech Stack & Technologies Used
Backend & API: FastAPI, Python
Data Processing: Pandas
Storage Engine: SQLite (SQL)
Visual Dashboard: Streamlit
System Monitoring: psutil

 How to Run the Project
Follow these steps to set up and run the platform locally:

1. Install Dependencies
Install all the required Python libraries using pip:
pip install -r requirements.txt
2. Initialize the Database
Create and set up the localized SQL database schema:
python database.py
3. Start the Real-Time Data Generator
Launch the background script to simulate continuous user activity and incoming orders:
python generator.py
4. Launch the Visual Dashboard
Run the Streamlit application to open the live analytics and SRE monitoring dashboard in your browser:
streamlit run dashboard.py
