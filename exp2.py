#demonstration of relational  operator
a=10
b=4
print("a=",a,"b=",b)

print("a!=b",a!=b)

print("a==b",a==b)

print("a>=b",a>=b)

print("a<=b",a<=b)

print("a<b",a<b)

print("a>b",a>b)

#demonstration of logical operator
a=10
b=4
print("a=",a,"b=",b)

print("a>b &b=4 is ",a>b and b==4)
print("a<b &b=4 is ",a<b and b==4)

print("a>b &b!=4 is ",a>b or b!=4)
print("a<b &b!=4 is ",a<b and b!=4)

print("a<b &b!=4 is ",a<b and b!=4)


print("not(a>b &b=4) is ",not(a>b and b==4))
print("not(a<b &b=4) is ",not(a<b and b==4))

#demonstration of membership operator
a=[1,2,3,45,6]
b=[7,77,777,7777]
print(a[1])
print(1 in a)
print(77 in a)
print(not(77 in a))
#demonstration of decision control statement

a=input("enter gender(m/f):")
b=int(input("enter age:"))
if((a=="M")or(a=="m") and (b>=21))or ((a=="F")or(a=="f") and (b>=18)):
    print("elligible for marriage")
else:
    print(" not elligible for marriage")

#program to demonstrate if-else statement

day=int(input("enter day in week:"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturdayday")
elif day==7:
    print("sunsday")
else:
    print("invalid day")
