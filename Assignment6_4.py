import threading

def small(s):
    cnt = 0
    for c in s:
        if c.islower():
            cnt += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Small letters:", cnt)

def capital(s):
    cnt = 0
    for c in s:
        if c.isupper():
            cnt += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Capital letters:", cnt)

def digits(s):
    cnt = 0
    for c in s:
        if c.isdigit():
            cnt += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits:", cnt)

def main():
    s = "Marvellous123"

    t1 = threading.Thread(target=small, args=(s,), name="Small")
    t2 = threading.Thread(target=capital, args=(s,), name="Capital")
    t3 = threading.Thread(target=digits, args=(s,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
