# Q1  to find the area of cicle using function
a = 3.14                                                     #take vale of pi=3.14
r = int(input("enter the radius of circle"))                 #take value of radius from user
def area(a, r):                                              #create a function of area
    return a * r * r                                         #take area=pi*r*r
print(area(a, r))                                            #print the area calculated

# Q2 print all the perfect numbers between 1 and 1000
i = 0
n = int(input("enter the range"))                           #take input range from user to find its perfect number
def perfect(n):                                             #create the function for peerfect number
    sum = 0                                                 #intialize sum=0
    for i in range(1, n):                                   #apply for loop
        if (n % i == 0):                                    #check the number for perfect
            sum = sum + i                                   #if true then add the sum and i
    if (sum == n):                                          #check weather the sum is equal to n
        print("true is a perfect number")                   #print true
    else:                                                   #check for another case
        print("false is not a perfect number")              #print false
print(perfect(n))                                           #print the perfect function



#Q3 print the table of number using recusion
def num_table(n, t=1):                                     #create the fuction num_table
    if t == 11:                                            #check for t ==11
        return                                             #if t==11 the return stop the recurssion
    print(str(n) + "x" + str(t) + "=" + str(n * t))        #print the table eg 2X1=2 2X2=4
    num_table(n, t + 1)                                    #incrinment the t by t=t+1
num_table(12)                                              #take the number from user to find its table


#Q4 program to find the power of a number using recursion

u=int(input("enterr the number"))                          #take input from user
h=int(input("enter the other number"))                     #take another from user to find power function
def power(u,h):                                            #create the power function
    if(h==1):                                              #check for h=1
        return u                                           #then print the number as it is eg 4
    else:                                                  #check if h!=1
        return (u*power(u,h-1))                            #then u*power
print(power(h,u))                                          #print the function


#Q5 program to find the factorial of a number and store the factorial in the dictionary
g=int(input("enter the number to get its factorial"))     #take input from user
def fact(g):                                              #create the function fact
    if g==0:                                              #check if input is 0 or not
        return 1                                          #take 1
    s=g * fact(g-1)                                       #apply formula to calculate fact
    return s                                              #and return s=fact
b=fact(g)                                                 #let fact=b
d={g:b}                                                   #now put both input and fact (b) in dictinary d
print(d)                                                  #print the dictinary 
