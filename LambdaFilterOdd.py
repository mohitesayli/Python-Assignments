CheckOdd = lambda No : (No % 2 != 0)

def main():
    Data = []
    Result = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    Result = list(filter(CheckOdd, Data))
    print("Odd numbers are :", Result)

if __name__ == "__main__":
    main()
