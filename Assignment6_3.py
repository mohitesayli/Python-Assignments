import threading

def even_list(arr):
    s = 0
    print("Even elements:")
    for i in arr:
        if i % 2 == 0:
            print(i)
            s += i
    print("Sum of even:", s)

def odd_list(arr):
    s = 0
    print("Odd elements:")
    for i in arr:
        if i % 2 != 0:
            print(i)
            s += i
    print("Sum of odd:", s)

def main():
    arr = [10, 15, 20, 25, 30]

    t1 = threading.Thread(target=even_list, args=(arr,))
    t2 = threading.Thread(target=odd_list, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
