class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*self.length+self.breadth
l1=int(input("enter length : "))
b1=int(input("enter breadth : "))
l2=int(input("enter length2: "))
b2=int(input("enter breadth2 : "))
r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
r1.area()
r2.area()
if r1.area()>r2.area():
    print ("r1 is greater")
else:
    print("r2 is greater")
