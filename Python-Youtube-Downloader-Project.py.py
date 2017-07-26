#Simple GUI
#Import the GUI package
from tkinter import *

#Create a window
master = Tk()

def Download():
    print("Just made the GUI window")
    
#Modify master window
b = Button(master, text="Download Video", command = Download)
b.place(relx=0.5, rely=0.5, anchor=CENTER)

#Kick off the event loop
mainloop()
