class Demo:
    value = 0
    def __init__(self,a,b):
        self.No1 = a
        self.No2 = b
    

    def Fun(self):
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)
    

    def Gun(self):
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)
    
def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()