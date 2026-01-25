CheckLength = lambda s : len(s) > 5

def main():
    Data = []
    Result = []

    print("Enter number of strings : ")
    size = int(input())

    print("Enter strings : ")
    for i in range(size):
        Data.append(input())

    Result = list(filter(CheckLength, Data))
    print("Strings with length > 5 :", Result)

if __name__ == "__main__":
    main()
