from tkinter import *
from tkinter import ttk
import sys

G = (6.67)* (10**-11)

def compute_btn_handler():
    m1 = float(mass1.get())
    m2 = float(mass2.get())
    r  = float(distance.get())
    F = (G * m1 * m2)/(r*r)
    val_strv.set(str(F))

def task_exit_btn():
    sys.exit(0)

def task_clear_btn():
    mass1.set('')
    mass2.set('')
    distance.set('')
    val_strv.set('')

root_window= Tk()
root_window.title("Compute gravitational")

obj_1_lable= Label(root_window)
obj_1_lable.grid(row=0 , column=0,sticky=W,padx=10,pady=5)
obj_1_lable.configure(text="Enter a mass of object 1 :")

mass1=StringVar()
obj_1_input=Entry(root_window)
obj_1_input.configure(textvariable=mass1 )
obj_1_input.grid(row=0,column=1,padx=10,pady=5)

obj_2_lable= Label(root_window)
obj_2_lable.grid(row=1 , column=0,sticky=W,padx=10,pady=5)
obj_2_lable.configure(text="Enter a mass of object 2 :")

mass2=StringVar()
obj_2_input=Entry(root_window)
obj_2_input.configure(textvariable=mass2)
obj_2_input.grid(row=1,column=1,padx=10,pady=5)

distance_lable= Label(root_window)
distance_lable.grid(row=2 , column=0,sticky=W,padx=10,pady=5)
distance_lable.configure(text="Enter a Distance between two object :")

distance=StringVar()
distance_input=Entry(root_window)
distance_input.configure(textvariable=distance)
distance_input.grid(row=2,column=1,padx=10,pady=5)

compuet_btn = Button(root_window)
compuet_btn.grid(row=3,column=0,sticky=W,padx=10,pady=10)
compuet_btn.configure(text="compute",command=compute_btn_handler)

clear_btn = Button(root_window)
clear_btn.grid(row=3,column=1,sticky=W,padx=10,pady=10)
clear_btn.configure(text="Clear",command=task_clear_btn)

exit_btn = Button(root_window)
exit_btn.grid(row=3,column=2,sticky=W,padx=10,pady=10)
exit_btn.configure(text="Exit",command=task_exit_btn)

left_label=Label(root_window)
left_label.configure(text="the gravitational force of attraction is ( ")
left_label.grid(row=5,column=1)

left_label=Label(root_window)
left_label.configure(text="the gravitational force of attraction is ( ")
left_label.grid(row=5,column=1)

right_label=Label(root_window)
right_label.configure(text=") Newton")
right_label.grid(row=5,column=3)

val_strv=StringVar()
val_label=Label(root_window)
val_label.configure(textvariable=val_strv)
val_label.grid(row=5,column=2)

root_window.mainloop()