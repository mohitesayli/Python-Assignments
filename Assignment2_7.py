def print_pattern(no):
    for i in range(no):
        for j in range(1, no + 1):
            print(j, end=" ")
        print()


def main():
    num = int(input("Enter number: "))
    print_pattern(num)


if __name__ == "__main__":
    main()
