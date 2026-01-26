def check_prime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False
    return True


def main():
    num = int(input("Enter number: "))

    if check_prime(num):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")


if __name__ == "__main__":
    main()
