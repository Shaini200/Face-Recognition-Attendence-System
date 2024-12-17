from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1700x900+0+0")
        self.root.title("Train Data")

        # Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Arial Rounded MT Bold", 25, "bold"), bg="gray", fg="navy blue")
        title_lbl.place(x=0, y=20, width=1700, height=70)

        # Image label
        img1 = Image.open(r"images\TrainData1.jpg")
        img1 = img1.resize((1700, 700), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=90, width=1700, height=700)

        # Train data button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classfier, cursor="hand2", font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=1000, y=600, width=300, height=50)

    def train_classfier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            imageNp = np.array(img, 'uint8')  # uint8 is the data type
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to break
                break

        ids = np.array(ids)

        # Train classifier & save the model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("clf.xml")  # Save the trained classifier

        cv2.destroyAllWindows()  # Close the OpenCV window showing the images during training
        messagebox.showinfo("Result", "Training dataset completed!!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
