#demonstration of for loop
for i in range(10):
    print(i)
    
for i in range(10,30,4):
    print(i)

    
print("\n***********************\n")


for i in range(10,1,-1):
    print(i)
    


for i in range(10,0,-1):
    if i==6:
        continue
    print(i)
else:
     print("happy")

#demonstration of while loop
i=1
while i<=6:
    print(i)
    i+=1
    
    
i=10
while i>=6:
    print(i)
    i-=1

    
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
print("\n*************\n")    
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)


#program to check prime no using for loop
num=int(input("enter a no:"))
if num>1: 
    for  i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        ("prime no")
    
