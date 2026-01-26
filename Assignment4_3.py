from functools import reduce


def main():
    Data = []
    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        Data.append(int(input()))

    print("Input List =", Data)

    FData = list(filter(lambda no: no >= 70 and no <= 90, Data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no + 10, FData))
    print("List after map =", MData)

    RData = reduce(lambda a, b: a * b, MData)
    print("Output of reduce =", RData)


if __name__ == "__main__":
    main()
