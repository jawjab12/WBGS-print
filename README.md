# WBGS-print

Allows you to print anything to the Library Printer, Free of charge and in full colour.

> **Disclaimer:** This script was created purely as a personal proof-of-concept and network testing tool. It is provided "as-is" for educational demonstration purposes. Use at your own discretion.

---

## 🛑 Important Requirement: Install Python First

Because this is an automation script, **your computer must have Python installed** for it to work. 

### How to install Python:
1. Go to the official website: [python.org/downloads](https://python.org)
2. Download and run the installer for your computer (Windows or Mac).
3. **CRITICAL STEP FOR WINDOWS:** When the installer opens, you **MUST check the box** at the bottom that says **"Add python.exe to PATH"** before clicking install. If you miss this, the script will not work.

---

## 📥 How to Download and Setup

Follow these quick steps to get the printing tool onto your computer:

1. Look at the right side of this GitHub page and click on the latest **Release** (`WBGS Library Print V1.0`).
2. Under the **Assets** section, click on **`LibPrint.py`** to download the script directly. 
3. Move the downloaded `LibPrint.py` file to an easy-to-find place, like your **Desktop**.

*Note: Make sure your computer is connected to **WGSB** before running the tool, or it won't be able to find the library printer.*

---

## 🚀 How to Run It

### Windows
1. Double-click the script file (`LibPrint.py`).
2. A black terminal window will open. 
3. **Drag and drop** the file you want to print straight into that window and press **Enter**. Alternatively, you can manually copy and paste the file path (for example: `C:\Users\Name\Downloads\image.png`).
4. Press **Enter** one more time to confirm. Your file is now in the library queue!

### macOS (Mac) & Linux
1. Open your **Terminal** app (press `Cmd + Space`, type *Terminal*, and press Enter).
2. Drag and drop the `LibPrint.py` file into the terminal window (or paste its file path) and press **Enter** to start it.
3. **Drag and drop** the file you want to print into the window when prompted (or paste its file path), and press **Enter**.
4. Press **Enter** again to complete the print request.

---

## 💡 Troubleshooting

* **File Not Found Error:** Make sure there aren't any extra spaces or strange symbols around your file name when you drag it in. If pasting a path manually, make sure it is exactly correct.
* **Connection Timed Out:** Double-check that you are fully logged into the school network. If you still can't connect, the library printer might be temporarily offline.
* **Script opens as a text document instead of running:** This means Python wasn't installed correctly or you forgot to check the **"Add to PATH"** box during installation. Re-run the Python installer and make sure that box is checked!
