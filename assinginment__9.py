#Q1
class Circle():                                #create class name ciercle
    def __init__(self,r):                      #define a function
        self.radius=r                          #take radius to r
    def area(self):                            #define another function
        return self.radius**2*3.14             #return the area by formula
    def circum(self):                          #define another function
        return 2*self.radius*3.14              #return the circum by formula

x=Circle(1)                                   #createobject x=circle and pass radius in it
print("area of circle:",x.area())             #print area
print("cirmun of circle:",x.circum())         #print circum

#Q2

class Student():                             #create a class name student
    def __init__(self,name,roll_number):     #define the varriables
        self.n=name                          #take n=name
        self.rn=roll_number                  #take rn=rollnumber
y=Student('vikramjit singh',57)              #y=object
print("name of student is:",y.n)             #print name
print("roll_number of student is:",y.rn)     #print roll number

#Q3

class Temperature():                         #create a class name temperature
    def __init__(self,celcius_temperature):  #define variables
        self.temp=celcius_temperature        #temp=celcius temp
    def frenheat(self):                      #function for farenheat
        return 9/5*self.temp+32              #formula for temp
    def celcius(self):                       #function for celcius temp
        return self.temp                     #return celcius
z=Temperature(37.5)                          #object =temepature
print("the frenheat temperature of celcius is:",z.frenheat())         #print farenheat temp
print("the celcius temperature of farenheat is:",z.celcius())         #print celcius temp

#Q4
#(a)

class Movie_Details():                                                   #create class movie_detail
    def __init__(self,movie_name,artist_name,year_of_relase,rating):     #def variables
        self.n=movie_name                                                #n= movie name
        self.an=artist_name                                              #an=artistname
        self.y=year_of_relase                                            #year
        self.r=rating                                                    #rating

    def __update__(self,movie_name,artist_name,year_of_relase,rating):   #function
        self.n = movie_name                                              #name
        self.an = artist_name                                            #artist
        self.y = year_of_relase                                          #year
        self.r = rating                                                  #rating

q=Movie_Details('singh is king','akshy',2016,5)                           #def variable
print("movie name is:",q.n)                                               #print name
print("artistname is:",q.an)                                              #print artistname
print("year of relase is:",q.y)                                           #print year
print("rating is :",q.r)                                                  #print rating
n=input("enter the movie name")                                           #input
an=input("entre the artist name")                                         #input
y=input("enter the year")                                                 #input
r=input("enter the rating")                                               #input
w=Movie_Details(movie_name,artist_name,year_of_relase,rating)             #update variable
w.__update__(movie_name,artist_name,year_of_relase,rating)
print(n)
print(an)
print(y)
print(r)

#Q5
class Expenditure():                                           #create a class expinditure
    def __init__(self,expenditure,saving,total_salary=0):      #def variable
        self.ex=expenditure                                    #denote ex
        self.s=saving                                          #denote s
        self.t=0                                               #denote t

    def display(self):                                         #def display
        print("total expenditure:",self.ex)                    #print ex
        print("total saving:",self.s)                          #print s
    def total_salary(self):                                    #def total_salary
        self.t=self.ex+self.s                                  #formula
    def display__salary(self):                                 #def display
        return self.t                                          #return
p=int(input("enter the expenditure"))                          #print ex
r=int(input("enter the saving"))                               #print s
i=Expenditure(p,r)                                            # call class
i.display()                                                    #display
i.total_salary()                                               #call total salary
print("total salary:",i.display__salary())                     #print total salary
