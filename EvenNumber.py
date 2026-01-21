def EvenNumber(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")



def main():
    EvenNumber(10)

if __name__ == "__main__":
    main()