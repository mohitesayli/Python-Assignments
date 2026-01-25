CheckDiv = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Data = []
    Result = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    Result = list(filter(CheckDiv, Data))
    print("Divisible by 3 and 5 :", Result)

if __name__ == "__main__":
    main()
