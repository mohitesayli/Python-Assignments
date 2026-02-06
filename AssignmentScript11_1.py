import os
import sys
import time

def WriteLog(Message):
    with open("DirectoryFileSearch.log", "a") as f:
        f.write(time.ctime() + " : " + Message + "\n")

def ValidateInputs(DirName, Extension):
    if not os.path.isdir(DirName):
        WriteLog("Invalid directory")
        return False
    if not Extension.startswith("."):
        WriteLog("Invalid file extension")
        return False
    return True

def SearchFiles(DirName, Extension):
    WriteLog(f"Searching for {Extension} files in {DirName}")
    for file in os.listdir(DirName):
        if file.endswith(Extension):
            WriteLog(file)

def main():
    if len(sys.argv) != 3:
        WriteLog("Invalid arguments")
        return

    DirName = sys.argv[1]
    Extension = sys.argv[2]

    if ValidateInputs(DirName, Extension):
        SearchFiles(DirName, Extension)

if __name__ == "__main__":
    main()
