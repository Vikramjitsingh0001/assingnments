#Q1name the Exception occured

#ZeroDivisionError                                     #output type of Errror in the question
try:                                                   #apply try statement
    a=int(input("enter the a"))                        #take input from user

    if a<4:                                            #check the input for given condition by if statement
        a=a/(a-3)                                      #check for a by formula
        print(a)                                       #print the answer as output

except ZeroDivisionError:                              #except block for error check like ZeroDivissionError
    print(("divided by zero"))                         #print the answer as output


#Q2
#IndexError                                            #output type of error in the question

try:                                                   #apply try statement
    l=[1,2,3,4]                                        #take a list l =1,2,3,4
    print(l[5])                                        #print the answer as output

except IndexError:                                     #except block for error check like IndexError
    print("index not in the list")                     #print the answer as output

try:                                                   #apply try statement
    k=[1,2,3,4]                                        #take a list k = 1,2,3,4
    print(k[2])                                        #print the answer as output

except IndexError:                                     #except block for error check like IndexError
    print("index not in the list")                     #print the answer as output


#Q3
#An exception                                          #output An exception print in the question

#Q4

#(a) -5                                                #output -5 print
#(b) a/b result is 0                                   #output print


#Q5

#(a)
try:                                                   #apply try statement
    import math                                        #import funtion to import the function present in the libary
except ImportError:                                    #except block for error check like ImportError
   print("file not found")                            #print the answer as output

try:                                                   #apply try statement
    import vikram                                      #import funtion to import the function present in the libary
except ImportError:                                    #except block for error check like ImportError
    print("file not found")                            #print the answer as output


#(b)
try:                                                   #apply try statement
    a=int(input("enter no"))                           #take input from user
    print(a)                                           #print the answer as output

except ValueError:                                     #except block for error check like ValueError
    print("please enter only integer")                 #print the answer as output



#(c)
try:                                                   #apply try statement
    l=[1,2,3,4]                                        #take a list l =  1,2,3,4
    print(l[5])                                        #print the 5th element in the list
except IndexError:                                     #except block for error check like IndexError
    print("index not in the list")                     #print the answer as output

try:                                                   #apply try statement
    l=[1,2,3,4]                                        #take a list l=1,2,3,4
    print(l[2])                                        #print the answer as output
except IndexError:                                     #except block for error check like IndexError
    print("index not in the list")                     #print the answer as output

#Q6
class AgesmallError(Exception):                        #create a class
    pass                                               #pass
a=True                                                 #take a==true

while(a):                                              #apply while loop
    try:                                               #apply try statement
        age=int(input("enter the age"))                #take input from user
    if(age>17):                                        #check the input for given condition by if statement
        raise AgesmallError(Exception)                 #raise the exception
    else:                                              #check for other case by else ststement
        print("age is :",age)                          #print the answer as output

    except AgesmallError:                              #except block for error check like AgeError
        print("Age is greater than 18")                #print the answer as output

    except ValueError:                                #except block for error check like ValueError
        print("enter a integer value")                #print 

