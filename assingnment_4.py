#Q1
a=(1,2,3,4,5,'car','bike')       #take tupil which contains different types of data type
print(len(a))                     #print the lenth of tupil eg number of varriable

#Q2
v=(1,5,3,7,33,9)         #take a tupil which contain n number
print(max(v))            #from n numbers find the largest one from tupil and print the larest one
print(min(v))            #from n numbers find the smallest one from tupil and print the smallest one


#Q3
t=(1*2*3*4)              #take a tupil and multipe it
print(t)                 #print the  product of elementspresent in tupil

#Q4(a)
s1=set((1,2,3,4,5,6,7))    #take a set s1
s2=set((1,3,6))            #take a set s2
s3=s1-s2                   #cmp s1 and s2 to have set s3
print(s3)                  #print s3 set

#(b)
a1=set((1,2,3,4,5,6,7,8))         #take set a1
a2=set((2,4,5,7))                 #take set a2
a3=a1>=a2                         #if a1>=a2 then a1 is a super set of a2
print("a1 is super set of a2")     #print
print(a3)                          #print the set a3
a4=a1<=a2                          #if a1<=a2 the a1 is a1 issub set of a2
print("a1 is a subset of a2 ")     #print
print(a4)                          #print set a4

#(c)
b1=set((1,2,3,4,5,6,7))            #take a set b1
b2=set((2,4,7,9))                  #take set b2
b3=b1&b2                           #take intersetion of two sets
print(b3)                          #print the interrsetion set
print("this is the intersection set")  #print
b4=b1|b2                             #take union of two sets
print(b4)                             #print the union of set
print("this is the unoin set")         #print

#Q5
a=input("enter the name")             #enter the name you want
b=input("enter marks")                #enter the marks
d={'name':'a','marks':'b'}             #make a dicitionary d
print(d)                                 #print the dictionary
#Q6


#Q7
l=('mississippi')                 #take a tupil which contains a sting in which  there is a repeation of same letters
check_for_m=l.count('m')            #count the number of m
check_for_i=l.count('i')            #count the number of i
check_for_s=l.count('s')             #count the number of s
check_for_p=l.count('p')             #count the number of p
d={'number of m':check_for_m,'number of i':check_for_i,'number of s':check_for_s,'number of p':check_for_p}
print(d)                          #print the dictionary d
