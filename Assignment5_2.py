import threading

def maximum(numbers):
    print("Maximum element:", max(numbers))

def minimum(numbers):
    print("Minimum element:", min(numbers))

def main():
    arr = [10, 40, 20, 50, 30]

    t1 = threading.Thread(target=maximum, args=(arr,))
    t2 = threading.Thread(target=minimum, args=(arr,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
