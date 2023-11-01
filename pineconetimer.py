#Imports
import tkinter  as tk 
from tkinter import *
from webbrowser import *
from time import strftime

#Font details
my_fonttime=('arial',40,'bold')
my_fontdate=('arial',15,'bold')

#This manages window movement
lastClickX = 0
lastClickY = 0
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))
    
#Setup for the window
root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
root.configure(background='black')
root.title("PineconeTimerV1.4")

#Time and Date logic
def my_time(): 
    l1=tk.Label(root,font=my_fonttime,bg='black',fg='#0f0',anchor='n')
    l1.grid(row=0,column=0,padx=0,pady=0)
    time_string = strftime(' %H:%M:%S ')
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds

def my_date():
    l2=tk.Label(root,font=my_fontdate,bg='black',fg='#0f0',anchor='s')
    l2.grid(row=1,column=0,padx=0,pady=0)
    date_string = strftime(' %A, %B %d, %Y ')
    l2.config(text=date_string)
    
#Right click menu
m = Menu(root, tearoff=0)
m.add_command(label="Exit", command=root.destroy)
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
root.bind("<Button-3>", do_popup) 


#runs the code
my_time()
my_date()
root.mainloop()