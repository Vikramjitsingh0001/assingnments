'''
#Q1program to read last n lines of a file

f=open("text.tht",encoding="utf8")                           #this will open the text.thtfile and will read  the whole content in it
a=(f.readlines())                                            #will read line by line
a.reverse()                                                  #reverse function to reverse all content
n=int(input("enter the number of lines u want to display"))  #take a input of no of liine from user
for i in range(0,n):                                         #apply for loop on it
    print(a[i])                                              #print the content in reverse order
f.close()                                                    #close thebuffer use to store the data




#Q2program to count the frequency of words in a file

v="kill"                                                   #take a word from the file text2.tht to check repeating
f=open("text2.tht","r")                                    #open the file and read it
k=f.read()                                                 #will read only the repeating word
m=k.split()                                                #split it from entier
print(k.count(v))                                          #print the count of split word


#Q3program to copy the contents of a file to another file

f=open("text.tht",encoding="utf8")                        #open thetext.tht file
a=(f.readlines())                                         #read all the line form the file
o=open("text3.tht","w")                                   #open the file where to copy all
o.writelines(a)                                           #write all the data to be copied from file 1 to file 2

'''
#Q4program to combine each line from first file with the corresponding line in second file.

i=0                                                      #intilize the i=0
f=open("text3.tht","r")                                  #open the text3.thtfile
a=(f.readlines())                                        #read all the lines from it
b=open("text2.tht","r")                                  #open the text2.tht file
o=(b.readlines())                                        #read all the lines from it
d=open("text4.tht","w")                                  #open another file where to save alla the data from both the files
for i,j in zip(a,o):                                     #apply for loop
    d.write(i+j)                                         #write from both files
f.close()                                                #close the f buffer
b.close()                                                #close the b buffer
d.close()                                                #close the d bufffer

#Q5

