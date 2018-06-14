#Q1 what is time tupil
print("There is a popular time module available in python which provides function for working with time,and for converting"
      " between representations ,the function (time.time()) returns the current system time in ticks since 12 am,january 1,1970(epoch)"

      "Index   Attribute   values"
      "o       tm_year     2018"
      "1       tm_mon      1-12"
      "2       tm_mday     1-31"
      "3       tm_hour     0 to 23"
      "4       tm_min      0 to 59"
      "5       tm_sec      0 to 61(60 or 61 are leap-seconds"
      "6       tm_wday     0 to 6"
      "7       tm_yday     1 to 366"
      "8       tm_isdst    -1,0,1 where -1 means library determines DST")




#Q2 program to get formatted time
import time                                     #import time function from libary
print(time.asctime())                           #print the formatted time


#Q3 take month from the time
import datetime                                #import datetime function from libary
a='1998-4-27'                                  #take the date (day/month/year)
d=datetime.datetime.strptime(a,"%Y-%m-%d")     #create the dictionary d and put the a and day month and year variables in it
print(d.month)                                 #print the month from the time

#Q4 take day from the time
import datetime                               #import the datetime function from the libary
b='1997-2-25'                                 #take the date (day/month/year)
h=datetime.datetime.strptime(b,"%Y-%m-%d")    #create the dictionary h and put enteries in it
print(h.day)                                  #print the day from the time

#Q5 take date from the time

import datetime                              #import the datetime function from libary
c='12/12/2012'                               #take enter of date
f=datetime.datetime.strptime(c,"%d/%m/%Y")   #create the dictinary
print(f.day)                                 #print the day

#Q6 print the time using localtime method

import time                                 #import the time from libary
print(time.asctime())                       #print time as asctime
print(time.localtime())                     #print the time in local time

#Q7 find factorial of a number using math package functions
import math                                             #import the time function lib
o=int(input("enter the numberto find its factorial"))   #take input from user
print(math.factorial(o))                                #print the factorial of number

#Q8 find the GCD of number using math function

import math                                             #import the math function from lib
x=int(input("enter the 1st number"))                    #take input from user
y=int(input("enter the 2nd number"))                    #take second input from user
print(math.gcd(x,y))                                    #print the GCD

#Q9
#(a) get current working directory using os function
import os                                              #import the os function from lib
print(os.getcwd())                                     #print the current working directory

#(b) get the user environment using os function
import os                                             #import the os function from lib
print(os.environ)                                     #print the user environment
