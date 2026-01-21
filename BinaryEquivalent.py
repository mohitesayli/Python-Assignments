def Binary(num):
    Binary = bin(num)[2:]
    print("Binary Equivalent : ",Binary)


def main():
    num = int(input("Enter Number : "))
    Binary(num)

if __name__ == "__main__":
    main()