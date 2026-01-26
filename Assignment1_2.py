def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter number : ")
    value = int(input())
    ChkNum(value)

if __name__ == "__main__":
    main()
