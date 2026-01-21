def CheckDivisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    CheckDivisible(15)


if __name__ =="__main__":
    main()