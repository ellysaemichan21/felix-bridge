# 🚀 NATHAN FELIX LIVE BRIDGE — FRIEND & TEAM SETUP GUIDE
**Enterprise DevOps & Real-Time SFTP Pipeline — Designed by Nathan Felix**

This guide explains how to share and deploy the **Nathan Felix Live Bridge** across your team or with friends without triggering Windows Defender or Microsoft SmartScreen security alerts!

---

### 📂 Why is there a `felix_bridge/` folder AND launchers outside?
When sharing this tool with your team or friends, you will notice two parts:
1. **The Core Folder (`felix_bridge/`)**: This folder contains the underlying engine (`felix_app.py`, `felix_terminal.py`, and your configuration). This keeps your project root clean and organized!
2. **The Root Launchers (`gui.py`, `gui.cmd`, `connect.py`, `connect.cmd`)**: These launcher files sit **OUTSIDE** the folder, directly in your main project root (alongside `app/`, `resources/`, `public/`, etc.).

**Why do the launchers sit outside?**
Because they act as the **Bridge**! By running from the root directory of your project, the tool can monitor your entire codebase (`app/`, `resources/`, `routes/`, etc.) and automatically sync your changes over SFTP in real time (< 50ms) whenever you save a file in Antigravity or VS Code!

---

### 🛠️ How to Share & Deploy to a Friend's Laptop
To give this tool to a friend or deploy it on a new laptop:

1. **Copy the Files**: Copy the **`felix_bridge/`** folder AND the 4 launcher files (**`gui.py`**, **`gui.cmd`**, **`connect.py`**, **`connect.cmd`**) into the root directory of their project.
2. **Ensure Python is Installed**: Make sure their laptop has Python installed (with *"Add Python to PATH"* checked during installation).
3. **Launch the Bridge**:
   - **For the Graphical UI (Dark & Gold Design):** Double-click **`gui.cmd`** or run `python gui.py` in the terminal.
   - **For the Standalone Terminal UI:** Double-click **`connect.cmd`** or run `python connect.py` in the terminal.
4. **Automatic Dependency Setup**: When you double-click `gui.cmd` or `connect.cmd`, the script will automatically check and install all required Python libraries (`customtkinter`, `pillow`, `paramiko`)!

---

### 🛡️ Why This Architecture Bypasses Windows Defender
Unlike compiled `.exe` files created with PyInstaller (which Windows Defender and SmartScreen almost always block as "Untrusted Apps" due to lack of expensive code-signing certificates), **this tool runs directly through standard Python (`.py`) scripts**. 

Because Windows trusts the official Python interpreter, **your friends will never see a blue SmartScreen warning or have their antivirus block the application!**

---

### 💡 Need Help?
Contact **Nathan Felix** — Principal Architect & Creator of the Live Bridge Pipeline!
