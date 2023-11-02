#Imports
import tkinter  as tk 
from tkinter import *
from webbrowser import *
from time import strftime

showtime = 1
showdate = 1

#Font details
my_fonttime=('arial',40,'bold')
my_fontdate=('arial',15,'bold')
timecolor = '#0f0'
datecolor = '#0f0'

#These manage window movement
lastClickX = 0
lastClickY = 0
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))
    
#Setup for the window ans text
root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
root.configure(background='black')
root.title("PineconeTimerV1.5")
timelabel=Label(root,font=my_fonttime,bg='black',fg=timecolor,anchor='n')
datelabel=Label(root,font=my_fontdate,bg='black',fg=datecolor,anchor='s')
        
#Time and Date logic
def timeHandler(): 
    timelabel.grid(row=0,column=0,padx=0,pady=0)
    time_string = strftime(' %H:%M:%S ')
    timelabel.config(text=time_string) 
    timelabel.after(1000, timeHandler) # time delay of 1000 milliseconds
def dateHandler():
    datelabel.grid(row=1,column=0,padx=0,pady=0)
    date_string = strftime(' %A, %B %d, %Y ')
    datelabel.config(text=date_string)
    datelabel.after(10000, dateHandler)
#Right click menu
m = Menu(root, tearoff=0)
#m.add_checkbutton(label='Toggle Time', onvalue=0, offvalue=1)
#m.add_checkbutton(label='Toggle Date', onvalue=0, offvalue=1)
m.add_command(label="Exit", command=root.destroy)


def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
root.bind("<Button-3>", do_popup) 


#runs the code
timeHandler()
dateHandler()
root.mainloop()