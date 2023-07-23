from tkinter import *

def login():
    username= username_entry.get();
    password= password_entry.get();

    if username =="admin" and password == "prasad":
        login_label.config(text="login successful")
    else:
        login_label.config(text="login unsuccessful")

root = Tk()
root.title("login page")
root.geometry("1500x1500")
root.config(bg="yellow")

username_label=Label(root,text="username:")
username_label.pack()

username_entry=Entry(root)
username_entry.pack()
    

password_label=Label(root,text="password:")
password_label.pack()

password_entry=Entry(root)
password_entry.pack()

login_button= Button(root,text="login:",command=login)
login_button.pack()

login_label= Label(root,text=" welcome")
login_label.pack()
    
root.mainloop()
