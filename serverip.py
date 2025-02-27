# This just accesses Roblox's files & obtains the Server IP (useless, just press Shift + F3) This was just made for fun.
import glob
import os
from time import sleep

os.system("title ROBLOX Server IP Finder")

print(r"""
============================================
      Divine Intention      
============================================

- This script obtains the server's IP of the game you're in.  
- Make sure you're fully loaded into the game before running.  
""")

input("[INFO] Press [ENTER] to scan Roblox logs for the server IP..")

username = os.getenv("username")
log_path = f"C:\\Users\\{username}\\AppData\\Local\\Roblox\\logs\\"

try:
    log_files = glob.glob(log_path + "*")
    if not log_files:
        raise FileNotFoundError("No logs found. Make sure Roblox is installed properly and has been opened at least one time.")

    latest_log = max(log_files, key=os.path.getctime)

    with open(latest_log, "r", encoding="utf-8", errors="ignore") as log_file:
        for line in log_file:
            if "Connection accepted from" in line:
                ip_address = line.split("Connection accepted from ")[-1].split("|")[0].strip()
                print(f"\n[SUCCESS] Server IP Found: {ip_address}")
                break
        else:
            print("[WARNING] No server IP found. Try rejoining the game and running the script again.")
except Exception as e:
    print(f"[ERROR] {e}")
