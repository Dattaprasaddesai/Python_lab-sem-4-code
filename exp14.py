from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        login_label.config(text="Login successful!")
    else:
        login_label.config(text="Login failed. Please try again.")

root = Tk()
root.title("Login Page")
root.geometry("1550x1500")
root.config(bg='red')

username_label = Label(root, text="Username:")
username_label.pack()

username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()

password_entry = Entry(root)
password_entry.pack()

login_button = Button(root, text="Login",width=15,height=15,bg="green",fg="pink", command=login)
login_button.pack()

login_label = Label(root, text="welcome")
login_label.pack()

root.mainloop()
