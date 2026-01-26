from functools import reduce


def CheckPrime(no):
    if no < 2:
        return False

    for i in range(2, int(no / 2) + 1):
        if no % i == 0:
            return False

    return True


def main():
    Data = []
    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        Data.append(int(input()))

    print("Input List =", Data)

    FData = list(filter(CheckPrime, Data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no * 2, FData))
    print("List after map =", MData)

    RData = reduce(lambda a, b: a if a > b else b, MData)
    print("Output of reduce =", RData)


if __name__ == "__main__":
    main()
