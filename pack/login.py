from tkinter import *
import os

def run():
    os.system('interface.py')
    

creds = 'tempfile.temp' 
 
def Signup(): 
    global pwordE 
    global nameE
    global roots
 
    roots = Tk() 
    roots.title('Signup') 
    intruction = Label(roots, text='Please Enter new Credentials\n') 
    intruction.grid(row=0, column=0) 
 
    nameL = Label(roots, text='New Username: ') 
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W)
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1) 
 
    signupButton = Button(roots, text='Signup', command=FSSignup) 
    signupButton.grid(row = 3,column = 1)
    roots.mainloop() 
 
def FSSignup():
    with open(creds, 'w') as f: 
        f.write(nameE.get()) 
        f.write('\n') 
        f.write(pwordE.get()) 
        f.close() 
 
    roots.destroy() 
    Login() 
 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
    rootA.geometry('250x150')
 
    intruction = Label(rootA, text='Enter User Name \n & password\n') 
    intruction.grid(row = 0, column = 1) 
 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) 
    loginB.grid(row = 3,column = 1)

    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if nameEL.get() == uname and pwordEL.get() == pword: 
        r = Tk() 
        r.title('Login Success')
        r.geometry('250x70') 
        rlbl = Label(r, text='\n Successfully Logged In') 
        rlbl.pack() 
        launch = Button(r,text = 'Start',command = run)
        launch.pack()
        r.mainloop()
    else:
        r = Tk()
        r.title('INVALID')
        r.geometry('150x70')
        rlbl = Label(r, text='\n Invalid Login')
        rlbl.pack()
        rbutx = Button(r,text = 'Retry',command = r.destroy)
        rbutx.pack()
        r.mainloop()
 
 
if os.path.isfile(creds):
    Login()
else: 
    Signup()