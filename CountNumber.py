def CountDigit(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num//10
    print(count)


def main():
    num = int(input("Enter Number : "))
    CountDigit(num)

if __name__ == "__main__":
    main()