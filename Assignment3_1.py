def add_elements(data):
    total = 0
    for no in data:
        total = total + no
    return total


def main():
    size = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(size):
        arr.append(int(input()))

    result = add_elements(arr)
    print("Addition is:", result)


if __name__ == "__main__":
    main()
