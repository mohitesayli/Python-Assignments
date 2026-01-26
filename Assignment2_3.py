def factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    return fact


def main():
    num = int(input("Enter number: "))
    print("Output:", factorial(num))


if __name__ == "__main__":
    main()
