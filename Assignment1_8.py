def print_stars(no):
    for i in range(no):
        print("*", end=" ")


def main():
    num = int(input("Enter number: "))
    print_stars(num)


if __name__ == "__main__":
    main()
