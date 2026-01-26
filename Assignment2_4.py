def sum_of_factors(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total = total + i
    return total


def main():
    num = int(input("Enter number: "))
    print("Output:", sum_of_factors(num))


if __name__ == "__main__":
    main()
