def PrintNumber(n):
    for i in range(1, n + 1):
        print(i, end = " ")

def main():
    n = int(input("Enter Number : "))
    PrintNumber(n)

if __name__ == "__main__":
    main()