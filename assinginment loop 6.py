
#Q1 To print 10 integers on screen given by user

i=0                                                   #intialize i=0
b=[]                                                  #take a empty list
while(i<10):                                          #apply while loop till i<10
   num=int(input("enter the num"))                    #tkae input from user a integer
   b.append(num)                                      #now put num (input) in the empty list b
   i=i+1                                              #increment i
for i in b:                                           #apply for loop in list b
    print(i)                                          #print the i in list b



#Q2infinite loop true

#while('true'):                                       #inlilize true
#   print('infinite')                                 #print loop infinite


#Q3create a list of integer and squre of it by theinput provided by user

b=[]                                                  #take a empty list b
sq=[]                                                 #take a list square empty
for i in range(0,5):                                  #apply for loop in the range of 0 to 5
    x=int(input("enter the num"))                     #take input from user
    b.append(x)                                       #put the input in list b
print(b)                                              #print the list  b

for x in b:                                           #apply the the for loopon list b
    k=x*x                                             #take square of x(input)
    sq.append(k)                                      #put the square in list sq
print(sq)                                             #print the square list


#Q4 make a list to store the different data types present in the list

i=0
l=[11,22,33,"vikram",3.4,4.6]                         #take list l containg differnt data types
m=[]                                                  #make a empty list m to store integers
e=[]                                                  #make a empty list e to store string
f=[]                                                  #make a empty list f to store float data type
for i in l:                                           #apply for loop

    if (type(i)==int):                                #check int data type in the list
        m.append(i)                                   #put the int data type in m list
    elif(type(i)==str):                               #ckeck the str data type in list
        e.append(i)                                   #put the str data type in list e
    else:                                             #check for float data type
        f.append(i)                                   #put the float data type in list f
print(m)                                              #print the int list
print(e)                                              #print the str list
print(f)                                              #print the float list


#Q5 make even and odd lists from the list
p=[]                                                  #take a empty even list
q=[]                                                  #take a empty odd list
for i in range(1,101):                                #apply for loop in range of 1to 101
    if(i%2==0):                                       #check for even number from list
        p.append(i)                                   #put the even number in the even list
    else:                                             #check for odd number
        q.append(i)                                   #put the odd numbe  in the odd list
print("even")                                         #print  even
print(p)                                              #print even list
print("odd")                                          #print odd
print(q)                                              #print the odd list




#Q6 print the pattern

r=4                                                  #inliae r upto 4
for i in range(0,r):                                 #apply for loop
    for s in range(0,i+1):                           #apply another for loop in  it
        print("$",end="")                            #print what you want to print in for loop
    print("\r")                                      #take next lined


#Q7 create a user defined dictionary andget keys corresponding to it
d={'name':'vikram','age':21,'roll no':57}           #take a dicitionary
for i in d:                                         #apply for loop on d
    print(i)                                        #print keys



#Q8 take a input from user to make a list and again take input from user and if it found in the list reove it
i=0
h=[]                                               #take aempty list
while(i<5):                                        #apply a while loop on it
    n=int(input("enter the number"))               #take input from user
    h.append(n)                                    #put the input in the list
    i=i+1                                          #increment
n=int(input("enter number to be searched"))        #take another input to find the data in the list
for i in h:                                        #apply for loop
    if(n==i):                                      #check the presence of input in the list
        h.remove(i)                                #remove the same input in the list
print(h)                                           #print the list afterremoval
