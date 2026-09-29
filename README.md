# WBGS print
# Lets you print files to the library printer in full colour, for free!


> [!NOTE]
> You must be connected to the **WGSB Wi-Fi** for the script to reach the printer.

## 1. Install Python (one-time)

1. Download the installer from [python.org/downloads](https://www.python.org/downloads/).
2. **Windows:** tick **"Add python.exe to PATH"** at the bottom of the installer *before* clicking Install.
3. **Mac/Linux:** Python 3 is usually already installed. Check by typing `python3 --version` in Terminal.

The script also needs `curl`, which is built into Windows 10 (version 1803 or later), Windows 11 and macOS.

## 2. Download the script

1. Open `LibPrint.py` in this repository.
2. Click the **Download raw file** icon (next to the **Raw** button, top-right of the file view).
3. Move `LibPrint.py` to your Desktop.

> [!TIP]
> Windows: if the file saved as `LibPrint.py.txt`, turn on *View > File name extensions* in File Explorer and rename it to `LibPrint.py`.

## 3. Run it

### Windows

1. Double-click `LibPrint.py`. A black window opens.
2. Drag your file into the window and press **Enter** (or paste the file path).
3. Choose the transfer format, or just press **Enter** for the default (see below).
4. Type how many copies you want, or just press **Enter** for 1.
5. Wait for "Success!", then press **Enter** to close the window.

### Mac and Linux

1. Open the **Terminal** app.
2. Type `python3 ` (with a space after it), then drag `LibPrint.py` into the Terminal window and press **Enter**.
3. When prompted, drag in the file you want to print and press **Enter**.
4. Follow the format and copies prompts as described below, then press **Enter** at the end to close.

### The prompts

| Prompt | What to enter |
| --- | --- |
| File | Drag and drop the file, or paste its path |
| Transfer format | Press **Enter** (Binary, the default) for PDFs, images and most files. Type `2` only for plain `.txt` files |
| Copies | Press **Enter** for 1, or type a number |

## What you can print

**PDF files work best.** Word, PowerPoint and similar files are not guaranteed to print through this method. If you have one of those, export or save it as a PDF first.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| **File not found** | Check the path for typos. Dragging the file into the window is the most reliable method. |
| **Double-click opens Notepad or a text editor, or nothing happens** | Python isn't installed, or the file was saved as `LibPrint.py.txt`. Install Python, check the file extension, then right-click the file and choose *Open with > Python*. |
| **`python` / `python3` is not recognised (Terminal)** | Python isn't installed or wasn't added to PATH. Re-run the installer and tick **"Add python.exe to PATH"**. |
| **`curl` is not installed** | Install curl, or update Windows to 10 (1803) or later. |
| **Curl error: connection timed out / failed to connect** | Make sure you're on the WGSB Wi-Fi. The library printer might also be switched off or offline. |
| **Sent successfully but nothing prints, or garbled output** | The printer can't read that file type. Convert it to PDF and try again. |
