# 🚨 ResQRoute – Intelligent Emergency Response System

ResQRoute is a real-time emergency response coordination platform that connects emergency vehicles, control rooms, and citizens. It aims to streamline the movement of emergency services by integrating smart routing, live signal mapping, and real-time notifications.

---

## 🔧 Features

### 👨‍💻 Citizen App
- Raise emergency requests (Medical, Fire, Accident, Crime, Rescue)
- Auto-detects current location via browser
- Notifies nearby emergency vehicles in real time
- Real-time status tracking of requests

### 🚑 Driver Dashboard
- View assigned emergency tasks
- See live emergency route map with signal points
- Receive navigation instructions to pickup/drop locations
- Update task status (en route, arrived, completed)

### 🧠 Control Room Dashboard
- Assign nearest vehicle based on location and availability
- Override traffic signals for emergency vehicle movement
- Live analytics on request types, average response time, and vehicle statuses

---

## 🗃️ Tech Stack

- **Frontend**: Streamlit (for Citizen App & Dashboards)
- **Backend**: Python
- **Database**: MySQL
- **Mapping**: Folium / Leaflet (Live Route & Signal Map)
- **Charting**: Plotly, Streamlit charts

---

## 🏗️ Project Structure

ResQRoute/ │ ├── backend/ │ ├── database.py # MySQL connection and query handlers │ ├── emergency_utils.py # Emergency finder and ETA logic │ └── signal_control.py # Smart signal override logic │ ├── citizen_app/ │ └── app.py # Citizen web interface │ ├── driver_dashboard/ │ └── app.py # Emergency vehicle dashboard │ ├── admin_dashboard/ │ └── app.py # Admin analytics dashboard │ ├── assets/ # Custom icons, images, logos │ ├── data/ # Sample CSVs if any fallback data is needed │ ├── requirements.txt # All dependencies └── README.md # You're here :)
 
2. Install dependencies:

pip install -r requirements.txt


3. Configure MySQL Database:

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Tanmay1@lol',
    'database': 'ResQRoute'
}


Tables in Database:

+---------------------+
| Tables_in_resqroute |
+---------------------+
| citizens            |
| drivers             |
| emergencies         |
| signal_logs         |
| signals             |
| tasks               |
| vehicles            |
+---------------------+


🚀 Deployed Apps Links:


1. Citizen App
[Live Demo](https://resqroute-citizen.onrender.com/)

2. Driver Dashboard
[Live Demo](https://resqroute-driverdashboard.onrender.com/)

3. Admin Dashboard
[Live Demo](https://resqroute-admindashboard.onrender.com/)

4. Control Room
[Live Demo](https://resqroute-controlroom.onrender.com/)


5. G Drive Link for Smart Signal DEMO and PPT

https://resqroute-controlroom.onrender.com/](https://drive.google.com/drive/folders/1jOpFL5HbiDZ0atpxDOxtQpu3maGTZA3H?usp=drive_link


📊 Admin Dashboard Analytics:
Pie Chart of Emergency Types

Total Vehicles vs On Duty/Available

Smart Alerts for system errors

Real-time dashboard with task metrics and statuses



📦 Python Dependencies:

Modules Used

streamlit
mysql-connector-python
pandas
folium
geopy
plotly
numpy
requests


💡 Future Improvements
Integration with Google Maps for more accurate routing

SMS/Email alerts to users

Mobile app version for drivers

Machine learning-based response prediction



👨‍🎓 Developed By:
ResQRoute

Member 1: Tanmay Kumar Singh
GitHub: https://github.com/Soultk1977
Email: soultk1977@gmail.com
Class: 12
School: Rajkiya Pratibha Vikas Vidyalaya, Karol Bagh, New Delhi

Member 2: Saubhagya Kumar Singh
GitHub: https://github.com/SirSaubhagya
Email: soulck1977@gmail.com
Class: 9
School: Rana Pratap (Sindhi) Sarvodaya Vidyalaya, R-Block, New Rajendra Nagar, New Delhi






