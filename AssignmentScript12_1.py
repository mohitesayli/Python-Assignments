import os
import sys
import hashlib
import time

def WriteLog(message):
    with open("DirectoryChecksum.log", "a") as f:
        f.write(time.ctime() + " : " + message + "\n")

def CalculateChecksum(path):
    hobj = hashlib.md5()
    with open(path, "rb") as f:
        hobj.update(f.read())
    return hobj.hexdigest()

def DirectoryChecksum(dirname):
    if not os.path.isdir(dirname):
        WriteLog("Invalid directory")
        return

    for file in os.listdir(dirname):
        filepath = os.path.join(dirname, file)
        if os.path.isfile(filepath):
            checksum = CalculateChecksum(filepath)
            WriteLog(f"{file} : {checksum}")

def main():
    if len(sys.argv) != 2:
        WriteLog("Invalid arguments")
        return

    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()
