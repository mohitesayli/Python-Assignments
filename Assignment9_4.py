def CopyFile(Source, Destination):
    with open(Source, "r") as f1:
        Data = f1.read()

    with open(Destination, "w") as f2:
        f2.write(Data)

def main():
    Src = input("Enter source file name: ")
    Dest = input("Enter destination file name: ")
    CopyFile(Src, Dest)
    print("Contents of", Src, "copied into", Dest)

if __name__ == "__main__":
    main()
