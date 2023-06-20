from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800")
        self.root.title("Face Recogination System")
        self.root.wm_iconbitmap("face.ico")

    # <=====Title==========>

        title_lbl = Label(self.root, text="Train Data Set", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        button = Button(self.root, text="Exit", font=("times new roman", 16, "bold"), command=root.destroy, relief=FLAT, bg="#4caf50", fg="white", activebackground="#45a049", activeforeground="white", width=10, borderwidth=2, highlightthickness=0)
        button.place(x=1360, y=11)

     
        

        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoImageTop = ImageTk.PhotoImage(img_top)

        firstLabel = Label(self.root, image=self.photoImageTop)
        firstLabel.place(x=0, y=55, width=1530, height=325)

        btn1 = Button(self.root,command=self.train_classifier ,text="Train Data", font=(
            "Oswald", 30, "bold"), bg="darkblue", fg="white", width=20)
        btn1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(
            r"college_images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoImagebottom = ImageTk.PhotoImage(img_bottom)

        firstLabel = Label(self.root, image=self.photoImagebottom)
        firstLabel.place(x=0, y=440, width=1530, height=325)

        # <========LBPH (Local binary pattern histogram )Algorithm
        # LBP = s a simple yet very efficient texture operator which labels the pixels of an image by 
        # thresholding the neighborhood of each pixel and considers the result as a binary number.

    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids=[]
        
        for image in path:
            #converting to grayscale image
            img=Image.open(image).convert("L")
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1]) 

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #training the classifier and save 

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!") 

        

     



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
