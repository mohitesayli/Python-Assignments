def SearchWord(FileName, Word):
    with open(FileName, "r") as f:
        for line in f:
            if Word in line:
                return True
    return False

def main():
    Name = input("Enter file name: ")
    Word = input("Enter word to search: ")

    Result = SearchWord(Name, Word)

    if Result:
        print("The word", Word, "is found in", Name)
    else:
        print("The word", Word, "is not found in", Name)

if __name__ == "__main__":
    main()
