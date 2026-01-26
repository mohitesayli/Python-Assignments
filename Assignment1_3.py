def Add(No1, No2):
    return No1 + No2

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Result = Add(A, B)
    print("Addition is :", Result)

if __name__ == "__main__":
    main()
