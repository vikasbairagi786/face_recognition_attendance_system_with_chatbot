import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #install pillow


class ChatBot:
        def __init__(self,root):
            self.root=root
            self.root.geometry("730x620+0+0")
            self.root.title("ChatBot")
            #self.root.bind('<Return>',self.enter_func)


            main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
            main_frame.pack()


            img_chat=Image.open(r"E:\PROJECTS\Face Recognition Attendance System\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\chatbot.png")
            img_chat=img_chat.resize((200,70),Image.Resampling.LANCZOS)
            self.photoimg=ImageTk.PhotoImage(img_chat)

            Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='- - -Welcome to the CHAT BOT Pannel',font=('arial',20,'bold'),fg='green',bg='Black')
            Title_label.pack(side=TOP)

            self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
            self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
            self.scroll_y.pack(side=RIGHT,fill=Y)
            self.text.pack()

            btn_frame=Frame(self.root,bd=4,bg='white',width=730)
            btn_frame.pack()

            

            label_1=Label(btn_frame,text="Type something",font=('arial',14,'bold'),fg='green',bg='white')
            label_1.grid(row=0,column=0,padx=5,sticky=W)


            self.entry=StringVar()
            self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('Times New Row',14,'bold'))
            self.entry1.grid(row=0,column=1,padx=5,sticky=W)

            self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',13,'bold'),width=8,bg='green')
            self.send.grid(row=0,column=2,padx=5,sticky=W)
            
            self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',13,'bold'),width=8,bg='red',fg='white')
            self.clear.grid(row=1,column=0,padx=5,sticky=W)

            self.msg=''
            self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
            self.label_11.grid(row=1,column=1,padx=5,sticky=W)

            #====================FUNCTION DECLARATION===========
        def enter_func(self,event):
            self.send.invoke()
            self.entry.set('')

        def clear(self):
            self.text.delete('1.0',END)
            self.entry.set('')

        def send(self):
            send='\t\t\t'+'You: '+self.entry.get()
            self.text.insert(END,'\n'+send)
            self.text.yview(END)

            if (self.entry.get()==''):
                self.msg='Please enter some input'
                self.label_11.config(text=self.msg,fg='red')

            else:
                self.msg=''
                self.label_11.config(text=self.msg,fg='red')

            if (self.entry.get()=='hello'):
                self.text.insert(END,'\n\n'+'Bot: Hello World!\n\n Welcome to the world of Innovation.\n\n I am an Artificial Intelligence based CHATBOT build to serve the nation.\n Devloped by : VIKAS BAIRAGI\n\n How can i help you sir/madam.? \n\nyou can give different commands by typing something in the textbox given below.')


            elif (self.entry.get()=='Hii'):
                self.text.insert(END,"\n\n"+"Bot: Hello")

            elif (self.entry.get()=='how are you?'):
                self.text.insert(END,"\n\n"+"Bot: I am fine sir/madam thank you. hope you also might be doing wonderfull.")
            
            elif (self.entry.get()=='I am also fine'):
                self.text.insert(END,"\n\n"+"Bot: Nice to hear that")
            
            elif (self.entry.get()=='Who developed you?'):
                self.text.insert(END,"\n\n"+"Bot: my sir mr. VIKAS BAIRAGI devloped me.\n\n I always feel proud to answer this question.\n\n You can know more about VIKAS BAIRAGI by clicking the link below\n https://linktr.ee/vikasbairagi08")

            elif (self.entry.get()=='can you reply in hindi?'):
                self.text.insert(END,"\n\n"+"Bot: जी हां बिल्कुल परंतु ,कुछ सीमित ही |\n\n मेरे रचयिता विकास बैरागी इस पर शोध कर रहे हैं, और मुझे पूरा विश्वास है शीघ्र ही में पूर्ण रूप से हिंदी में उत्तर देने के काबिल हो जाऊंगा || ")

            elif (self.entry.get()=='what is Machine Learning?'):
                self.text.insert(END,"\n\n"+"Bot: Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.")

            elif (self.entry.get()=='how does face recognition work?'):
                self.text.insert(END,"\n\n"+"Bot: The face capture process transforms analog information (a face) into a set of digital information (data) based on the person's facial features. Your face's analysis is essentially turned into a mathematical formula. The numerical code is called a faceprint.")

            elif (self.entry.get()=='what is python programming?'):
                self.text.insert(END,"\n\n"+"Bot: Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.")

            elif (self.entry.get()=='what is your name?'):
                self.text.insert(END,"\n\n"+"Bot: my devloper does not gave me any specific name but everyone call me \nCHATBOT 🤗 ")


            elif (self.entry.get()=='bye'):
                self.text.insert(END,"\n\n"+"Bot: Thank you for chatting :) \n Have a good day")

            else:
                self.text.insert(END,"\n\n"+"Bot : Sorry!!! I didn't get it :(")
            


if __name__ == "__main__":
    root = Tk()
    obj=ChatBot(root)
    root.mainloop()