class BankAccount:
    
    ROI = 10.5   

   
    def __init__(self, Name, Amount):
        self.Name = Name        
        self.Amount = Amount    

    
    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Account Balance:", self.Amount)

   
    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print("Amount deposited successfully.")

    
    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal not allowed.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    Acc1 = BankAccount("Sayli", 10000)
    Acc1.Display()
    Acc1.Deposit()
    Acc1.Withdraw()
    print("Interest:", Acc1.CalculateInterest())
    Acc1.Display()

    print("------------------------")

    Acc2 = BankAccount("Amit", 5000)
    Acc2.Display()
    Acc2.Deposit()
    Acc2.Withdraw()
    print("Interest:", Acc2.CalculateInterest())
    Acc2.Display()


if __name__ == "__main__":
    main()
