from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1700x900+0+0")
        self.root.title("Face Detector")

        # title
        title_lbl = Label(self.root, text="FACE  DETECTION", font=("Arial Rounded MT Bold", 30, "bold"), bg="gray", fg="navy blue")
        title_lbl.place(x=0, y=20, width=1700, height=70)

        # Image
        img1 = Image.open(r"images\detection.jpg")
        img1 = img1.resize((1700, 700), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=90, width=1700, height=700)

        # button
        b1_1 = Button(self.root, text="Face Detection", cursor="hand2", font=("times new roman", 20, "bold"), bg="red", fg="white", command=self.face_detect)
        b1_1.place(x=430, y=375, width=200, height=100)

    # ------------ attendance ------------
    def mark_attendance(self, i, n, s, r):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

            if i not in name_list and n not in name_list and s not in name_list and r not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{s},{r},{dtString},{d1},Present")

    # ------------- face detection -------------
    def face_detect(self):
       
        def draw_boundray(img, classifier, scaleFactor, minNeighbor, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbor)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Shaini123#", database="face_recognition"
                )
                my_cursor = conn.cursor()

                my_cursor.execute(f"SELECT Student_ID FROM student WHERE Student_ID = {str(id)}")
                result = my_cursor.fetchone()
                i = result[0] if result else "Unknown"

                my_cursor.execute(f"SELECT Name FROM student WHERE Student_ID = {str(id)}")
                result = my_cursor.fetchone()
                n = result[0] if result else "Unknown"

                my_cursor.execute(f"SELECT Grade FROM student WHERE Student_ID = {str(id)}")
                result = my_cursor.fetchone()
                s = result[0] if result else "Unknown"

                my_cursor.execute(f"SELECT Subject FROM student WHERE Student_ID = {str(id)}")
                result = my_cursor.fetchone()
                r = result[0] if result else "Unknown"


                
                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Grade: {s}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Subject: {r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, n, s, r)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognition(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if faceCascade.empty():
            print("Error: Haar cascade file not found.")
            return
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists("clf.xml"):
            print("Error: Trained model file not found.")
            return
        clf.read("clf.xml")

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            print("Error: Unable to access the webcam")
            return

        while True:
            ret, img = video_cap.read()
            if not ret or img is None:
                print("Warning: Failed to capture frame. Skipping...")
                continue  # Skip this iteration

            img = recognition(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Detector(root)
    root.mainloop()
