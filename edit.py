from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import os
from time import strftime
from student import StudentDetail
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

        # Background Image
        img = Image.open(r"images\display.png")
        img = img.resize((1700, 900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1700, height=900)

        # Title
        title_lbl = Label(f_lbl, text="Face Recognition Student Attendance Management System",
                          font=("ItalicT", 25, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=20, width=1700, height=70)

        # Time Display
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(f_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=20, y=700, width=150, height=50)
        time()

        # Button with Rounded Image
        def create_button(x, y, image_path, text, command):
            # Create rounded image
            rounded_img = rounded_image(image_path, (180, 180), radius=30)
            photoimg = ImageTk.PhotoImage(rounded_img)

            # Button with image
            img_btn = Button(self.root, image=photoimg, cursor="hand2", command=command, bd=0)
            img_btn.image = photoimg  # Keep reference to avoid garbage collection
            img_btn.place(x=x, y=y, width=180, height=180)

            # Label below the button
            lbl = Label(self.root, text=text, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="gold", fg="navy blue")
            lbl.place(x=x, y=y + 150, width=180, height=30)
            lbl.bind("<Button-1>", lambda e: command())  # Make label clickable

        # Buttons
        create_button(130, 200, r"images\studentDetail.jpg", "Student Details", self.student_Details)
        create_button(390, 200, r"images\Detectfacebutton.jpg", "Face Detector", self.face_Data)
        create_button(650, 200, r"images\attendence.png", "Attendance", self.attendance_Data)
        create_button(910, 200, r"images\photo.png", "Photo Sample", self.open_img)
        create_button(1170, 200, r"images\trainData.jpg", "Train Data", self.train_data)

        # Exit Button
        exit_img = rounded_image(r"images\exit.png", (200, 50), radius=15)
        self.photoimg_exit = ImageTk.PhotoImage(exit_img)
        b6 = Button(self.root, image=self.photoimg_exit, cursor="hand2", command=self.iExit, bd=0)
        b6.place(x=1200, y=600, width=200, height=50)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this page?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    def student_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentDetail(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

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
