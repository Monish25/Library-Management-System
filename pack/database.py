from tkinter import *
a=Tk()
import os
def view():
    b = Tk()
    b.title('What DB')
    b.geometry('200x100')
    bt1= Button(b,text = 'Book  Register',width = 11, command =books )
    bt1.pack()
    bt2= Button(b,text = 'Borrowed',width = 11,command = bor)
    bt2.pack()
    bt3= Button(b,text = 'Returned',width = 11,command = ret)
    bt3.pack()
    b.mainloop()
def bor():
    os.system('issue.xlsx')
def ret():
    os.system('issr.xlsx')
def books():
    os.system('database.xlsx')
def insert():
    os.system('insert.py')

a.title('Database')
a.geometry('200x100')
Head1= Label(text = "Database", font = ("Lucida Handwriting", 13))
Head1.pack()
but1=Button(a,text='Insert',command=insert,width = 4)
but1.pack()
but2=Button(a,text='view',command=view,width = 4)
but2.pack()
a.mainloop()