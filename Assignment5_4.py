import threading

def sum_elements(numbers):
    print("Sum of elements:", sum(numbers))

def product_elements(numbers):
    result = 1
    for i in numbers:
        result *= i
    print("Product of elements:", result)

def main():
    arr = [1, 2, 3, 4, 5]

    t1 = threading.Thread(target=sum_elements, args=(arr,))
    t2 = threading.Thread(target=product_elements, args=(arr,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()
