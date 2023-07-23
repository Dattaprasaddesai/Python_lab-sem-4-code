from array import array
a=array('i',[10,20,30])
b=array('i',[10,20,30])
c=a+b
print(c)


import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print("a+b=",a+b)

print(a-b)
print(a*b)

print(a/b)


print(a%b)

print(a<b)

print(a>b)

print(np.sin(0))
print(np.cos(0))

print(np.cos(90))



a=np.matrix("3,4,5;6,7,8;9,10,11")
print(a)
b=np.matrix("3,4,5;6,7,8;9,10,11")
print(b)

print(a-b)
print(a+b)
print(a*b)

print(a/b)

print(a<b)



#function

def my_function():
    print("hello prasad")
my_function()






def fact(a):
    if a==0:
        return 1
    return a*fact(a-1)
print("factorial=",fact(5))



def area(a,b=None):
    if b==None:
        return a*a
    else:
        return a*b
print("area=",area(3))
print("area=",area(3,5))
    

def display(a,b,c,d):
    print("a=",a,"b=",b,"c=",c,"d=",d)
display(3,4,5,6)
