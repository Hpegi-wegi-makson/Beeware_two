
<div align="center">
  <img width="634" height="506" alt="Снимок экрана 2025-11-05 012314" src="https://github.com/user-attachments/assets/d68e5bc7-1f0a-4e57-8ff7-fbeb05897980" /><img width="643" height="502" alt="Снимок экрана 2025-11-05 012300" src="https://github.com/user-attachments/assets/d713015a-12c7-44ad-a3b7-1ff81a8ae532" /><img width="636" height="499" alt="Снимок экрана 2025-11-05 012244" src="https://github.com/user-attachments/assets/14f28512-d036-499e-8221-3e896eff43b0" />



🔐 BeeWare Authentication App  

A simple and elegant desktop application for user authentication

</div>
✨ Features
Feature	Description
🔑 Authentication	User login and registration
⌨️ Virtual Keyboard	Custom keyboard for convenient input
💾 Data Storage	SQLite database for accounts and logs
📊 Logging	Record all authorization attempts
✅ Validation	Check input data correctness
🏗 Architecture
Technology Stack
Frontend: Toga (BeeWare) - native UI framework

Backend: Python 3.x

Database: SQLite3

Platform: Desktop (cross-platform)

Database Structure
📋 Table Log
sql
CREATE TABLE IF NOT EXISTS Log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    login TEXT,
    password TEXT,
    result TEXT
)
👥 Table account
sql
CREATE TABLE IF NOT EXISTS account (
    id INTEGER PRIMARY KEY,
    id_log INTEGER,
    timestamp TEXT,
    login TEXT,
    password TEXT,
    FOREIGN KEY (id_log) REFERENCES Log (id)
)
🎮 Interface
Application Screens:
🚀 Start Screen - choose between login and registration

🔐 Login Screen - authorization for existing users

📝 Registration Screen - create new account

Keyboard Features:
🎯 Automatic display on focus

🔄 Two independent keyboards

⌫ Backspace function for character deletion

⚡ Quick Start
Installation
bash
pip install toga
Running
bash
python main.py
🎯 Core Functions
Component	Purpose
HelloWorld	Main application class
generate_keyboard()	Create virtual keyboard
сheck_to_register()	Validate user credentials
get_account()	Retrieve user data
qget_account()	Register new user
🔍 Usage Example
Launch the application

Choose "Login in" for login or "Registration" for new account

Enter data using virtual keyboard

Receive authorization result

📝 Operation Logging
The application records to database:

⏰ Operation timestamps

👤 Entered logins and passwords

✅ Authorization check results

🔄 Relationships between accounts and logs

<div align="center">
Developed with BeeWare Toga
Cross-platform Python application

</div>
