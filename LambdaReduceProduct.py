from functools import reduce

Multiply = lambda A, B : A * B

def main():
    Data = []

    print("Enter number of elements : ")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    Result = reduce(Multiply, Data)
    print("Product is :", Result)

if __name__ == "__main__":
    main()
