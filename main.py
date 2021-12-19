from tkinter import *
import pyqrcode

win = Tk()
win.title("Search Bar")

def search():
    link = entry.get()
    pyqrcode.create(link).svg('qrcode.svg',scale=10)

label1 = Label(win,text="Enter URL here:",font=("arial",10,"bold"))
label1.grid(row=0,column=0)

entry = Entry(win,width=30)
entry.grid(row=0,column=1)

button = Button(win,text="Search",command=search)
button.grid(row=1,column=0,columnspan=2,pady=10)

win.mainloop()
