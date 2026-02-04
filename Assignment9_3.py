def DisplayFile(FileName):
    with open(FileName,"r") as f:
        for line in f:
            print(line.strip())

def main():
    Name = input("Enter File Name: ")
    DisplayFile(Name)


if __name__ == "__main__":
    main()