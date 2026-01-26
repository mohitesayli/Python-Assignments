import threading

def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def prime(numbers):
    print("Prime numbers:")
    for i in numbers:
        if is_prime(i):
            print(i)

def nonprime(numbers):
    print("Non-prime numbers:")
    for i in numbers:
        if not is_prime(i):
            print(i)

def main():
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    t1 = threading.Thread(target=prime, args=(arr,))
    t2 = threading.Thread(target=nonprime, args=(arr,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
