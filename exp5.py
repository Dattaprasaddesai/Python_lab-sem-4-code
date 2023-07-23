#demonstration of string

s="i i love my india"
print(s)

print("uppercase",s.upper())
print("lowercase",s.lower())
print("split only",s.split())
print("count i=",s.count("i"))
print("replace my with hi",s.replace("my",",hi"))


r="ratnagiri"
for ch in r:
    print(ch)

#demonstration of array
from array import array

a=array('i',[5,2,4,5,6,7,8,9])
print(a)
print(a.count(7))
a.reverse()
print(a)

print(a.index(5))
print(len(a))
a.pop(0)
print(a)
print("to bytes",a.tobytes())


#demonstration of set
s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print("intersection" ,s1&s2)
print("union" ,s1|s2)
print("set difference" ,s1-s2)
print("set symmetric difference" ,s1^s2)
print(type(s1))
print(len(s1))
s1.add(12)
print(s1)
s1.discard(12)
print(s1)
      




    
