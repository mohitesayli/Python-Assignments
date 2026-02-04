def DisplayContents(FileName):
    try:
        with open(FileName,"r")as f:
            print("Contents of file")
            print(f.read())
    except FileNotFoundError:
        print("File Not Found")
        


def main():
    Name = input("Enter File Name : ")
    DisplayContents(Name)


if __name__ == "__main__":
    main()