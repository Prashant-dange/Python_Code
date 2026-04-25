#import package require for windowing
import tkinter

#create a main window by creating object of class TK
root_window=tkinter.Tk()

#set title of window
root_window.title('Tkinter-python')

#set minimum widht and height of window
root_window.minsize(200,150)

#set maximum width and height
root_window.maxsize(800,600)

#create a lable object
my_name = tkinter.Label(
                        root_window,text='Prashant Dange',
                        fg='green',font=('Time new Roman',12,'bold')
                        )

my_name.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
#enter a event loop
root_window.mainloop()
