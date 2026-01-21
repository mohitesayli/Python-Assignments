def CheckPerfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    num = int(input("Enter Number : "))
    CheckPerfect(num)

if __name__ == "__main__":
    main()
