def CountFrequency(FileName,word):
    try:
        count = 0
        with open(FileName,"r")as f:
            for line in f:
                count = count + line.count(word)
                return count
    except FileNotFoundError:
        print("File Not Found")
        return -1

def main():
    Name = input("Enter File Name :")
    word = input("Enter string to search : ")
    Result = CountFrequency(Name,word)
    if Result != -1:
        print(f"Frequency of '{word}'' is : ", Result)
        

if __name__ == "__main__":
    main()