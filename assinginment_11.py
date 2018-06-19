
#Q1
import threading
import time
class Batman(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
        time.sleep(5)
    def run(self):
        print("Ek tha Tiger",self.h)

Thread=Batman(1)
Thread.start()
Thread=Batman(2)
Thread.start()

#Q2

import threading
import time
class Hulk(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("no is",self.h)

for i in range(10):
    time.sleep(1)
    Thread1=Hulk(i)
    Thread1.start()

print("active threads are",threading.active_count())

#Q3

import threading
import time
a=(2,4,6,8,10)
class Spiderman(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self,counter):
        time.sleep(counter)
        print(self.h)

for i in a:
    Thread=Spiderman(i)
    Thread.run(i)

#Q4

import threading
import time
import math
class Avenger(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        x=self.h
        y=math.factorial(x)
        print("factorial is :",y)
user=int(input("enter the number to find factorial"))
Thread=Avenger(user)
Thread.start()
