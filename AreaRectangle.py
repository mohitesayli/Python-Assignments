def AreaRect(length,width):
    area = length * width
    print("Area of rectangle is : ",area)


def main():
    length = float(input("Enter length : "))
    width = float(input("Enter width : "))
    AreaRect(length,width)

if __name__ == "__main__":
    main()