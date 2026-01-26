def check_divisible_by_5(no):
    return no % 5 == 0


def main():
    num = int(input("Enter number: "))
    result = check_divisible_by_5(num)
    print("Output:", result)


if __name__ == "__main__":
    main()
