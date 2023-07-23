# error handling
try:
    a=int(input("enter a no"))
    if a==0:
        raise ValueError()
    b=int(input("enter a no"))
    c=int(input("enter a no"))
    d=(a/(b-c))
    print("d=",d)
except ValueError:
    print("value error")
except:
    print("some other error")
    d=(a/b)
    print("d=",d)
else:
    print("prasad")
finally:
    print("finished")
#multithreading= multithreading enables us to run  multiple thread concurrently


import threading


def print_no():
    for i in range(10):
        print (i)
        
 
def print_letter():
    for letter in 'abcdefghijklmnop':
        print (letter)

if __name__ =='__main__':
    thread1 = threading.Thread(target=print_no)
    thread2 = threading.Thread(target=print_letter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    

        
