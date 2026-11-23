# Cyber Security Base: Course Project I

Course project detailing 5 security flaws from OWASP Top 10:2021 list as well as their fixes.

The application is a movie review website made with flask and sqlite3.

Original application repo: https://github.com/lapatinn/kirjainlaatikko

## Additional installation Instructions

### macOS

1. Clone the git repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Make a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Enter the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Install Flask:
   ```bash
   pip install flask
   ```
5. Run the app:
   ```bash
   flask run
   ```
6. The app will start on port 5000 and can be accessed via http://localhost:5000
7. Any changes made to the code will require a restart. Use `Ctrl + C` to stop the app and run it again with `flask run`.

> **Note:** On macOS Monterey and later, port 5000 may already be in use by the AirPlay Receiver. If so, either turn off AirPlay Receiver in **System Settings → General → AirDrop & Handoff**, or run the app on another port: `flask run --port 5001`

### Windows

These commands work in **Command Prompt** (cmd). PowerShell differences are noted below.

1. Clone the git repository:
   ```bat
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Make a virtual environment:
   ```bat
   python -m venv venv
   ```
3. Enter the virtual environment:
   ```bat
   venv\Scripts\activate
   ```
   In **PowerShell**, use:
   ```powershell
   venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks the script, run this first:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
4. Install Flask:
   ```bat
   pip install flask
   ```
5. Run the app:
   ```bat
   flask run
   ```
6. The app will start on port 5000 and can be accessed via http://localhost:5000
7. Any changes made to the code will require a restart. Use `Ctrl + C` to stop the app and run it again with `flask run`.
