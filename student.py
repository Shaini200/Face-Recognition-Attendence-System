from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import messagebox
import mysql.connector
import cv2
import os
#from mysql.connector import Error



class StudentDetail:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1700x900+0+0")
        self.root.title("Student Details")
        
        #---------------variables---------------
        self.var_grade = StringVar()
        self.var_year = StringVar() 
        self.var_sub = StringVar()
        self.var_StudentID = StringVar()
        self.var_sname = StringVar()
        self.var_gender = StringVar()
        self.var_Dob = StringVar()
        self.var_parentName = StringVar()
        self.var_PhoneNo = StringVar()
        self.var_address = StringVar()
        




        #image (background)
        img=Image.open(r"C:\Users\shaini\Desktop\Face Recognition attendence system\images\2.png")
        img = img.resize((1700, 300), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1700,height=300)

        #title
        title_lbl=Label(f_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("HP Simplified Hans",30,"bold"),bg="dark gray",fg="dark blue") #Castellar
        title_lbl.place(x=0,y=20,width=1700,height=60)

        #main frame
        main_frame=Frame(self.root,bd=100)
        main_frame.place(x=50,y=130,width=1400,height=620)

        #left label frame-----------------------------------
        left_frame=LabelFrame(main_frame,bd=1,bg="white", relief=RIDGE,text="Student Details",font=("times new roman",17,"bold"))
        left_frame.place(x=5,y=5,width=600,height=580)

        img1=Image.open(r"C:\Users\shaini\Desktop\Face Recognition attendence system\images\leftlabel.jpg")
        img1 = img1.resize((350, 80), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(left_frame,image=self.photoimg1)
        f_lbl1.place(x=10,y=0,width=350,height=80)

        #current class..............
        current_class=LabelFrame(left_frame,bd=1,bg="white", relief=RIDGE,text="Current Class",font=("times new roman",14,"bold"))
        current_class.place(x=5,y=80,width=580,height=120)

        #Grade
        grade_label=Label(current_class,text="Grade",font=("times new roman",12,"bold"),bg="white")
        grade_label.grid(row=0,column=0)

        grade_combo=ttk.Combobox(current_class,textvariable=self.var_grade,font=("times new roman",12),width=20,state="read only")
        grade_combo["values"]=("Select Grade","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11")
        grade_combo.current(0)
        grade_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        #subject
        sub_label=Label(current_class,text="Subject",font=("times new roman",12,"bold"),bg="white")
        sub_label.grid(row=0,column=2)

        sub_combo=ttk.Combobox(current_class,textvariable=self.var_sub,font=("times new roman",12),width=20,state="read only")
        sub_combo["values"]=("Select Subject","Maths","Science","Sinhala","ICT","Commerce","History","Geography","Tamil","English","Music")
        sub_combo.current(0)
        sub_combo.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #year
        year_label=Label(current_class,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(current_class,textvariable=self.var_year,font=("times new roman",12),width=20,state="read only")
        year_combo["values"]=("Select year","2023","2024","2025","2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        #student Information..............
        student_info=LabelFrame(left_frame,bd=1,bg="white", relief=RIDGE,text="Student Information",font=("times new roman",14,"bold"))
        student_info.place(x=5,y=220,width=580,height=350)

        #Student ID
        stdID_label=Label(student_info,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        stdID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        stdID_entry=ttk.Entry(student_info,width=10,textvariable=self.var_StudentID,font=("times new roman",12))
        stdID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student Name
        stdName_label=Label(student_info,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        stdName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        stdName_entry=ttk.Entry(student_info,width=25,textvariable=self.var_sname,font=("times new roman",12))
        stdName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Gender
        gender_label=Label(student_info,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        #gender_entry=ttk.Entry(student_info,width=10,textvariable=self.var_gender,font=("times new roman",12))
        #gender_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        gender_combo=ttk.Combobox(student_info,textvariable=self.var_gender,font=("times new roman",12),width=20,state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        #DOB
        dob_label=Label(student_info,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_info,width=15,textvariable=self.var_Dob,font=("times new roman",12))
        dob_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)


        #parent's name
        parent_label=Label(student_info,text="Parent's Name",font=("times new roman",12,"bold"),bg="white")
        parent_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        parent_entry=ttk.Entry(student_info,width=10,textvariable=self.var_parentName,font=("times new roman",12))
        parent_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Phone No.
        phoneNo_label=Label(student_info,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        phoneNo_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        phoneNo_entry=ttk.Entry(student_info,width=15,textvariable=self.var_PhoneNo,font=("times new roman",12))
        phoneNo_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Address
        address_label=Label(student_info,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        address_entry=ttk.Entry(student_info,width=12,textvariable=self.var_address,font=("times new roman",12))
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(student_info, text="Take Photo Sample", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2 = ttk.Radiobutton(student_info, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame................
        btn_frame=Frame(student_info,bd=1,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=575,height=35)

        #save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update btn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete btn
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset btn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #button frame................
        btn_frame1=Frame(student_info,bd=1,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=205,width=575,height=35)


        #Take Photo btn
        #takePhoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=28,font=("times new roman",13,"bold"),bg="blue",fg="white")
        #takePhoto_btn.grid(row=0,column=0)

        #update photo btn
        updatePhoto_btn=Button(btn_frame1,command=self.update_photo_sample,text="Update photo Sample",width=56,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatePhoto_btn.grid(row=0,column=0)




        #right label frame----------------------------------
        right_frame=LabelFrame(main_frame,bd=1,bg="white", relief=RIDGE,text="Student Details",font=("times new roman",17,"bold"))
        right_frame.place(x=650,y=5,width=550,height=580)

        img2=Image.open(r"C:\Users\shaini\Desktop\Face Recognition attendence system\images\right.jpg")
        img2 = img2.resize((350, 100), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(right_frame,image=self.photoimg2)
        f_lbl2.place(x=70,y=5,width=350,height=100)


        #.....Search system......
        search_frame=LabelFrame(right_frame,bd=1,bg="white", relief=RIDGE,text="Search System",font=("times new roman",14,"bold"))
        search_frame.place(x=5,y=80,width=530,height=100)

        search_label=Label(search_frame,text="Search by:",font=("times new roman",12,"bold"),bg="green")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)



        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),width=15,state="read only")
        search_combo["values"]=("Select","Student ID","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)


        #update btn
        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=1,column=1,padx=4)

        #delete btn
        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=1,column=2,padx=4)


        #.....table frame.....
        table_frame=LabelFrame(right_frame,bd=1,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=200,width=530,height=280)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("grade","sub","year","StudentID","sname","gender","Dob","parentName","PhoneNo","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("grade",text="Grade")
        self.student_table.heading("sub",text="Subject")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("StudentID",text="Student ID")
        self.student_table.heading("sname",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("parentName",text="Parent's Name")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("grade",width=100)
        self.student_table.column("sub",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("StudentID",width=100)
        self.student_table.column("sname",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("parentName",width=100)
        self.student_table.column("PhoneNo",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=110)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #----Function decration-----------------
    def add_data(self):
        if self.var_grade.get()=="Select Grade" or self.var_sname.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Shaini123#',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                #my_cursor.execute("insert into student value(grade,sub,year,StudentID,sname,gender,Dob,parentName,PhoneNo,address,radio1)",(
                    
                                                                                    self.var_grade.get(),
                                                                                    self.var_sub.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_StudentID.get(),
                                                                                    self.var_sname.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_Dob.get(),
                                                                                    self.var_parentName.get(),
                                                                                    self.var_PhoneNo.get(),
                                                                                    self.var_address.get(),             
                                                                                    self.var_radio1.get()        
                                                                                        
                                                                                        )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)

    #------------fetch Data----------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shaini123#",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #------------get cursor----------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        if len(data) == 11:  # Assuming there are 11 columns (grade, sub, year, StudentID, etc.)
            self.var_grade.set(data[0])
            self.var_sub.set(data[1])
            self.var_year.set(data[2])
            self.var_StudentID.set(data[3])
            self.var_sname.set(data[4])
            self.var_gender.set(data[5])
            self.var_Dob.set(data[6])
            self.var_parentName.set(data[7])
            self.var_PhoneNo.set(data[8])
            self.var_address.set(data[9])
            self.var_radio1.set(data[10]) 


    #------------delete Data----------
    def delete_data(self):
        if self.var_StudentID.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student's record?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Shaini123#', database='face_recognition')
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_ID=%s"
                    val = (self.var_StudentID.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Student record has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    

    #------------update Data----------
    def update_data(self):
        if self.var_grade.get() == "Select Grade" or self.var_sname.get() == "" or self.var_StudentID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's record?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Shaini123#', database='face_recognition')
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Grade=%s,Subject=%s,Year=%s,Name=%s,Gender=%s,DOB=%s,Parent_Name=%s,Phone_No=%s,Address=%s,Sampl_Photo=%s where Student_ID=%s",
                        (
                                                                                    self.var_grade.get(),
                                                                                    self.var_sub.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_sname.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_Dob.get(),
                                                                                    self.var_parentName.get(),
                                                                                    self.var_PhoneNo.get(),
                                                                                    self.var_address.get(),             
                                                                                    self.var_radio1.get(),
                                                                                    self.var_StudentID.get()
                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    

    #reset
    def reset_data(self):
        self.var_grade.set("Select Grade")
        self.var_sub.set("Select Subject")
        self.var_year.set("Select Year")
        self.var_StudentID.set("")
        self.var_sname.set("")
        self.var_gender.set("Male")
        self.var_Dob.set("")
        self.var_parentName.set("")
        self.var_PhoneNo.set("")
        self.var_address.set("")
        self.var_radio1.set("")
                

   

 # Generate data set or take a photo sample



    def generate_dataset(self):
        # Check if all required fields are filled
        if self.var_grade.get() == "Select Grade" or self.var_sub.get() == "" or self.var_year.get() == "" or self.var_StudentID.get() == "" or self.var_sname.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Establish MySQL connection
                conn = mysql.connector.connect(host="localhost", username="root", password="Shaini123#", database="face_recognition")
                my_cursor = conn.cursor()

                # Fetch all student records to determine the ID
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()

                # Initialize an ID counter based on the number of students
                id = len(myresult) + 1

                # Update student record with provided details
                my_cursor.execute(
                    "UPDATE student SET Grade=%s, Subject=%s, Year=%s, Name=%s, Gender=%s, DOB=%s, Parent_Name=%s, Phone_No=%s, Address=%s, Sampl_Photo=%s WHERE Student_ID=%s",
                    (
                        self.var_grade.get(),
                        self.var_sub.get(),
                        self.var_year.get(),
                        self.var_sname.get(),
                        self.var_gender.get(),
                        self.var_Dob.get(),
                        self.var_parentName.get(),
                        self.var_PhoneNo.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),  # Assuming this is for photo sample status
                        self.var_StudentID.get()  # Using the provided Student ID to update
                    )
                )

                conn.commit()  # Commit the changes
                self.fetch_data()  # Refresh the UI table data
                self.reset_data()  # Reset the form data
                conn.close()

                # Ensure the directory for saving the images exists
                output_dir = "data/"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # Load face classifier for detection
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                print(hasattr(cv2, 'CascadeClassifier'))
                # Function to detect and crop faces
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # If faces are detected, return the cropped face
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                # Capture photos using the webcam
                cap = cv2.VideoCapture(0)
                img_id = 0
                student_id = self.var_StudentID.get() # Get the current student's ID

                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)

                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert face to grayscale

                        # Save the captured face image with a unique name
                        file_name_path = f"data/users.{str(student_id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path, face)

                        # Display the captured face with the image number overlay
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    # Break the loop if 'Enter' key is pressed or 100 samples have been taken
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break
                    
                    

                cap.release()
                cv2.destroyAllWindows()

                # Indicate that dataset generation is completed
                messagebox.showinfo("Result", "Generating dataset completed successfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        
    def update_photo_sample(self):
        if self.var_StudentID.get() == "":
            messagebox.showerror("Error", "Student ID is required to update photo", parent=self.root)
        else:
            try:
                
                # Open the camera and capture new photo samples
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                student_id = self.var_StudentID.get()  # Get the current student's ID

                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)

                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert face to grayscale

                        # Ensure the student ID and image ID are formatted correctly
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)

                        # Display the captured face with the image number overlay
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    # Break the loop if 'Enter' key is pressed or 100 samples have been taken
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                # Message box to indicate the completion of the photo update
                messagebox.showinfo("Result", "Photo samples updated successfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

                
                    
    




if __name__ == "__main__":
    root = Tk()
    obj = StudentDetail(root)
    root.mainloop()