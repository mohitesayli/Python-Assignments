Square = lambda No : No * No

def main():
    Data = []
    Result = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    Result = list(map(Square, Data))

    print("Squares are : ", Result)

if __name__ == "__main__":
    main()
