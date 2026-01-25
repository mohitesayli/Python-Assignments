Cube = lambda No : No * No * No

def main():
    value = 0
    Ret = 0

    print("Enter Number : ")
    value = int(input())

    Ret = Cube(value)
    print("Cube is :", Ret)

if __name__ == "__main__":
    main()
