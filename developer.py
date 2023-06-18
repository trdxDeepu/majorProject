from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog




class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800")
        self.root.title("Face Recogination System")

        
        title_lbl = Label(self.root, text="Developer", font=(
            "times new roman", 35, "bold"),  fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoImageTop = ImageTk.PhotoImage(img_top)

        firstLabel = Label(self.root, image=self.photoImageTop)
        firstLabel.place(x=0, y=55, width=1530, height=720)

        
        main_frame = Frame(firstLabel, bd=2)
        main_frame.place(x=1000, y=10, width=500, height=600)

        img_top = Image.open(r"college_images\Bill_Gates.jpg")
        img_top = img_top.resize((200, 200), Image.LANCZOS)
        self.photoImageTop1 = ImageTk.PhotoImage(img_top)

        firstLabel = Label(main_frame, image=self.photoImageTop1)
        firstLabel.place(x=300, y=0, width=200, height=200)

        dev_lbl = Label(main_frame, text="Developer info", font=(
            "times new roman", 30, "bold"), bg="white", fg="darkgreen")
        dev_lbl.place(x=0, y=5)
        dev1_lbl = Label(main_frame, text="Sandeep Gautam,Mahesh,Deependra Singh", font=(
            "times new roman", 19, "bold"), bg="white", fg="black")
        dev1_lbl.place(x=0,y=240)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()