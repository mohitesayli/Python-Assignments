from functools import reduce

Add = lambda A, B : A + B

def main():
    Data = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    Result = reduce(Add, Data)
    print("Addition is :", Result)

if __name__ == "__main__":
    main()
