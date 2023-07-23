from tkinter import  *

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "prasad" and password == "1234":
        login_label.config(text="succesfull login")
    else:
        login_label.config(text="unsuccesfull login")

    

root=Tk()
root.title("login page")
root.geometry("1500x1500")
root.config(bg="green")

username_label=Label(root,text="username:")
username_label.pack()

username_entry=Entry(root)
username_entry.pack()

password_label=Label(root,text="password:")
password_label.pack()

password_entry=Entry(root)
password_entry.pack()

login_button=Button(root,text="login",fg="orange",bg="black",height=20,width=40,command=login)
login_button.pack()

login_label=Label(root,text="welcome",bg="orange",fg="black")
login_label.pack()


root.mainloop()
