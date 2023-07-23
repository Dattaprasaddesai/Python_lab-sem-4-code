#program to demonstrate list ,tuple,dictonary

# a simple list
list1=[1,2,"python","program",15.9]
list2=["prasad","sahil","anahy"]

#printing the list
print(list1)
print(list2)
print(list1[2])
print(list2[1])
print(len(list2))


#copying the list
list1=[1,2,"python","program",15.9]
list3=list1.copy()
print(list3)
list3[3]=45
print(list3)

#repetition of list
list1=[1,2,"python","program",15.9]
#repetition operator
l=list1*2
print(l)

#concatenation of two list
list1=[1,2,"python","program",15.9]
list2=["prasad","sahil","anahy"]
#concatenation operator +
list3=list1 + list2
print(list3)

#append
list4=[12,11,10,3,4]
list4.append(100)
print(list4)
#sort
list4.sort()
#list allow duplicate values

#list constructor
thislist=list4=[12,11,10,3,4]
print(thislist)

#type()
mylist=["apple","banana ","orange"]
print(type(mylist))


#tuple
mylist=("apple","banana ","orange")
print(mylist)
print(type(mylist))
print(len(mylist))
print(mylist[1])
print(mylist[-1])


x=("11","12","13")
y=list(x)
y[1]="14"
x=tuple(y)
print(x)


#dictionaries
thisdict={ "brand":"zara",
           "model":"VK",
           "year":"2023"}
x=thisdict["model"]
print(x)
print(thisdict)
del thisdict
print(thisdict)# these cause error beacause this dict no longer exists

