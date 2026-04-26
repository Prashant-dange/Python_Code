import tkinter

root_window=tkinter.Tk()
root_window.title("Grid expriment")

B1=tkinter.Button(root_window, text='ok')
B2=tkinter.Button(root_window,text='cancel')
B3=tkinter.Button(root_window,text='retry')

B1.grid(row=1,column=1,sticky=(tkinter.E,tkinter.W))
B2.grid(row=2,column=1,sticky=(tkinter.E,tkinter.W))
B3.grid(row=3,column=1,sticky=(tkinter.E,tkinter.W))


root_window.mainloop()