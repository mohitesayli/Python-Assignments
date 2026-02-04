def CountLines(FileName):
    Count = 0
    with open(FileName, "r") as f:
        for line in f:
            Count = Count + 1
    return Count

def main():
    Name = input("Enter file name: ")
    Result = CountLines(Name)
    print("Total number of lines in", Name, "are:", Result)

if __name__ == "__main__":
    main()
