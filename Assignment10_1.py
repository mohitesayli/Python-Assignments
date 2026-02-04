import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        return True
    else:
        return False
def main():
    Name = input("Enter file Name : ")
    if CheckFile(Name):
        print(f"{Name} Exists in Current directory")
    else:
        print(f"{Name} does not exists in current directory")

if __name__ == "__main__":
    main()