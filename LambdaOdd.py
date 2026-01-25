CheckEven = lambda No : (No % 2 != 0)

def main():
    value = 0
    Ret = False

    print("Enter Number : ")
    value = int(input())

    Ret = CheckEven(value)
    if Ret == True:
        print("True (Number is Even)")
    else:
        print("False (Number is Odd)")

if __name__ == "__main__":
    main()
