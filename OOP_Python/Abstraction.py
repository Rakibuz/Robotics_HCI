from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    @abstractmethod
    def area(self):
        #print("Shape has no area")
        pass
        #this method have no body other method will overwrite this and use this 

class Triangle(Shape):

    #As this class inherit Shape class it must use area or abstract method otherwise error will be shown
    def area(self):
        area=0.5* self.dim1*self.dim2
        print("Area of Triangle is :",area)

class Rectangle(Shape):
    def area(self):
        area=self.dim1*self.dim2
        print("Area of Rectangle is :",area)

# we can't create abstract class object
# s1= Shape(10,20)
# s1.area()

t1=Triangle(20,30)
t1.area()

r1=Rectangle(20,30)
r1.area()