def find_min(data):
    min_no = data[0]
    for no in data:
        if no < min_no:
            min_no = no
    return min_no


def main():
    size = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(size):
        arr.append(int(input()))

    result = find_min(arr)
    print("Minimum number is:", result)


if __name__ == "__main__":
    main()
