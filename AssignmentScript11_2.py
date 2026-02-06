import os
import sys
import time

def WriteLog(Message):
    with open("DirectoryRename.log", "a") as f:
        f.write(time.ctime() + " : " + Message + "\n")

def ValidateInputs(DirName, OldExt, NewExt):
    if not os.path.isdir(DirName):
        WriteLog("Invalid directory")
        return False
    if not OldExt.startswith(".") or not NewExt.startswith("."):
        WriteLog("Invalid file extension")
        return False
    if OldExt == NewExt:
        WriteLog("Old and New extensions are same")
        return False
    return True


def RenameFiles(DirName, OldExt, NewExt):
    WriteLog(f"Renaming {OldExt} files to {NewExt}")
    for file in os.listdir(DirName):
        if file.endswith(OldExt):
            OldPath = os.path.join(DirName, file)
            NewFile = file.replace(OldExt, NewExt)
            NewPath = os.path.join(DirName, NewFile)
            os.rename(OldPath, NewPath)
            WriteLog(f"Renamed: {file} -> {NewFile}")

def main():
    if len(sys.argv) != 4:
        WriteLog("Invalid arguments")
        return

    DirName = sys.argv[1]
    OldExt = sys.argv[2]
    NewExt = sys.argv[3]

    if ValidateInputs(DirName, OldExt, NewExt):
        RenameFiles(DirName, OldExt, NewExt)

if __name__ == "__main__":
    main()
