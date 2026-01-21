def MultTable(num):
    for i in range(1,11):
        print(num * i,end = " ")
    

def main():
    num = int(input("Enter number:"))
    MultTable(num)
if __name__ == "__main__":
    main()