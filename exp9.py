#method overloading

class A:
    def message(self):
        print("hello")
    def fun(self,x):
        print("x=",x)
    def fun(self,x,y=None):
        if y==None:
            print("x=",x)
        else:
            print("x=",x,"y=",y)
mc=A()
mc.message()
mc.fun(3)
mc.fun(3,4)



#operator overloading
class complex:
    def __init__(self,a,b):
          self.a=a
          self.b=b
    def display(self):
        print( "a=",a,"b=",b)
    def __add__(self,other):
        return self.a +other.a,self.b+other.b
    def __mul__(self,other):
        return self.a *other.a,self.b*other.b

    
ob1 =complex(1,2)
ob2 =complex(2,3)
ob3= ob1 +ob2
print(ob3)
ob4= ob1 *ob2
print(ob4)
