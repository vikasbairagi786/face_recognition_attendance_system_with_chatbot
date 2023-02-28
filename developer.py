import tkinter
from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\bg4.png")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer's Pannel",font=("verdana",25,"bold"),bg="Black",fg="#00FF00")
        title_lb1.place(x=0,y=150,width=1366,height=45)

           #title section
        title_lb1 = Label(bg_img,text="Hello World!!",font=("verdana",10,"bold"),bg="White",fg="Black")
        title_lb1.place(x=0,y=200,width=1286,height=45)

        #title section
        title_lb1 = Label(bg_img,text="I'm Vikas Bairagi",font=("verdana",15,"bold"),bg="Black",fg="#00FF00")
        title_lb1.place(x=0,y=260,width=1256,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\m.jpg")
        std_img_btn=std_img_btn.resize((380,380),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=70,y=100,width=380,height=380)

        std_b1_1 = Button(bg_img,text="VIKAS BAIRAGI",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=70,y=490,width=380,height=45)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()