from tkinter import *
from tkinter import messagebox
import tkinter
import time
import  os
from PIL import Image , ImageTk     
from PIL import Image 

from tkinter import messagebox as ms

Window=Tk()
Window.geometry("820x320")
Window.title("Verification Screen")
Window.configure(background="sandy brown")
count = 3  #global variable for count calculation. Initially there are 3 attempts. So I set as 3
# image2 =Image.open('2.png')
# image2 =image2.resize((820,320), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label =Label(Window, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0) 
def verify():
    global count
    global Window
    end=time.time()          # timers ends when the user clicks verfiy
    t = format(end - start)  # calculate the difference between end and start timer
    print(float(t))          #  print the time in seconds
    if float(t) >= 120:      # Check it the user enters above 2 minutes. So i set as >=120
        messagebox.showinfo("Time out", "Session Expired ...Time out Please regenerate OTP")
        Window.destroy()
    else:
        b=str(a.get())             # Get the entered OTP
        #cmd='python verify.py '+cmd1
        f1=open("otp.txt","r")
        b1=f1.read()
        f1.close()
        #print(b,b1)
        if b==b1:
            f = open("status.txt", "w")
            f.write("success")
            f.close()
            #Window = Tk()
            #Window.geometry("620x320")
            #Window.title("Success") 
            messagebox.showinfo("Congratulations", "Your OTP was verified Successfully!!.")
            Window.destroy()
            #Window.destroy()
            from subprocess import call
            call(["python", "Trans_Mast.py"]) 
            
            #Window.destroy()
            #Window.mainloop()
        else:
            f = open("status.txt", "w")
            f.write("failure")
            f.close()
            #os.system(cmd)                # call the verify program
            ok='Invalid OTP: '+str((count-1))+' attempts remaining'
            count=count-1
            f1=open("status.txt","r")
            bh=f1.read()

            if count>=1 and bh != "success":

                tkinter.messagebox.askretrycancel("Error", ok)
                f1.close()
            elif count == 0 and bh != "success":
                f=open("otp.txt","w")
                f.write("")
                f.close()
                messagebox.showinfo("Oooo","Your 3 attempts was over. Please regenerate OTP")
                f1.close()
                Window.destroy()
                
                

            elif bh == "success":
                f1.close()
                Window.destroy()

start=time.time() # Timer started once the screen is entered
label1=Label(Window,text="Verification Screen",relief="solid",font=("arial",20,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="Enter your Otp",font=("arial",15,"bold")).place(x=20,y=90)
w1=Entry(Window,width=20,textvariable=a,font=("arial",15,"bold"))
w1.place(x=250,y=90)
Re1=Label(Window,text="Please enter within 2 minutes",font=("arial",10,"bold")).place(x=550,y=90)
ver = Button(Window, text="Verify",relief="raised", bg='blue', font=("arial", 25, "bold"), fg='white',command=verify).place(x=350,y=180)
Window.mainloop()