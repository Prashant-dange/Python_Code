from tkinter import *
from tkinter import ttk



LS=['core','Programming','academy']
i=-1

def change_text():
    global i
    i=i+1 
    if i == len(LS):
        i=0
    m.set(LS[i])


root_window=Tk()
root_window.title("String var Demo")
m=StringVar()
m.set('Start')

B= Button(root_window)

B.configure(text='change',command=change_text)

B.grid(row=0,column=0)


L = Label(root_window)
L.configure(textvariable=m)

L.grid(row=0,column=1)



root_window.mainloop()