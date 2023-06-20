from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recogination import Face_recogination
from attendence import Attendance
from developer import Developer

class Face_Recogination_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogination System")
        self.root.wm_iconbitmap("face.ico")

        img = Image.open(r"Images\1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoImage = ImageTk.PhotoImage(img)

        firstLabel = Label(self.root, image=self.photoImage)
        firstLabel.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"Images\2.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        firstLabel = Label(self.root, image=self.photoImage1)
        firstLabel.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"Images\3.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        firstLabel = Label(self.root, image=self.photoImage2)
        firstLabel.place(x=1000, y=0, width=550, height=130)

       # background Image
        img3 = Image.open(r"Images\4.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bgImage = Label(self.root, image=self.photoImage3)
        bgImage.place(x=0, y=130, width=1520, height=710)

        # Title
        title_lbl = Label(bgImage, text="Face Recognition Attendance System", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Student Button

        img4 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\gettyimages-1022573162.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoImage4 = ImageTk.PhotoImage(img4)

        b1 = Button(bgImage,command=self.student_details, image=self.photoImage4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1 = Button(bgImage,command=self.student_details, text="Student Details", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=200, y=300, width=220, height=40)


        # Detector Button

        img5 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoImage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bgImage, image=self.photoImage5, cursor="hand2",command=self.face_details)
        b1.place(x=500, y=100, width=220, height=220)

        b1 = Button(bgImage, text="Face Detector", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.face_details)
        b1.place(x=500, y=300, width=220, height=40)

        #Attendence face button

        img6 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\report.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoImage6 = ImageTk.PhotoImage(img6)

        b1 = Button(bgImage, image=self.photoImage6, cursor="hand2",command=self.attendance_details)
        b1.place(x=800, y=100, width=220, height=220)

        b1 = Button(bgImage, text="Attendance", cursor="hand2",command=self.attendance_details,font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=800, y=300, width=220, height=40)

        #Help Desk

        
        img7 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoImage7 = ImageTk.PhotoImage(img7)

        b1 = Button(bgImage, image=self.photoImage7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1 = Button(bgImage, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=1100, y=300, width=220, height=40)

        #Train data
        img8 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoImage8 = ImageTk.PhotoImage(img8)

        b1 = Button(bgImage, image=self.photoImage8, cursor="hand2",command=self.train_details)
        b1.place(x=200, y=380, width=220, height=220)

        b1 = Button(bgImage, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.train_details)
        b1.place(x=200, y=580, width=220, height=40)

        #Photo Face 
        img9 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoImage9 = ImageTk.PhotoImage(img9)

        b1 = Button(bgImage, image=self.photoImage9, cursor="hand2",command=self.open_image)
        b1.place(x=500, y=380, width=220, height=220)

        b1 = Button(bgImage, text="Photos",command=self.open_image, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=500, y=580, width=220, height=40)


         #developer 
        img10 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoImage10 = ImageTk.PhotoImage(img10)

        b1 = Button(bgImage, image=self.photoImage10, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1 = Button(bgImage, text="Developers", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.developer_data)
        b1.place(x=800, y=580, width=220, height=40)


         #Exit
        img11 = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoImage11 = ImageTk.PhotoImage(img11)

        b1 = Button(bgImage, image=self.photoImage11, cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1 = Button(bgImage, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.iExit)
        b1.place(x=1100, y=580, width=220, height=40)


    #<=============Open images=============>

    def open_image(self):
        os.startfile("Data") 

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recogniation","Are You Sure to exit ?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return     

        

    #<=================Function buttons==================>
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)    
    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 
    def face_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recogination(self.new_window) 
    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)         
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)         

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recogination_System(root)
    root.mainloop()
