import sys
import os
import hashlib
import time

def WriteLog(message):
    with open("Log.txt", "a") as f:
        f.write(message + "\n")

def Checksum(path):
    fd = open(path, 'rb')
    hobj = hashlib.md5()
    hobj.update(fd.read())
    fd.close()
    return hobj.hexdigest()

def RemoveDuplicates(dirname):
    data = {}

    for folder, subfolder, files in os.walk(dirname):
        for file in files:
            path = os.path.join(folder, file)
            hashcode = Checksum(path)

            if hashcode in data:
                os.remove(path)
                WriteLog("Deleted : " + file)
            else:
                data[hashcode] = path

def main():
    start = time.time()

    if len(sys.argv) != 2:
        WriteLog("Invalid arguments")
        return

    RemoveDuplicates(sys.argv[1])

    end = time.time()
    WriteLog("Execution time : " + str(end - start) + " seconds")

if __name__ == "__main__":
    main()
