from functools import reduce

Min = lambda A, B : A if A < B else B

def main():
    Data = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    Result = reduce(Min, Data)
    print("Minimum number is :", Result)

if __name__ == "__main__":
    main()
