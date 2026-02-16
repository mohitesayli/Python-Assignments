import os
import sys
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

LOG_DIR = "Logs"
HISTORY_FILE = "BackupHistory.txt"
SENDER_EMAIL = "saylimohite1902@gmail.com"
APP_PASSWORD = "acdmwrrdiiutdkay"
EXCLUDE_EXT = [".tmp", ".log", ".exe"]

def CreateLogDir():
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

def WriteLog(data):
    CreateLogDir()
    logfile = os.path.join(LOG_DIR, "BackupLog.txt")
    with open(logfile, "a") as f:
        f.write(data + "\n")

def calculate_hash(path):
    hobj = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            hobj.update(data)
    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_files = []
    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            if any(file.endswith(ext) for ext in EXCLUDE_EXT):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)
                z.write(full_path, relative)

    return zip_name

def UpdateHistory(zip_name, file_count):
    size = os.path.getsize(zip_name) / (1024 * 1024)

    with open(HISTORY_FILE, "a") as f:
        f.write(f"{time.ctime()} | Files: {file_count} | "
                f"Zip: {zip_name} | Size: {size:.2f} MB\n")

def ShowHistory():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            print(f.read())
    else:
        print("No backup history found.")

def SendMail(receiver, zip_file):
    msg = EmailMessage()
    msg['Subject'] = "Marvellous Data Shield Backup Report"
    msg['From'] = "saylimohite1902@gmail.com"
    msg['To'] = receiver

    msg.set_content("Backup completed successfully. Log and Zip attached.")

    # Attach Zip
    with open(zip_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(zip_file)
        )

    # Attach Log
    logfile = os.path.join(LOG_DIR, "BackupLog.txt")
    if os.path.exists(logfile):
        with open(logfile, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename="BackupLog.txt"
            )

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("saylimohite1902@gmail.com", "acdmwrrdiiutdkay")
    server.send_message(msg)
    server.quit()

def RestoreBackup(zipfile_name, destination):
    with zipfile.ZipFile(zipfile_name, 'r') as z:
        z.extractall(destination)
    print("Restore Completed Successfully.")

def MarvellousDataShieldStart(Source, receiver=None):

    Border = "-" * 50
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Started at:", time.ctime())
    print(Border)

    WriteLog("Backup started at: " + time.ctime())

    files = BackupFiles(Source, BackupName)
    zip_file = make_zip(BackupName)

    WriteLog(f"Files Copied: {len(files)}")
    WriteLog(f"Zip Created: {zip_file}")
    WriteLog(Border)

    UpdateHistory(zip_file, len(files))

    print("Backup Completed Successfully")
    print("Files Copied:", len(files))
    print("Zip Created:", zip_file)

    if receiver:
        SendMail(receiver, zip_file)

def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Data Shield System -----")
    print(Border)

    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        ShowHistory()

    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        RestoreBackup(sys.argv[2], sys.argv[3])

    elif len(sys.argv) == 4:
        interval = int(sys.argv[1])
        source = sys.argv[2]
        receiver = sys.argv[3]

        schedule.every(interval).minutes.do(
            MarvellousDataShieldStart, source, receiver)

        print("Data Shield System Started...")
        print("Press Ctrl+C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("Backup: Script.py <interval> <source> <receiver_email>")
        print("Restore: Script.py --restore <zipfile> <destination>")
        print("History: Script.py --history")

    print(Border)

if __name__ == "__main__":
    main()
