def primenumber(num):
    if num <= 1:
        print("Not Prime")
        return
    
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return
    print("Prime Number")


def main():
    num = int(input("Enter Number :"))
    primenumber(num)

if __name__ == "__main__":
    main()