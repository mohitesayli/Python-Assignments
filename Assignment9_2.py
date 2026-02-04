def CountWords(FileName):
    Count = 0
    with open(FileName, "r") as f:
        for line in f:
            words = line.split()
            Count = Count + len(words)
    return Count

def main():
    Name = input("Enter file name: ")
    Result = CountWords(Name)
    print("Total number of words in", Name, "are:", Result)

if __name__ == "__main__":
    main()
