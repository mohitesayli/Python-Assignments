def sum_of_digits(no):
    total = 0
    while no > 0:
        total = total + (no % 10)
        no = no // 10
    return total


def main():
    num = int(input("Enter number: "))
    result = sum_of_digits(num)
    print("Sum of digits:", result)


if __name__ == "__main__":
    main()
