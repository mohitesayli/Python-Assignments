Power = lambda no: no ** 2


def main():
    value = int(input("Enter number: "))
    ret = Power(value)
    print("Output:", ret)


if __name__ == "__main__":
    main()
