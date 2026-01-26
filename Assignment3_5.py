import MarvellousNum


def ListPrime(data):
    total = 0

    for no in data:
        if MarvellousNum.ChkPrime(no):
            total = total + no

    return total


def main():
    size = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(size):
        arr.append(int(input()))

    result = ListPrime(arr)
    print("Addition of prime numbers is:", result)


if __name__ == "__main__":
    main()
