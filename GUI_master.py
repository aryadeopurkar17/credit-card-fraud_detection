from tkinter import * 
import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
import math, random
from tkinter import messagebox as ms
##############################################+=============================================================

root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Face Recognisation")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('img1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Credit Card Fraud Detection", font=('times', 40,' bold '), height=1, width=50,bg="Brown",fg="white")
lbl.place(x=0, y=0)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=600, height=550, bd=5, font=('times', 15, ' bold '),bg="gray")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=400, y=100)


#

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 


def Create_database():
        
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)
    
#    id = input('enter user id')
    id=entry2.get()
    
    sampleN=0;
    
    while 1:
    
        ret, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
    
            sampleN=sampleN+1;
    
            cv2.imwrite("facesData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
    
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
            cv2.waitKey(100)
    
        cv2.imshow('img',img)
    
        cv2.waitKey(1)
    
        if sampleN > 40:
    
            break
    
    cap.release()
    entry2.delete(0,'end')
    cv2.destroyAllWindows()

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='blue1', fg='white')
    result_label.place(x=350, y=500)

def Train_database():
           
    recognizer =cv2.face.LBPHFaceRecognizer_create();
    
    path="facesData"
    
    def getImagesWithID(path):
    
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   
    
     # print image_path   
    
     #getImagesWithID(path)
    
        faces = []
    
        IDs = []
    
        for imagePath in imagePaths:      
    
      # Read the image and convert to grayscale
    
            facesImg = Image.open(imagePath).convert('L')
    
            faceNP = np.array(facesImg, 'uint8')
    
            # Get the label of the image
    
            ID= int(os.path.split(imagePath)[-1].split(".")[1])
    
             # Detect the face in the image
    
            faces.append(faceNP)
    
            IDs.append(ID)
    
            cv2.imshow("Adding faces for traning",faceNP)
    
            cv2.waitKey(10)
    
        return np.array(IDs), faces
    
    Ids,faces  = getImagesWithID(path)
    
    recognizer.train(faces,Ids)
    
    recognizer.save("trainingdata.yml")
    
    cv2.destroyAllWindows()
a=IntVar()
# def author_identification():
#     frame_alpr1 = tk.LabelFrame(root, text=" --Transaction-- ", width=900, height=400, bd=5, font=('times', 14, ' bold '),bg="SeaGreen1")
#     frame_alpr1.grid(row=0, column=0, sticky='nw')
#     frame_alpr1.place(x=330, y=90)
#     result_label = tk.Label(frame_alpr1, text="Credit Card No :", width=15, font=("bold", 15), bg='bisque2', fg='black')
#     result_label.place(x=150, y=80)
    
    
    # entry3=tk.Entry(frame_alpr1,bd=2,width=30,textvariable=a)
    # entry3.place(x=350, y=80)
    
    # button3 = tk.Button(root, text="Authenticate User", command=Test_database, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
    # button3.place(x=350, y=480)
    


def Test_database():
   flag=0
   recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)    
        #ms.showinfo("message","Successfully Updated")  
   recognizer.read('trainingdata.yml')
   cascadePath = "haarcascade_frontalface_default.xml"
   faceCascade = cv2.CascadeClassifier(cascadePath);
   font = cv2.FONT_HERSHEY_SIMPLEX
        #iniciate id counter
   id = 0
        # names related to ids: example ==> Marcelo: id=1,  etc
        #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person'] 
        # Initialize and start realtime video capture
   cam = cv2.VideoCapture(0)
   cam.set(3, 640) # set video widht
   cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
   minW = 0.1*cam.get(3)
   minH = 0.1*cam.get(4)
    
   while True:
       ret, img =cam.read()
#             img = cv2.flip(img, -1) # Flip vertically
       gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
       faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))
       for(x,y,w,h) in faces:
           cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
           id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
                # If confidence is less them 100 ==> "0" : perfect match
                
           if (confidence < 60):
               #print(id)
                #name = names[id]
                id = id
                
                print(type(id))
                
                #
                #id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                
                         
                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
             
                cam.release()  
                #l = Label(frame_display1, text = "Authenticated User...Locker Successfully Open..") 
                #l.config(font =("Courier", 20, "bold"),fg= 'green') 
                #l.place(x=330,y=400)
                #l.pack()
                update_label('Authenticated User...')
          
                #button4 = tk.Button(root, text="Generate OTP", command=otp, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
                #button4.place(x=800, y=290)
                from subprocess import call
                call(["python", "Trans_Mast.py"]) 
                
                
           else:
#                 print(confidence)
              id = "unknown Person Identified"
              confidence = "  {0}%".format(round(100 - confidence))
                
              cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
              cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
                
              cam.release() 
               # l = Label(frame_display1, text = "Ooops!!!!!....Unauthenticated User..") 
               # l.config(font =("Courier", 25,"bold"),fg= 'red4') 
                #l.place(x=330,y=400)
                #l.pack() 
              update_label('Ooops!!!!!....Unauthenticated User..')
               

              cv2.imshow('camera',img) 

              if cv2.waitKey(1) == ord('Q'):
                break

def registration():
    
##### tkinter window ######
    
    print("Registration")
    from subprocess import call
    call(["python", "registration.py"]) 




        
        
        
def ID():     
    my_conn = sqlite3.connect('face.db')
    r_set=my_conn.execute("SELECT * FROM User")
    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e =tk.Entry(frame_display, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
        
        
def otp():
    from subprocess import call
    call(["python", "Trans_Mast.py"]) 
          
            
    



#################################################################################################################
def window():
    root.destroy()


#button1 = tk.Button(frame_alpr, text="Registration Of User", command=registration,width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
#button1.place(x=10, y=50)

button1 = tk.Button(frame_alpr, text="Create Face Data", command=Create_database,width=15, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
button1.place(x=100, y=100)

button2 = tk.Button(frame_alpr, text="Train Face Data", command=Train_database, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
button2.place(x=100, y=200)

button3 = tk.Button(frame_alpr, text="Authenicate User", command=Test_database, width=20, height=1, font=('times', 15, ' bold '),bg="purple",fg="white")
button3.place(x=100, y=300)


entry2=tk.Entry(frame_alpr,bd=2,width=7,font=('times', 15, ' bold '))
entry2.place(x=300, y=100)


##
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=10, y=280)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=100, y=400)



root.mainloop()