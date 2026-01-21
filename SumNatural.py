def SumNatural(N):
    Total = 0
    for i in range(1,N+1):
        Total = Total + i
    print(Total)


def main():
    N = int(input("Enter Number:"))
    SumNatural(N)

if __name__ == "__main__":
    main()