def frequency(data, target):
    count = 0
    for no in data:
        if no == target:
            count += 1
    return count


def main():
    size = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(size):
        arr.append(int(input()))

    search = int(input("Enter element to search: "))
    result = frequency(arr, search)

    print("Frequency is:", result)


if __name__ == "__main__":
    main()
