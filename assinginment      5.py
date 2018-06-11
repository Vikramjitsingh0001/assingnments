#Q1 to check wheather the given year by a user is a leap year or not
x=int(input("enter the year"))     #enter the year
if(x%4==0):                        #if year divide by 4 equal to 0 then leap
    print("the year is a leap year")  #print


else:                                         #else loop for negtive result
    print("the year is not a leap year")        #print


#Q2 To check wheather the given dimenssion are of square or a rectange

a=int(input("enter the length"))        # enter the length
b=int(input("enter the breadth"))         #enter the breadth
if(a==b):                                 #check if they are equal or not
    print("the length and breadth are same so these are the dimenssions of square ")  #print square

else:                                     #check for negative result
    print("the length and breadth are not same so these are the dimenssions of rectangle")  #print rectangle

#Q3 find the oldest and youngest among 3 persons

u=int(input("enter the age of 1st person u"))    #enter the age of 1st person
v=int(input("enter the age of second person v"))   #enter the age of 2nd person
w=int(input("enter the age of 3rd person w"))       #enter the age of 3rd person
if(u>v and u>w):                                 #check the age
    print("u is oldest among all 3")            #print the oldest one

elif(v>u and v>w):                                 #ckeck  for negtive case
    print("v is oldest among all 3")          #print the oldest one


elif(w>u and w>v):                          #check age
    print("w is oldest among all 3")          #print the oldest one


if(u<v and u<w):                             #check for youngest u
    print("u is youngest among all 3")        #print the youngest one


elif(v<u and v<w):                          #check for yougest v
    print("v is youngest among all 3")      #print the youngest one


elif(w<u and w<v):                            #check for youngest w
    print("w is youngest among all 3")   #print the youngest one

else:                                      #check for same age
    print("all are of same age")            #print the result

#Q4t Tell the competitors weather they won the prize based on there points or not and if they won then which prize

p=int(input("enter the points they scorred "))         #enter the points you won
if(p>=1 and p<=50):                         #check for prize for the points
    print("no prize won")                    #print the prize

elif(p>=51 and p<=150):              #check for prize for the points
    print("you won a wooden dog in prize")  #print the prize

elif(p>=151 and p<=180):                #check for prize for the points
    print("you won a book in prize")        #print the prize

else:                               #check for prize for the points
    print("you won chocalates in prize")      #print the prize

#Q5 calculate the total cost of quantity after the discount of 10% on Rs1000 shopping

q=int(input("enter the the quantiy or number of products"))     #enter the number of products
price=q*100                                                      #total price for the products
if(price>1000):                                          #check for discount if q>10
    print(price-0.10*price)       #print the cost

else:                  #check for number of products if q>10 or not
    print(price)    #print the cost
