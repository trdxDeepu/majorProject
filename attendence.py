from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog


myData=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800")
        self.root.title("Face Recogination System")


        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name= StringVar()
        self.var_dep = StringVar()
        self.var_time= StringVar()
        self.var_date= StringVar()
        self.var_attendance= StringVar()

        
        img1 = Image.open(r"college_images\smart-attendance.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        firstLabel = Label(self.root, image=self.photoImage1)
        firstLabel.place(x=0, y=0, width=800, height=200)

        img2 = Image.open(r"college_images\IMG_1183_augmented_reality_faces1.jpg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        firstLabel = Label(self.root, image=self.photoImage2)
        firstLabel.place(x=800, y=0, width=800, height=200)

        img3 = Image.open(r"Images\4.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bgImage = Label(self.root, image=self.photoImage3)
        bgImage.place(x=0, y=130, width=1530, height=710)

         # Title
        title_lbl = Label(bgImage, text="Attendance Management System", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # frames for attendance management

        main_frame = Frame(bgImage, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)

        # leftSide Label Frame

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance details", font=(
            "times new roman", 13, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)

        
        img_left = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoImageLeft = ImageTk.PhotoImage(img_left)

        firstLabel = Label(left_frame, image=self.photoImageLeft)
        firstLabel.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(left_frame, bd=2,relief=RIDGE)
        left_inside_frame.place(x=0, y=135, width=720, height=370)
        
        #<========Labels Entry=============>

        AttendanceID_label = Label(left_inside_frame, text="AttendanceID:", font=(
            "times new roman", 13, "bold"), bg="white")
        AttendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id, width=20, font=(
            "courier", 13, "bold"))
        AttendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        
        Roll_label = Label(left_inside_frame, text="Roll:", font=(
            "times new roman", 13, "bold"), bg="white")
        Roll_label.grid(row=0, column=2, padx=4, pady=8, sticky=W)

        Roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_roll , width=20, font=(
            "courier", 13, "bold"))
        Roll_entry.grid(row=0, column=3, padx=8,  sticky=W)

        Name_label = Label(left_inside_frame, text="Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        Name_label.grid(row=1, column=0, padx=4, pady=8, sticky=W)

        Name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_name ,width=20, font=(
            "courier", 13, "bold"))
        Name_entry.grid(row=1, column=1, padx=8,  sticky=W)
        
        Dep_label = Label(left_inside_frame, text="Department:", font=(
            "times new roman", 13, "bold"), bg="white")
        Dep_label.grid(row=1, column=2, padx=4, pady=8, sticky=W)

        Dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_dep ,width=20, font=(
            "courier", 13, "bold"))
        Dep_entry.grid(row=1, column=3, padx=8,  sticky=W)
      
        Time_label = Label(left_inside_frame, text="Time:", font=(
            "times new roman", 13, "bold"), bg="white")
        Time_label.grid(row=2, column=0, padx=4, pady=8, sticky=W)

        Time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_time , width=20, font=(
            "courier", 13, "bold"))
        Time_entry.grid(row=2, column=1, padx=8,  sticky=W)
       
        Date_label = Label(left_inside_frame, text="Date:", font=(
            "times new roman", 13, "bold"), bg="white")
        Date_label.grid(row=2, column=2, padx=4, pady=8, sticky=W)

        Date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_date ,width=20, font=(
            "courier", 13, "bold"))
        Date_entry.grid(row=2, column=3, padx=8,  sticky=W)

        Attendance_label = Label(left_inside_frame, text="Date:", font=(
            "times new roman", 13, "bold"), bg="white")
        Attendance_label.grid(row=2, column=2, padx=4, pady=8, sticky=W)

        Attendance_Status_label = Label(left_inside_frame, text="Attendance Status:", font=(
            "times new roman", 13, "bold"), bg="white")
        Attendance_Status_label.grid(row=3, column=0, padx=4, pady=8, sticky=W)

        self.atten_Status=ttk.Combobox(left_inside_frame,textvariable=self.var_attendance,width=20,font=(
            "times new roman", 13, "bold"),state="readonly")
        self.atten_Status["values"] = ["Status","Present","Absent"]
        self.atten_Status.grid(row=3,column=1,pady=8)
        self.atten_Status.current(0)

        
        buttonFrame = Frame(left_inside_frame,
                            bd=2, relief=RIDGE, bg="white")
        buttonFrame.place(x=0, y=300, width=715, height=37)

        save_btn = Button(buttonFrame,  text="Import CSV",command=self.import_csv,font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0)

        update_btn = Button(buttonFrame,  text="Export CSV", command=self.export_csv,font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(buttonFrame,text="Update", font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(buttonFrame, text="Reset", command=self.reset_data ,font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3)

        

        # right frame

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text=" Attendance details", font=(
            "times new roman", 13, "bold"))
        right_frame.place(x=780, y=10, width=720, height=580)

        tableFrame = Frame(right_frame,
                            bd=2, relief=RIDGE, bg="white")
        tableFrame.place(x=5, y=5, width=680, height=445)

        #<===========Scrollbar and table =============>

                # scrollbar
        scroll_x = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableFrame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        
        self.AttendanceReportTable = ttk.Treeview(tableFrame, columns=("id","roll","name","dep","time","date","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dep", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Status")
        self.AttendanceReportTable["show"] = "headings"


        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("dep", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
     
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #<======Fetch Data ================>

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def import_csv(self):
        global myData
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All files","*.*")),parent=self.root)
        with open(filename) as myFile:
            csvread=csv.reader(myFile,delimiter=",")
            for i in csvread:
                   myData.append(i)
            self.fetch_data(myData)   

    def export_csv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            
            filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All files","*.*")),parent=self.root)
            with open(filename,mode="w",newline="\n") as myFile:
                exp_write = csv.writer(myFile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your Data exported to"+os.path.basename(filename)+"Successfull",parent=self.root)    
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])        
        self.var_roll.set(rows[1])        
        self.var_name.set(rows[2])        
        self.var_dep.set(rows[3])        
        self.var_time.set(rows[4])        
        self.var_date.set(rows[5])        
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_id.set("")        
        self.var_roll.set("")        
        self.var_name.set("")        
        self.var_dep.set("")        
        self.var_time.set("")        
        self.var_date.set("")        
        self.var_attendance.set("Status")



              




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
