#Q1
class Animals:
    def animal_attribute(self):
        print("EK Tha Tiger")

class tiger(Animals):
    def back(self):
        print("tiger is back ,Tiger Zinda ha")
t=tiger()
t.animal_attribute()
t.back()

#Q2
#(a)A B
#(b)A B

#Q3
class Cop():
    def __init__(self,name,age,workexperience,desigination):
        self.n=name
        self.a=age
        self.w=workexperience
        self.d=desigination
    def display(self):
        print("before update")
        print("name",self.n)
        print("age:",self.a)
        print("workexperience:",self.w)
        print("desigination:",self.d)

class Mission(Cop):
    def add_mission_detail(self,name,age,workexperience,desigination):
        print("update cop details are")
        print("name=",end="")
        self.n=name
        print(name)
        print("age=",end="")
        self.a=age
        print(age)
        print("workexperience=",end="")
        self.w=workexperience
        print(workexperience)
        print("desigination=",end="")
        self.d=desigination
        print(desigination)
v=Mission("vikramjit Singh karwal",21,100,"Mallak(owner)")
name=input("enter the name")
age=input("enter the age")
workexperience=input("enter the workexperrience")
desigination=input("enter the desiginattion")
v.display()
v=Mission(name,age,workexperience,desigination)
v.add_mission_detail(name,age,workexperience,desigination)




#Q4

class Shape:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self,area):
        area=self.l*self.b
        print(area)

class Rectangle(Shape):

    def area(self):
        area=self.l*self.b
        print("area of rectangle:",area)

class Square(Shape):

    def area(self):
        area=self.l*self.b
        print("the area of square is:",area)

x=Rectangle(5,7)
y=Square(5,5)
x.area()
y.area()