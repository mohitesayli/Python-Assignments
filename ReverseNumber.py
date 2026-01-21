def ReverseNumber(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print(rev)



def main():
    num = int(input("Enter Number : "))
    ReverseNumber(num)


if __name__ == "__main__":
    main()