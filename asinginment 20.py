#project on pandas

import pandas as pd
#Question-1
#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

data={'Name':['Vikramjit singh','harpinder'],'Age':[20,41],'E-mail':['vikramjitsinghkarwal@gmail.com','harpindersinghkarwal@gmail.com'],'Phone-No.':[9855374004,9855374008]}
df=pd.DataFrame(data)
print(df)
print('\n')

#Question-2
data1=pd.read_csv("test9.csv")
df1=pd.DataFrame(data1)
#(a) First 5 rows of Dataframe

print("First five rows are..")
print(df1.head(5))
print('\n')

#(b) First 10 rows of the Dataframe

print("First ten rows are....")
print(df1.head(10))
print('\n')

#(c) find basic statistics on the particular dataset.

print("Basic Statistics on particular dataset are..")
print(df1.dtypes)
print(df1.size)
print(df1.axes)
print(df1.shape)
print(df1.ndim)
print('\n')

#(d) Find the last 5 rows of the dataframe

print("Last five rows are")
print(df1.tail(5))
print('\n')

#(e) Extract the 2nd column and find basic statistics on it

a=df1.iloc[:,1]
print("Basic Statistics of Second Column are..")
print(a.dtype)
print(a.size)
print(a.axes)
print(a.shape)
print(a.ndim)