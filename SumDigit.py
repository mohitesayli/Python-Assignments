def SumDigit(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    print(total)


def main():
    num = int(input("Enter Number : "))
    SumDigit(num)

if __name__ == "__main__":
    main()