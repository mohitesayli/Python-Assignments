Minimum = lambda A, B : A if A < B else B

def main():
    value1 = 0
    value2 = 0
    Ret = 0

    print("Enter First Number : ")
    value1 = int(input())

    print("Enter Second Number : ")
    value2 = int(input())

    Ret = Minimum(value1, value2)
    print("Minimum Number is :", Ret)

if __name__ == "__main__":
    main()
