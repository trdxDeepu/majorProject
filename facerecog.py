from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_recogination:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800")
        self.root.title("Face Recogination System")

    # <=====Title==========>

        title_lbl = Label(self.root, text="Face Recogination", font=(
            "times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoImageTop = ImageTk.PhotoImage(img_top)

        firstLabel = Label(self.root, image=self.photoImageTop)
        firstLabel.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(
            r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoImagebottom = ImageTk.PhotoImage(img_bottom)

        firstLabel = Label(self.root, image=self.photoImagebottom)
        firstLabel.place(x=650, y=55, width=950, height=700)

        # button
        btn1 = Button(firstLabel, text="Face Recognination", cursor="hand2", command=self.face_recog, font=(
            "times new roman", 16, "bold"), bg="darkgreen", fg="white")
        btn1.place(x=365, y=620, width=200, height=40)

    #<====================Attendence System ==================>

    def mark_attendence(self,i,r,n,d):
        with open("Attendence.csv","r+",newline="\n") as f :
            my_Data_List=f.readlines()
            name_list=[]
            for line in my_Data_List:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list))and((r not in name_list)) and ((n not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                dy=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dt},{dy},Present")


   


    # <==============Face Recogination=============>

    def face_recog(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
 
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Singhdepu@1", database="face_detection")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Studen_id="+str(id))
                n = my_cursor.fetchone()

                n = "+".join(str(i) for i in n)

                my_cursor.execute( "select Roll from student where Studen_id="+str(id))
                r = my_cursor.fetchone()

                r = "+".join(str(i) for i in r)

                my_cursor.execute("select Dep from student where Studen_id="+str(id))
                d = my_cursor.fetchone()

                d = "+".join(str(i) for i in d)
                
                my_cursor.execute("select Studen_id from student where Studen_id="+str(id))
                t = my_cursor.fetchone()

                t = "+".join(str(i) for i in t)

                if confidence > 77:
                    cv2.putText(img, f"ID:{t}", (x, y-85), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                    self.mark_attendence(t,r,n,d)

                else:
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "KON HO AAP MAHAJAN?", (x, y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                coord = [x, y, w, h]

            return coord

        def recogonize(img, clf, faceCascade):
            coord= draw_boundary(img, faceCascade, 1.1,10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recogonize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognitation", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk() 
    obj = Face_recogination(root)
    root.mainloop()
