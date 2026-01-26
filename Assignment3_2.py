def find_max(data):
    max_no = data[0]
    for no in data:
        if no > max_no:
            max_no = no
    return max_no


def main():
    size = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(size):
        arr.append(int(input()))

    result = find_max(arr)
    print("Maximum number is:", result)


if __name__ == "__main__":
    main()
