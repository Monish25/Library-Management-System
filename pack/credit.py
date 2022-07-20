from tkinter import *
a = Tk()
a.geometry('400x100')
a.title('Credits')
canvas = Canvas(a,width = 400, height = 200,bg ='grey' )
canvas.pack()
det1 = 'Library Management software(2019) \n v(1.0) \n Made By: Ashwin,Monish,Shaheen \n Made using Python 3.7.0 using Anaconda distribution'
lab1 = Label(canvas, text = det1)
lab1.pack()
but1 = Button(a,text = 'Ok', command = a.destroy)
but1.pack()
a.mainloop()