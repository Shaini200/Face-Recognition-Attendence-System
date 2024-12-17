from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1700x900+0+0")
        self.root.title("Student Details")
        
        #--------------variables-----------------
        self.var_Atten_id=StringVar()
        self.var_Atten_name=StringVar()
        self.var_Atten_grade=StringVar()
        self.var_Atten_subject=StringVar()
        self.var_Atten_time=StringVar()
        self.var_Atten_date=StringVar()
        self.var_Atten_attendance=StringVar()

        #title
        title_lbl=Label(self.root,text="ATTENDANCE  MANAGEMENT  SYSTEM",font=("Arial Rounded MT Bold",30,"bold"),bg="gray",fg="dark blue") #Castellar
        title_lbl.place(x=0,y=20,width=1700,height=70)

        #Image
        img1=Image.open(r"images\1.png")
        img1 = img1.resize((1700, 700), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=0,y=90,width=1700,height=700)

        #main frame
        main_frame=Frame(self.root,bd=100,bg="#C0C9F8")
        main_frame.place(x=50,y=140,width=1400,height=610)

        #left label frame-----------------------------------
        left_frame=LabelFrame(main_frame,bd=1,bg="white", relief=RIDGE,text="Student Attendance Details",font=("times new roman",14,"bold"))
        left_frame.place(x=5,y=5,width=600,height=480)

        img1=Image.open(r"images\leftlabel.jpg")
        img1 = img1.resize((350, 80), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(left_frame,image=self.photoimg1)
        f_lbl1.place(x=10,y=0,width=350,height=80)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=120,width=595,height=330)

        #Labeland Entry
        #Attendance ID
        attendanceID_label=Label(left_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        stdID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_id,font=("times new roman",12))
        stdID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_name,font=("times new roman",12))
        name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Grade
        grade_label=Label(left_inside_frame,text="Grade",font=("times new roman",12,"bold"),bg="white")
        grade_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        subject_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_grade,font=("times new roman",12))
        subject_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #subject
        subject_label=Label(left_inside_frame,text="Subject",font=("times new roman",12,"bold"),bg="white")
        subject_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        subject_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_subject,font=("times new roman",12))
        subject_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Time
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_time,font=("times new roman",12))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_date,font=("times new roman",12))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #attendance
        attendance_Label=Label(left_inside_frame,text="Attendance Status",bg="white",font=("times new roman",12,"bold"))
        attendance_Label.grid(row=3,column=0)


        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_Atten_attendance,font=("times new roman",12,"bold"))
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame................
        btn_frame=Frame(left_inside_frame,bd=1,relief=RIDGE,bg="white")
        btn_frame.place(x=7,y=240,width=575,height=35)

        #import btn
        import_btn=Button(btn_frame,text="Import csv",command=self.impoerCsv,width=19,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        #export btn
        export_btn=Button(btn_frame,text="Export csv",command=self.exporeCsv,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        #update btn
        #update_btn=Button(btn_frame,text="Update",command=self.update,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        #update_btn.grid(row=0,column=2)

        #reset btn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)


        #right label frame----------------------------------
        right_frame=LabelFrame(main_frame,bd=1,bg="white", relief=RIDGE,text="Attendance Details",font=("times new roman",14,"bold"))
        right_frame.place(x=650,y=5,width=600,height=480)

        #frame................
        table_frame=Frame(right_frame,bd=1,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=590,height=440)

        #scroll bar table...................
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","grade","subject","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("grade",text="Grade")
        self.AttendanceReportTable.heading("subject",text="Subject")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("grade",width=100)
        self.AttendanceReportTable.column("subject",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=120)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #----------------fetch data--------------
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def impoerCsv(self):
        global mydata
        mydata.clear()
        filName=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(filName) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
              mydata.append(i)
            self.fetchData(mydata)  


    #export csv
    def exporeCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            filName=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(filName,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(filName)+" successfully")
        except Exception as es:
                messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)


        
        
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        if cursor_row:
            content = self.AttendanceReportTable.item(cursor_row)
            rows = content['values']
            if len(rows) >= 7:  # Ensure there are enough columns
                self.var_Atten_id.set(rows[0])
                self.var_Atten_name.set(rows[1])
                self.var_Atten_grade.set(rows[2])
                self.var_Atten_subject.set(rows[3])
                self.var_Atten_time.set(rows[4])
                self.var_Atten_date.set(rows[5])
                self.var_Atten_attendance.set(rows[6])
            else:
                messagebox.showwarning("Selection Error", "The selected row does not have enough data.")
        else:
            messagebox.showwarning("Selection Error", "No row selected.")



    def reset_data(self):
        self.var_Atten_id.set("")
        self.var_Atten_name.set("")
        self.var_Atten_grade.set("")
        self.var_Atten_subject.set("")
        self.var_Atten_time.set("")
        self.var_Atten_date.set("")
        self.var_Atten_attendance.set("")
        


    #def update(self):

        # Get the values from the form (input fields)
        #id = self.var_Atten_id.get()
        #name = self.var_Atten_name.get()
        #grade = self.var_Atten_grade.get()
        #subject = self.var_Atten_subject.get()
        #time = self.var_Atten_time.get()
        #date = self.var_Atten_date.get()
        #status = self.var_Atten_attendance.get()

        # Validate input (all fields must be filled)
        #if id == "" or name == "" or grade == "" or subject == "" or time == "" or date == "" or status == "":
            #messagebox.showerror("Error", "All fields are required")
            #return

        # Find the selected row in the table
        #selected_row = self.AttendanceReportTable.focus()
        #if selected_row == "":
            #messagebox.showerror("Error", "No row selected")
            #return

        # Get the index of the selected row in the `mydata` list
        #index = self.AttendanceReportTable.index(selected_row)
        
        # Update the `mydata` list at the found index
        #mydata[index] = [id, name, grade, subject, time, date, status]
        
        # Update the table display to reflect the changes
        #self.fetchData(mydata)  # Assuming you have this method to refresh the table display with updated data

        # Show success message
        #messagebox.showinfo("Success", "Record updated successfully")
        
        








        



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
