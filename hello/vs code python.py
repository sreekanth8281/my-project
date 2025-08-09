from tkinter import *


def on_circle_click(event):
    print("Circle button clicked!")
    
canvas = Canvas(root,width=200,height=100,bg="white")
canvas.pack()
circle=canvas.create_oval(30,30,140,90,fill="blue")



root = Tk()
root.config(bg="sky blue")
root.title("calculator")
entry = Entry(root,width=20,justify="right",font=("Arial",18))
entry.pack(fill=X,padx=20,pady=20,ipadx=30,ipady=10)

btn_frame = Frame(root)
btn_frame.pack()



button_labels = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "C","0","=","/"
]

i = 0
for label in button_labels:
    button = Button(btn_frame,text=label,font=("Arial",20),padx=20,pady=20,bg="pink")
    button.grid(row = i//4,column = i%4)
    canvas.tag_bind(circle, "<Button-1>", on_circle_click)
    i+=1


root.mainloop()