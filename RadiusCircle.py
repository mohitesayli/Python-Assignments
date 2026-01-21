def AreaCircle(radius):
    area = 3.14 * radius * radius
    print("Area of Circle is : ",area)

def main():
   radius = float(input("Enter Radius : "))
   AreaCircle(radius)

if __name__ == "__main__":
    main()