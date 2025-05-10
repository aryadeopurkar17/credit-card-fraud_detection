import os
from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk     
from PIL import Image 

from tkinter import messagebox as ms
Window=Tk()
Window.geometry("620x320")
Window.title("MAIL OTP")
w, h = Window.winfo_screenwidth(), Window.winfo_screenheight()
#Window.geometry("%dx%d+0+0" % (w, h))
#------------------------
image2 =Image.open('1.png')
image2 =image2.resize((620,320), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label =Label(Window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
a=IntVar()
#--------------------------------------------------------
def verify():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)
label1=Label(Window,text="One Time Password",relief="solid",font=("arial",26,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="EMAIL ID",font=("arial",15,"bold"),width=20).place(x=50,y=100)
w=Entry(Window,width=20,validate="key",textvariable=a,font=("arial",15,"bold"))
w.place(x=320,y=100)

log = Button(Window, text="Proceed",relief="raised", bg='maroon', font=("arial", 22, "bold"), fg='black',command=verify).place(x=250,y=190)
Window.mainloop()