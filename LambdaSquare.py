Square = lambda No : No * No

def main():
    value = 0
    Ret = 0

    print("Enter Number : ")
    value = int(input())

    Ret = Square(value)
    print("Square is :", Ret)

if __name__ == "__main__":
    main()
