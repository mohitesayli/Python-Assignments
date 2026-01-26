import threading

def forward():
    for i in range(1, 51):
        print(i)

def reverse():
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = threading.Thread(target=forward)
    t2 = threading.Thread(target=reverse)

    t1.start()
    t1.join()   # Thread2 starts after Thread1

    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
