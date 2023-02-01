# Multi Level Inheritance
#                               A
#                               |
#                               |
#                               B
#                               |                         
#                               |
#                               C


# Multiple Inheritance

#                                A
#                               / \
#                              /   \
#                             /     \
#                            B       C
#                             \     /
#                              \   /
#                                D





class  A:
    def display1(self):
        print("I am inside A class")

class  B(A):
    #display1()
    def display2(self):
        print("I am inside B class")

class  C(B):
    #display1()
    #display2()
    
    def display3(self):
         #calling inherited class methods
        super().display1()
        super().display2()
        print("I am inside C class")


ob1 =C()
#ob1.display1()
#ob1.display2()
ob1.display3()