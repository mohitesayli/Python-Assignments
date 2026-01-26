import threading

def even_factor(no):
    s = 0
    print("Even Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            s += i
    print("Sum of Even Factors:", s)

def odd_factor(no):
    s = 0
    print("Odd Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            s += i
    print("Sum of Odd Factors:", s)

def main():
    no = int(input("Enter number: "))

    t1 = threading.Thread(target=even_factor, args=(no,))
    t2 = threading.Thread(target=odd_factor, args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
