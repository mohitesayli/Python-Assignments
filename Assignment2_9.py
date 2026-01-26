def count_digits(no):
    count = 0
    while no > 0:
        count += 1
        no = no // 10
    return count


def main():
    num = int(input("Enter number: "))
    result = count_digits(num)
    print("Number of digits:", result)


if __name__ == "__main__":
    main()
