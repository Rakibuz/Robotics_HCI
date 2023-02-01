class  A:
    def display(self):
        print("I am inside A class")

class  B:
    #display()
    def display(self):
        print("I am inside B class")

class  C(A,B):
    #display()
    #display()
    
    # def display(self):
    #     print("I am inside C class")
    pass


ob1 =C()
#ob1.display1()
#ob1.display2()
ob1.display()