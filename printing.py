#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path  # Cross-platform path handling

def run_printer_upload():
    HOST = "172.24.77.24"
    USER = "anonymous"
    PASSWORD = ""

    print("=========================================")
    print("      PRINTER FTP UPLOAD LAUNCHER        ")
    print("=========================================\n")

    print("Step 1: Provide the file you want to print.")
    raw_input = input("   Drag & drop the file here or type the path: ").strip()
    
    # Securely strip quotes that come from drag-and-drop actions
    clean_path = raw_input.strip("'\"")
    
    # Path conversion ensures Windows backslashes are resolved properly
    local_file_path = Path(clean_path).resolve()
    
    if not local_file_path.exists() or not local_file_path.is_file():
        print(f"\nError: File '{clean_path}' not found.")
        print("Please check the path and try again.")
        print("\n" + "="*41)
        input("Press Enter to close this window...")
        return
        
    remote_filename = local_file_path.name

    print("\nStep 2: Select transfer format.")
    print("   [1] Binary mode (For PDFs, Images, PostScript, PCL, Documents) - RECOMMENDED")
    print("   [2] ASCII mode  (For Plain Text, raw text logs, script files)")
    choice = input("   Enter choice (1 or 2, default is 1): ").strip()

    extra_args = []
    if choice == "2":
        extra_args.append("--ascii")
        mode_text = "ASCII"
    else:
        mode_text = "Binary"

    ftp_url = f"ftp://{HOST}/lp/{remote_filename}"
    
    # local_file_path is converted to a string format native to the host OS
    curl_command = [
        "curl",
        "--user", f"{USER}:{PASSWORD}",
        "-T", str(local_file_path),
        ftp_url
    ] + extra_args

    print(f"\nSending '{remote_filename}' via {mode_text} mode to printer...")
    
    try:
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        print("\nSuccess! The file has been sent to the printer queue.")
        
    except subprocess.CalledProcessError as e:
        print("\nCurl Error: Could not send file to printer.")
        print("Details:", e.stderr if e.stderr else "Connection timed out or printer is unreachable.")
    except FileNotFoundError:
        print("\nSystem Error: 'curl' utility is not installed on this system.")
        print("Please install curl to run this script.")

    print("\n" + "="*41)
    input("Process finished. Press Enter to close this window...")

if __name__ == "__main__":
    run_printer_upload()
