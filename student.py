from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800")
        self.root.title("Face Recogination System")

     # <======Variables======>

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\smart-attendance.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoImage = ImageTk.PhotoImage(img)

        firstLabel = Label(self.root, image=self.photoImage)
        firstLabel.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"Images\8.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        firstLabel = Label(self.root, image=self.photoImage1)
        firstLabel.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"Images\8.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        firstLabel = Label(self.root, image=self.photoImage2)
        firstLabel.place(x=1000, y=0, width=550, height=130)

        img3 = Image.open(r"Images\4.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bgImage = Label(self.root, image=self.photoImage3)
        bgImage.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bgImage, text="Student Management System", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # frames for student management

        main_frame = Frame(bgImage, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)

        # leftSide Label Frame

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 13, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoImageLeft = ImageTk.PhotoImage(img_left)

        firstLabel = Label(left_frame, image=self.photoImageLeft)
        firstLabel.place(x=5, y=0, width=720, height=130)

        # current Course

        Cuurent_course_frame_Label = LabelFrame(
            left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        Cuurent_course_frame_Label.place(x=5, y=135, width=720, height=150)

        # departtment label

        dep_label = Label(Cuurent_course_frame_Label, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=3)

        dep_combo = ttk.Combobox(Cuurent_course_frame_Label, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Electronics and Communication",
                               "Information and Technology", "Mechanical Engineering", "Electrical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course Label

        Course_label = Label(Cuurent_course_frame_Label, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        Course_label.grid(row=0, column=2, padx=10, sticky=W)

        Course_combo = ttk.Combobox(Cuurent_course_frame_Label, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Course_combo["values"] = (
            "Select Course", "CS", "ECE", "EE", "ME", "IT")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year

        Year_label = Label(Cuurent_course_frame_Label, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=2, sticky=W)

        Year_combo = ttk.Combobox(Cuurent_course_frame_Label, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        Year_combo["values"] = ("Select Year", "2014-2018", "2015-2019",
                                "2016-2020", "2017-2021", "2018-2022", "2019-2023", "2020-2024")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester

        semester_label = Label(Cuurent_course_frame_Label, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(Cuurent_course_frame_Label, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select Semester", "1st Sem", "2nd Sem",
                                    "3rd Sem", "4th Sem", "5th Sem", "6th Sem", "7th Sem", "8th Sem")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        class_Student_frame_Label = LabelFrame(
            left_frame, bd=2, relief=RIDGE, text=" Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame_Label.place(x=5, y=250, width=720, height=300)

        student_label = Label(class_Student_frame_Label, text="StudentID:", font=(
            "times new roman", 13, "bold"), bg="white")
        student_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Student Entry

        studentID_entry = ttk.Entry(class_Student_frame_Label, textvariable=self.var_std_id, width=20, font=(
            "courier", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name

        studentName_label = Label(class_Student_frame_Label, text="Student Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame_Label, textvariable=self.var_std_name, width=20, font=(
            "courier", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        class_div_label = Label(class_Student_frame_Label, text="Class Division : ", font=(
            "times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(class_Student_frame_Label, textvariable=self.var_div, font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        class_div_combo["values"] = (
            "Select division", "ECE 1", "ECE 2", "CSE ")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll no
        roll_No_label = Label(class_Student_frame_Label, text="Roll No :", font=(
            "times new roman", 13, "bold"), bg="white")
        roll_No_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_No_entry = ttk.Entry(class_Student_frame_Label, width=20, textvariable=self.var_roll, font=(
            "courier", 13, "bold"))
        roll_No_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # gender

        gender_label = Label(class_Student_frame_Label, text="Gender:", font=(
            "times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame_Label, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # date of birth

        dob_label = Label(class_Student_frame_Label, text="DOB:", font=(
            "times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame_Label, textvariable=self.var_dob, width=20, font=(
            "courier", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email

        email_label = Label(class_Student_frame_Label, text="Email:", font=(
            "times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame_Label, width=20, textvariable=self.var_email, font=(
            "courier", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phoneNo

        phone_label = Label(class_Student_frame_Label, text="Phone :", font=(
            "times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame_Label, width=20, textvariable=self.var_phone, font=(
            "courier", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address

        address_label = Label(class_Student_frame_Label, text="Address :", font=(
            "times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame_Label, width=20, textvariable=self.var_address, font=(
            "courier", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name

        teacher_label = Label(class_Student_frame_Label, text="Teacher Name :", font=(
            "times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame_Label, textvariable=self.var_teacher, width=20, font=(
            "courier", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        self.var_radio1 = StringVar()
        radioButton1 = ttk.Radiobutton(
            class_Student_frame_Label, variable=self.var_radio1, text="Take a photo sample", value="yes")
        radioButton1.grid(row=5, column=0)

        self.var_radio2 = StringVar()
        radioButton2 = ttk.Radiobutton(
            class_Student_frame_Label, variable=self.var_radio2, text="No photo sample", value="No",)
        radioButton2.grid(row=5, column=3)

        # button Frame

        buttonFrame = Frame(class_Student_frame_Label,
                            bd=2, relief=RIDGE, bg="white")
        buttonFrame.place(x=0, y=200, width=715, height=70)

        save_btn = Button(buttonFrame, command=self.add_Data, text="Save", font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0)

        update_btn = Button(buttonFrame, command=self.update_fun, text="Update", font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(buttonFrame, command=self.delete_data, text="Delete", font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(buttonFrame, text="Reset", command=self.Reset_fun, font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3)

        buttonFrame1 = Frame(class_Student_frame_Label,
                             bd=2, relief=RIDGE, bg="white")
        buttonFrame1.place(x=0, y=235, width=715, height=35)

        photo_sample_btn = Button(buttonFrame1,command=self.generate_dataset ,text="Take Photo Samaple", font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=35)
        photo_sample_btn.grid(row=0, column=0)

        update_photo_sample_btn = Button(buttonFrame1, text="Update Photo Samaple", font=(
            "courier", 13, "bold"), bg="blue", fg="white", width=35)
        update_photo_sample_btn.grid(row=0, column=1)

        # right frame

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 13, "bold"))
        right_frame.place(x=780, y=10, width=720, height=580)

        img_right = Image.open(
            r"C:\Users\Depuj\Downloads\1628243597666college-images\college_images\gettyimages-1022573162.jpg")
        img_right = img_right.resize((760, 130), Image.LANCZOS)
        self.photoImageRight = ImageTk.PhotoImage(img_right)

        firstLabel = Label(right_frame, image=self.photoImageRight)
        firstLabel.place(x=5, y=0, width=720, height=130)

        # <===========Seacrh Sytem===========>

        search_frame_Label = LabelFrame(
            right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame_Label.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame_Label, text="Serch by:", font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame_Label, font=(
            "times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "RollNo", "Phone", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame_Label, width=14, font=(
            "courier", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame_Label, text="Search", font=(
            "courier", 12, "bold"), bg="blue", fg="white", width=12)
        search_btn.grid(row=0, column=3,)

        showAll_btn = Button(search_frame_Label, text="Show All", font=(
            "courier", 12, "bold"), bg="blue", fg="white", width=12)
        showAll_btn.grid(row=0, column=4, padx=2)

        # <===================Table Frame=================>

        table_frame_Label = Frame(
            right_frame, bd=2, relief=RIDGE)
        table_frame_Label.place(x=5, y=210, width=700, height=350)

        # scrollbar
        scroll_x = ttk.Scrollbar(table_frame_Label, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame_Label, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame_Label, columns=("dep", "course", "year", "sem", "id", "name", "roll", "gender", "div", "email", "phone", "dob",
                                                                      "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_Data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Singhdepu@1", database="face_detection")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO Student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_div.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details have been added successfully", parent=self.root)
            except mysql.connector.Error as e:
                messagebox.showerror(
                    "Error", f"Database Error: {str(e)}", parent=self.root)
       # <===============Fetch Data ==================>

    def fetch_data(self):

        conn = mysql.connector.connect(
            host="localhost", username="root", password="Singhdepu@1", database="face_detection")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(
                *self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # <=========update function==============>
    def get_cursor(self, event=""):

        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_div.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_dob.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # <============Update function=============>

    def update_fun(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do You Want to Update the details?", parent=self.root)
                if Update > 0:

                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Singhdepu@1", database="face_detection")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Division=%s,Email=%s,Phone=%s,DOB=%s,Address=%s,Teacher=%s,Photos=%s where Studen_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_div.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get(),
                    ))

                else:

                    if not Update:

                        return
                messagebox.showinfo(
                    "Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

        # <============Delete Function===============>

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required! ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete details", "Do you want to delete the student details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Singhdepu@1", database="face_detection")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Studen_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:

                    if not delete:

                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully Deleted the data of student")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

    # <==========Reset function=================>

    def Reset_fun(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_div.set("Select Division")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    

            

    # <=======Implementing the openCV===========>
    # <=======Generate dataset using openCv========>

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Singhdepu@1", database="face_detection")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1

                my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Division=%s,Email=%s,Phone=%s,DOB=%s,Address=%s,Teacher=%s,Photos=%s where Studen_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_div.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1,
                ))
                conn.commit()
                self.fetch_data()
                self.Reset_fun()
                conn.close()
                
                #==========loading frontal face ==========

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                     
                     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(gray, 1.1, 5)

                     for (x, y, w, h) in faces:

                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                     
                     
                cap = cv2.VideoCapture(0)
                img_id=0

                while True:
                    ret,my_frame=cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(550,550))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)    
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed successfully")


            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)
  

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
