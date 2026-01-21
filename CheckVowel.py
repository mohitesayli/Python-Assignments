def CheckVowel(ch):
    if ch in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonant")

def main():
    ch = input("Enter Character : ")
    CheckVowel(ch)

if __name__ == "__main__":
    main()