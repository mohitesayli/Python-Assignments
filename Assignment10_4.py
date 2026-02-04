import sys

def CompareFiles(File1, File2):
    try:
        with open(File1, "r") as f1, open(File2, "r") as f2:
            Data1 = f1.read().strip()
            Data2 = f2.read().strip()

            if Data1 == Data2:
                print("Success")
            else:
                print("Failure")

    except FileNotFoundError:
        print("One or both files not found")

def main():
    if len(sys.argv) != 3:
        print("Invalid arguments")
        return

    CompareFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
