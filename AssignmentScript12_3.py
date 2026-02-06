import os
import sys
import hashlib
import time

def WriteLog(message):
    with open("Log.txt", "a") as f:
        f.write(time.ctime() + " : " + message + "\n")

def GetChecksum(path):
    hobj = hashlib.md5()
    with open(path, "rb") as f:
        hobj.update(f.read())
    return hobj.hexdigest()

def RemoveDuplicate(dirname):
    if not os.path.isdir(dirname):
        WriteLog("Invalid directory")
        return

    files = {}
    for file in os.listdir(dirname):
        path = os.path.join(dirname, file)
        if os.path.isfile(path):
            checksum = GetChecksum(path)
            if checksum in files:
                os.remove(path)
                WriteLog(f"Removed duplicate file : {file}")
            else:
                files[checksum] = file

def main():
    if len(sys.argv) != 2:
        WriteLog("Invalid arguments")
        return

    RemoveDuplicate(sys.argv[1])

if __name__ == "__main__":
    main()
