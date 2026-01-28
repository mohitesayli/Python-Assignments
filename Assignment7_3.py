class Arithmetic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter First number :"))
        self.Value2 = int(input("Enter Second number :"))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        else:
            return self.Value1 / self.Value2

def main():
    Obj1 = Arithmetic()
    Obj1.Accept()
    print("Addition:", Obj1.Addition())
    print("Substraction:", Obj1.Substraction())
    print("Multiplication:", Obj1.Multiplication())
    print("Division:", Obj1.Division())

    print("----------------------")

    Obj2 = Arithmetic()
    Obj2.Accept()
    print("Addition:", Obj2.Addition())
    print("Substraction:", Obj2.Substraction())
    print("Multiplication:", Obj2.Multiplication())
    print("Division:", Obj2.Division())


if __name__ == "__main__":
    main()