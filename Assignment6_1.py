import threading

def even():
    for i in range(2, 21, 2):
        print("Even :", i)

def odd():
    for i in range(1, 20, 2):
        print("Odd :", i)

def main():
    t1 = threading.Thread(target=even)
    t2 = threading.Thread(target=odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
