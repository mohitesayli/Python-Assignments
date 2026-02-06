import os
import sys
import shutil
import time

def WriteLog(message):
    with open("DirectoryCopy.log", "a") as f:
        f.write(time.ctime() + " : " + message + "\n")

def CopyFiles(src, dest):
    try:
        if not os.path.exists(src):
            WriteLog("Source directory not found")
            return

        if not os.path.exists(dest):
            os.mkdir(dest)
            WriteLog("Destination directory created")

        for file in os.listdir(src):
            src_path = os.path.join(src, file)
            dest_path = os.path.join(dest, file)

            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
                WriteLog(f"Copied file : {file}")

    except Exception as e:
        WriteLog(str(e))

def main():
    if len(sys.argv) != 3:
        WriteLog("Invalid arguments")
        return

    Source = sys.argv[1]
    Destination = sys.argv[2]

    CopyFiles(Source, Destination)

if __name__ == "__main__":
    main()
