import sys

def CopyFile(Source):
    try:
        with open(Source,"r")as f1:
            Data = f1.read()
        with open("Demo.txt","w")as f2:
            f2.write(Data)
            print("Content copied Succesfully into Demo.txt")  
    except FileNotFoundError:
        print("Source File Not Found")  


def main():
    if(len(sys.argv)!=2):
        print("Invalid arguments")
        return
    CopyFile(sys.argv[1])

if __name__ == "__main__":
    main()