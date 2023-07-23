try:
    a=int(input("enter a no a"))
    if a==0:
        raise ValueError()
    b=int(input("enter a no b"))
    c=int(input("enter a no c"))
    d=(a/(b-c))
    print("d=",d)
except ValueError:
    print("value error")
except :
    print("some other error")
    d=(a/b)
    print("d=",d)
else:
    print("prasad")
finally:
    print("finished")
    
    
