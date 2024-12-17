from tkinter import *
from tkinter import ttk
import tkinter.messagebox  
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox  
import mysql.connector
import tkinter
import os
from tkinter import Label

from time import strftime
from datetime import datetime

from student import StudentDetail  # first file name, second class name
from train import Train
from Face_Detector import Face_Detector
from attendace import Attendance

def rounded_image(image_path, size, radius):
    # Open and resize image
    img = Image.open(image_path).resize(size, Image.Resampling.LANCZOS)
    # Create a mask for rounded corners
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    # Apply mask to image
    img.putalpha(mask)
    return img


class Face_Recognition_Attendence_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1700x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # Image (background)
        img = Image.open(r"images\background1.jpg")
        img = img.resize((1700, 900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1700, height=900)

        # Title
        title_lbl = Label(f_lbl, text="Face Recognition Student Attendance Management System", font=("Ugfa", 25, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=20, width=1700, height=70)

        # Time display
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(f_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=20, y=700, width=150, height=50)
        time()

        # Buttons
        img1 = Image.open(r"images\studentDetail.jpg")
        img1 = img1.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(self.root, image=self.photoimg1, command=self.student_Details, cursor="hand2")
        b1.place(x=130, y=200, width=180, height=180)

        b1_1 = Button(self.root, text="Student Details", command=self.student_Details, cursor="hand2", font=("times new roman", 15, "bold"), bg="gold", fg="navy blue")
        b1_1.place(x=130, y=350, width=180, height=30)
        
        

        img2 = Image.open(r"images\Detectfacebutton.jpg")
        img2 = img2.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(self.root, image=self.photoimg2, cursor="hand2", command=self.face_Data)
        b2.place(x=390, y=200, width=180, height=180)

        b2_1 = Button(self.root, text="Face Detector", command=self.face_Data, cursor="hand2", font=("times new roman", 15, "bold"), bg="gold", fg="navy blue")
        b2_1.place(x=390, y=350, width=180, height=30)

        img3 = Image.open(r"images\attendence.png")
        img3 = img3.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(self.root, image=self.photoimg3, cursor="hand2", command=self.attendance_Data)
        b3.place(x=650, y=200, width=180, height=180)

        b3_1 = Button(self.root, text="Attendance", cursor="hand2", command=self.attendance_Data, font=("times new roman", 15, "bold"), bg="gold", fg="navy blue")
        b3_1.place(x=650, y=350, width=180, height=30)

        img4 = Image.open(r"images\photo.png")
        img4 = img4.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(self.root, image=self.photoimg4, cursor="hand2", command=self.open_img)
        b4.place(x=910, y=200, width=180, height=180)

        b4_1 = Button(self.root, text="Photo Sample", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="gold", fg="navy blue")
        b4_1.place(x=910, y=350, width=180, height=30)

        img5 = Image.open(r"images\trainData.jpg")
        img5 = img5.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(self.root, image=self.photoimg5, cursor="hand2", command=self.train_data)
        b5.place(x=1170, y=200, width=180, height=180)

        b5_1 = Button(self.root, text="Train data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="gold", fg="navy blue")
        b5_1.place(x=1170, y=350, width=180, height=30)

        # Exit button
        img6 = Image.open(r"images\exit.png")
        img6 = img6.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(self.root, image=self.photoimg6, cursor="hand2", command=self.iExit)
        b6.place(x=1200, y=600, width=200, height=50)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this page?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    # Functions for buttons
    def student_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentDetail(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)  # This will open the train window and keep it open

    def face_Data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Detector(self.new_window)

    def attendance_Data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Attendence_System(root)
    root.mainloop()
