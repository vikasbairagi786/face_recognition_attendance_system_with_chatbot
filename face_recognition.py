from sys import path
from tkinter.ttk import Treeview
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import data
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import pyttsx3

from mysql.connector import cursor

class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 


        # backgorund image 1
        bg1=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\FaceRecog2.jpg")
        bg1=bg1.resize((650,700),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=55,width=650,height=700)


        # backgorund image 2
        bg2=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\facial_recognition_system.jpg")
        bg2=bg2.resize((950,700),Image.Resampling.LANCZOS)
        self.photobg2=ImageTk.PhotoImage(bg2)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg2)
        bg_img.place(x=650,y=55,width=950,height=700)


        #title section
        title_lb1 = Label(self.root,text="WELCOME TO FACE RECOGNITION PANEL",font=("Algerian",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=60,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="red")
        std_b1_1.place(x=60,y=350,width=180,height=45)


        # button
        std_b1_1=Button(bg_img,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("Times New Roman",18,"bold"),bg="black",fg="white")
        std_b1_1.place(x=365,y=620,width=200,height=40)

 #=====================Attendance===================

    def mark_attendance(self,i,r,n):
        with open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)
                id, predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()

                mycursor.execute("select Name from student where Student_ID="+str(id))
                n=mycursor.fetchone()
                n="+".join(n)
                #n=str(n)

                mycursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=mycursor.fetchone()
                r="+".join(r)
                #r=str(r)

                mycursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=mycursor.fetchone()
                i="+".join(i)
                #i=str(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0), 3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.mark_attendance(i,r,n)

                   
                   ###TESTING OF AUDIO LIBRARY###############
                    engine = pyttsx3.init()
                    # testing
                    voices = engine.getProperty('voices')
                    engine.setProperty('voice', voices[1].id)
                    engine.say("Your Attendance has been Marked. you can proceed further. Have a good day sir.")
                    engine.runAndWait()
                    engine.stop()
                    ##########################################


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,10, (255,25,255), "Face", clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize (img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()