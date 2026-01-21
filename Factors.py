def Factors(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i, end = " ")


def main():
    num = int(input("Enter Number : "))
    Factors(num)

if __name__ == "__main__":
    main()