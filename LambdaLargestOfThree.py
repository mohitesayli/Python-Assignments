Maximum = lambda A, B, C : A if (A >= B and A >= C) else (B if B >= C else C)

def main():
    value1 = 0
    value2 = 0
    value3 = 0
    Ret = 0

    print("Enter First Number : ")
    value1 = int(input())

    print("Enter Second Number : ")
    value2 = int(input())

    print("Enter Third Number : ")
    value3 = int(input())

    Ret = Maximum(value1, value2, value3)
    print("Largest Number is :", Ret)

if __name__ == "__main__":
    main()
