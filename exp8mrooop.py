#MRO

class A:
    def rk(self):
        print("in class a")
class B(A):
    def rk(self):
        print("in class b")
class C(A):
    def rk(self):
        print("in class c")
class D(C,A):
    pass
r=D()
r.rk()

#inheritance & method overriding
class RECT:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def display(self):
        print("length=",self.length,"width=",self.width)
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def fun(self):
        print("hii prasad:")
print("ractangle details")
door=RECT(3,4)
door.display()
print("area=",door.area())
print("perimeter=",door.perimeter())
door.fun()

class BOX(RECT):
    def __init__(self,l,w,h):
        self.height=h
        super().__init__(l,w)
    def volume(self):
         return super().area()*self.height

print("box details")
bo=BOX(1,3,4)
bo.display()
print("volume=",bo.volume())
bo.fun()
print("perimeter=",bo.perimeter())
    
    



