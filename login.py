from tkinter import *
from tkinter import ttk
import tkinter.messagebox  
from PIL import Image, ImageTk
from tkinter import messagebox  
import mysql.connector
import tkinter
import os
from tkinter import Label

from time import strftime
from datetime import datetime

from main import Face_Recognition_Attendence_System   #first file name, second class name

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1700x900+0+0")
        self.root.title("Login")

        #variable
        self.var_email=StringVar()
        self.var_password=StringVar()
        
        

        #background image
        img=Image.open(r"images\log.png")
        img = img.resize((1700, 900), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1700,height=900)

        #Frame
        frame=Frame(self.root,bg="black")
        frame.place(x=580,y=170,width=340,height=480)

        img1=Image.open(r"images\login1.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        img1_lbl=Label(image=self.photoimg1,bg="black",borderwidth=0)
        img1_lbl.place(x=695,y=190,width=100,height=100)



        get_start=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="#5998DD",bg="black")
        get_start.place(x=100,y=120)

        #User Name
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",14,"bold"),fg="white",bg="black")
        username.place(x=70,y=160)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.txtuser.place(x=50,y=190,width=220,height=25)

        #Password
        #label
        password=lbl=Label(frame,text="Password",font=("times new roman",14,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",13,"bold"),show="*")
        self.txtpass.place(x=50,y=260,width=220,height=25)

        #icon images
        #username
        img2=Image.open(r"images\user.png")
        img2 = img2.resize((20, 20), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        img2_lbl=Label(image=self.photoimg2,bg="black",borderwidth=0)
        img2_lbl.place(x=628,y=332,width=20,height=20)

        #password
        img3=Image.open(r"images\password.png")
        img3 = img3.resize((20, 20), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        img3_lbl=Label(image=self.photoimg3,bg="black",borderwidth=0)
        img3_lbl.place(x=628,y=405,width=20,height=20)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="#1405D1",activeforeground="white",activebackground="#4A3CFA")
        loginbtn.place(x=110,y=325,width=120,height=40)

        #register button
        loginbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",11,"bold"),bd=3,borderwidth=0,fg="#DEE909",bg="black",activeforeground="#F2F95D",activebackground="black")
        loginbtn.place(x=35,y=390,width=160)

        #forget password
        loginbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",11,"bold"),bd=3,borderwidth=0,fg="#DEE909",bg="black",activeforeground="#F2F95D",activebackground="black")
        loginbtn.place(x=28,y=420,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
           messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="Kapu" and self.txtpass.get()=="abc":
            messagebox.showwarning("Success","Welcome!!!!!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shaini123#",database="face_recognition")    
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                    self.var_email.get(),
                                                                    self.var_password.get()         
                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_Attendence_System(self.new_window)
                    
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #--------reset password----------
    def reset_password(self):
        if self.combo_findQuestion.get()=="Select":
            messagebox.showerror("Error","Select these security question",parent=self.root2)
        elif self.answer_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.newPassword_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shaini123#",database="face_recognition")    
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and findQuestion=%s and answer=%s")
            value=(self.txtuser.get(),self.combo_findQuestion.get(),self.answer_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.newPassword_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()
    





    #-----------forget password window------------
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shaini123#",database="face_recognition")    
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)


            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("450x500+600+170")
                self.root2.configure(bg='#C1D3DD')

                l=Label(self.root2,text="Forget Password",font=("times new roman",18,"bold"),fg="#96D6D6",bg="black")
                l.place(x=0,y=10,relwidth=1)


                #label
                findQuestion=Label(self.root2,text="Select Security Question",font=("times new roman",14,"bold"),fg="black",bg="#C1D3DD")
                findQuestion.place(x=50,y=70)
                #entry
                self.combo_findQuestion=ttk.Combobox(self.root2, font=("times new roman", 13),state="readonly")
                self.combo_findQuestion["values"]=("Select","Your Birth place","Your last school","Your favourite color","Your pet name")
                self.combo_findQuestion.place(x=50,y=100,width=300)
                self.combo_findQuestion.current(0)


                #label
                answer=Label(self.root2,text="Security Answers",font=("times new roman",14,"bold"),fg="black",bg="#C1D3DD")
                answer.place(x=50,y=140)
                #entry
                self.answer_entry = ttk.Entry(self.root2, font=("times new roman", 13))
                self.answer_entry.place(x=50, y=170, width=300)


                #label
                newPassword=Label(self.root2,text="New Passwords",font=("times new roman",14,"bold"),fg="black",bg="#C1D3DD")
                newPassword.place(x=50,y=210)
                #entry
                self.newPassword_entry = ttk.Entry(self.root2, font=("times new roman", 13),show="*")
                self.newPassword_entry.place(x=50, y=240, width=300)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",14,"bold"),fg="white",bg="#140571",activeforeground="black",activebackground="#140571")
                btn.place(x=120,y=300,width=200)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1700x900+0+0")
        self.root.title("Register Form")


        #-------variable------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_findQuestion=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()
        self.var_confirmPassword=StringVar()
        

        #background image
        img=Image.open(r"images\login.jpg")
        img = img.resize((1700, 900), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1700,height=900)

        #Frame
        frame=Frame(self.root,bg="#0B094B")
        frame.place(x=400,y=140,width=680,height=480)

        register_lbl = Label(frame, text="REGISTER HERE...", font=("times new roman", 20, "bold"), fg="#0CF006",bg="#0B094B")
        register_lbl.place(x=20, y=20)

        #-------------label & entry-----------------

        #label------------->1 row
        fname=Label(frame,text="First Name",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        fname.place(x=50,y=90)
        #entry
        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 13))
        self.fname_entry.place(x=50, y=120, width=200)


        #label
        lname=Label(frame,text="Last Name",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        lname.place(x=350,y=90)
        #entry
        self.lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 13))
        self.lname_entry.place(x=350, y=120, width=200)



        #label------------->2 row
        contact=Label(frame,text="Contact No",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        contact.place(x=50,y=160)
        #entry
        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 13))
        self.contact_entry.place(x=50, y=190, width=200)


        #label
        email=Label(frame,text="Email",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        email.place(x=350,y=160)
        #entry
        self.email_entry = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 13))
        self.email_entry.place(x=350, y=190, width=200)



        #label------------->3 row
        findQuestion=Label(frame,text="Select Security Question",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        findQuestion.place(x=50,y=230)
        #entry
        self.combo_findQuestion=ttk.Combobox(frame,textvariable=self.var_findQuestion, font=("times new roman", 13),state="readonly")
        self.combo_findQuestion["values"]=("Select","Your Birth place","Your last school","Your favourite color","Your pet name")
        self.combo_findQuestion.place(x=50,y=260,width=200)
        self.combo_findQuestion.current(0)


        #label
        answer=Label(frame,text="Security Answers",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        answer.place(x=350,y=230)
        #entry
        self.answer_entry = ttk.Entry(frame,textvariable=self.var_answer, font=("times new roman", 13))
        self.answer_entry.place(x=350, y=260, width=200)




        #label------------->4 row
        password=Label(frame,text="Password",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        password.place(x=50,y=300)
        #entry
        self.password_entry = ttk.Entry(frame,textvariable=self.var_password, font=("times new roman", 13),show="*")
        self.password_entry.place(x=50, y=330, width=200)


        #label
        confirmPassword=Label(frame,textvariable=self.var_confirmPassword,text="Confirm Password",font=("times new roman",14,"bold"),fg="white",bg="#0B094B")
        confirmPassword.place(x=350,y=300)
        #entry
        self.confirmPassword_entry = ttk.Entry(frame, font=("times new roman", 13),show="*")
        self.confirmPassword_entry.place(x=350, y=330, width=200)
        

        #----check button----
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman", 13,"bold"),fg="white",bg="#0B094B",activeforeground="white",activebackground="#0B094B",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=370)

        #-----button------
        registerbtn=Button(frame,command=self.registerData,text="Registor Now",borderwidth=0,cursor="hand2",font=("times new roman",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="#F21E08",activeforeground="black",activebackground="#F21E08")
        registerbtn.place(x=100,y=400,width=200,height=40)

        exitbtn=Button(frame,command=self.return_exit,text="Exit Now",borderwidth=0,cursor="hand2",font=("times new roman",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="#F21E08",activeforeground="black",activebackground="#F21E08")
        exitbtn.place(x=330,y=400,width=200,height=40)


    #------function declaration----------
    def registerData(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_password.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.password_entry.get()!=self.confirmPassword_entry.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shaini123#",database="face_recognition")    
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                                                        self.var_fname.get(),
                                                        self.var_lname.get(),
                                                        self.var_contact.get(),
                                                        self.var_email.get(),
                                                        self.var_findQuestion.get(),
                                                        self.var_answer.get(),
                                                        self.var_password.get()
                ))


            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfully")
    
    def return_exit(self):
        self.root.destroy()

    #------------Functions buttons-----------------
    def FaceRecognitionAttendenceSystem(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_Attendence_System(self.new_window)


if __name__ == "__main__":
    main()

