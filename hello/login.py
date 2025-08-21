from tkinter import *

def open_new_win():
    new_win = Toplevel(root)
    new_win.config(bg="#d77ad9")
    new_win.title("welcome")
    new_win.geometry("300x300")

    label = Label(new_win,text="Logged in succesfully!",font=("Arial",12),bg="#d77ad9")
    label.grid()
    btn = Button(new_win,text="Exit",font=("Arial",12),bg="#8087e2",command=new_win.destroy)
    btn.grid()
    check = Checkbutton(new_win,text="Ok",font=("Arial",12),bg="#d77ad9")
    check.grid()



root = Tk()
root.config(bg="#8087e2")
root.title("Login Form")
root.geometry("350x450")


frame = Frame(root,bg="#8087e2")

label = Label(frame,text="Login",font=("Arial",12))
label.grid(row=0,column=2,columnspan=2,pady=20)
username_label = Label(frame,text="Username",font=("Arial",12),bg="#8087e2")
username_entry = Entry(frame)
password_label = Label(frame,text="Password",font=("Arial",12),bg="#8087e2")
password_entry = Entry(frame)
btn = Button(frame,text="Login",font=("Arial",12),bg="#7ad9b6",command=open_new_win)

username_label.grid(row=1,column=0,ipady=10)
username_entry.grid(row=1,column=1)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
btn.grid(row=3,column=1,columnspan=2)


frame.pack()
root.mainloop()