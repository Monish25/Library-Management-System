from tkinter import *
import os
def issue():
    os.system('issue.py')   #function : Run the file 'issue'

def ret():
    os.system('return.py')  #function : Run the file 'return'

def database():
    os.system('database.py')  #function : Run the file 'status'
    
def credit():
    os.system('credit.py')  #function : Run the file 'credit'



a = Tk()    # a is the window variable
a.title('Doodle Engine powered Library management')
a.geometry('500x300')
heading = Label(text = "Library ManageMent", bg = "grey",width = '43', height = "1", font = ("Lucida Handwriting", 13))
heading.grid(row=0, column=0, columnspan=2)
bt_issue = Button(a,text = 'Issue',width = 9, height = 1,command = issue )
bt_issue.grid(padx=5, pady=10, row=1, column=0)      #sets button issue
bt_return = Button(a,text = 'Return',width = 9, height = 1,command = ret )
bt_return.grid(padx=5, pady=10, row=1, column=1)     #sets button return
bt_status = Button(a,text = 'Database',width = 9, height = 1,command = database )
bt_status.grid(padx=5, pady=10, row=2, column=0)     #sets button status
bt_default = Button(a,text = 'Credits',width = 9, height = 1,command = credit )
bt_default.grid(padx=5, pady=10, row=2, column=1)    #sets button defaulter
bt_credits = Button(a,text = 'Exit',width = 9, height = 1,command = a.destroy )
bt_credits.grid(padx=20, pady=40,row=3 , column=0)    #sets button credit
a.mainloop()     #sets the GUI running
