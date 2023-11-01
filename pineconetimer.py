import tkinter  as tk 
from tkinter import *
from webbrowser import *
from time import strftime

lastClickX = 0
lastClickY = 0

my_fonttime=('arial',60,'bold') # display size and style
my_fontdate=('arial',20,'bold') # display size and style

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))
    

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
#root.geometry("400x400+500+300")
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
root.configure(background='black')
root.title("PineconeTimer V1")
#img = PhotoImage(file='pineconetimer.ico')
#root.tk.call('wm', 'iconphoto', root._w, img)


def my_time(): 
    l1=tk.Label(root,font=my_fonttime,bg='black',fg='#0f0',anchor='n')
    l1.grid(row=0,column=0,padx=0,pady=0)
    time_string = strftime(' %H:%M:%S ')
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds

def my_date():
    l2=tk.Label(root,font=my_fontdate,bg='black',fg='#0f0',anchor='s')
    l2.grid(row=1,column=0,padx=0,pady=0)
    date_string = strftime(' %A %B %d %Y ')
    l2.config(text=date_string)
my_time()
my_date()
root.mainloop()