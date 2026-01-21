def  CheckPalindrome(num):
    temp = num 
    rev  = 0
   
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    
    if temp == rev:
        print("Palindrome Number")
    else:
        print("Not Palindrome")


def main():
    num = int(input("Enter Number : "))
    CheckPalindrome(num)

if __name__ == "__main__":
    main()