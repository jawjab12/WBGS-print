# WBGS-print

Allows you to print anything to the Library Printer, free of charge and in full colour. Feel free to make a pull request if you know what you are doing.

> [!WARNING]
> **Disclaimer:** This script is a personal proof-of-concept/network testing tool provided "as-is" for educational demonstration purposes. Use at your own discretion.

---

## 1. Setup Python (Required)

Your computer needs Python to run this automation script.
* **Download:** Get the installer from [python.org](https://python.org).
* **Crucial Windows Step:** You **MUST** check the box that says **"Add python.exe to PATH"** at the bottom of the installer before clicking install, or the script will break.

---

## 2. Download the Script

1. Look at the main file list at the top of this GitHub repository.
2. Click on the **`LibPrint.py`** file.
3. Click the **Raw** button in the top-right corner of the file view.
4. Right-click anywhere on the page and select **Save As...** (or press `Ctrl + S` / `Cmd + S`) to save it.
5. Move the **`LibPrint.py`** file to your **Desktop**.

> [!NOTE]
> You must be actively connected to WGSB Wi-Fi for the script to reach the printer.

---

## 3. How to Run It

### Windows
1. Double-click **`LibPrint.py`**.
2. Drag and drop your file into the black window and press **Enter** (or paste the file path manually).
3. Press **Enter** again to confirm and send it to the library queue!

### macOS (Mac) & Linux
1. Open the **Terminal** app.
2. Drag and drop the **`LibPrint.py`** file into the terminal window and press **Enter**.
3. Drag and drop the file you want to print into the window when prompted, then press **Enter** twice to complete.

---

## Troubleshooting

* **File Not Found:** Check for accidental spaces or symbols in your file path.
* **Connection Timed Out:** Make sure you are logged into the school Wi-Fi. The library printer might also be offline.
* **Opens as text instead of running:** Python is missing or wasn't added to your PATH. Re-run the Python installer and remember to check the "Add to PATH" box!
