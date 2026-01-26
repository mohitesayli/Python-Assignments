Multiply = lambda a, b: a * b


def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    ret = Multiply(no1, no2)
    print("Output:", ret)


if __name__ == "__main__":
    main()
