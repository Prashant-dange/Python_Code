from tkinter import *
from tkinter import ttk

def show_entered_text():
    s=svE1.get()
    print("imput text is ",s)
    svL2.set(s)

def do_clear():
    svE1.set("")
    svL2.set("")

root_window=Tk()
root_window.title("Enter widget titile")
root_window.minsize(300,200)
root_window.maxsize(800,600)

L1= Label(root_window)
L1.configure(text="Enter something:")
L1.grid(row=0,column=0)

svE1 = StringVar ()
E1 = Entry(root_window)
E1.configure(textvariable=svE1)
E1.grid(row=0,column=1)

B1=Button(root_window)
B1.configure(text='Print',command=show_entered_text)
B1.grid(row=1,column=0)

B2=Button(root_window)
B2.configure(text='Clear',command=do_clear)
B2.grid(row=1,column=1)


svL2=StringVar()
L2=Label(root_window)
L2.configure(textvariable=svL2)
L2.grid(row=3,column=0)



root_window.mainloop()