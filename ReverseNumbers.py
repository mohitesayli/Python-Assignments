def  ReverseNumber(num):
    for i in range(num, 0, -1):
        print(i, end=" ")


def main():
    num = int(input("Enter Number : "))
    ReverseNumber(num)

if __name__ == "__main__":
    main()