CheckDiv5 = lambda No : (No % 5 == 0)

def main():
    value = 0
    Ret = False

    print("Enter Number : ")
    value = int(input())

    Ret = CheckDiv5(value)
    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")

if __name__ == "__main__":
    main()
