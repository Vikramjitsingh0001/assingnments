#Q1
l=[]                                       #create a list
a=input("enter the number")                #enter the number you want
l.append(a)                                #number added
a=input("enter the number")                #enter another number
l.append(a)                                #number added
a=input("enter the number")                #enter the number
l.append(a)                                #number added
print(l)                                   #print tne list

#Q2
c=["google","facebook","apple","whatsapp"]         #list c cotains this
l.append(c)                                        #add list c in list l
print(l)                                           #print the list l

#Q3
print(c.count("apple"))                            #print the number of time the apple appear in the list

#Q4
v=[7,6,5,4,3,2,1]                               #list v in any oder
v.sort()                                        #sort the list v in assendinding order
print(v)                                        #print the list v in assending order

#Q5
a=[5,4,3,2,1]                                    #list a in any order
b=[9,8,7,6]                                       #list b in any order
c=a+b                                             #add list a and list b
c.sort()                                          #sort the list c
print(c)                                          #print the sorted list

#Q6
x=[1,2,3,4,5]                                     #list x
x.append(7)                                       #append 7 in list x
print(x)                                          #print the list x
x.pop(3)                                           #pop 3 from the list
print(x)                                           #print the list x

