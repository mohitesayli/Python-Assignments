def Check(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    print("Enter number : ")
    value = int(input())
    Check(value)

if __name__ == "__main__":
    main()
