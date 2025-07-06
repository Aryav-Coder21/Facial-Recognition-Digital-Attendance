from ast import Del, Delete
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import title, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# ==============Student Main class start=====================


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Student's Details")
        self.root.wm_iconbitmap("face.ico")

        # ==============all database fucntion variables code start============================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.va_sid = StringVar()
        self.var_enroll = StringVar()
        self.var_s_name = StringVar()
        self.var_f_name = StringVar()
        self.var_c_no = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_h_name = StringVar()
        # ==============all database fucntion variables code end==============================

        # ===========first row of header start===============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\s1s.jpg")
        img = img.resize((500, 120), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=120)
        # Image second.
        img1 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\s2s.jpg")
        img1 = img1.resize((500, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=120)
        # Image third.
        img2 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\s3s.jpg")
        img2 = img2.resize((520, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=520, height=120)
        # ===========first row of header end===============================

        # ============background image start===============================
        bgimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\bg im.jpg")
        bgimg = bgimg.resize((1520, 690), Image.ANTIALIAS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        b_img = Label(self.root, image=self.photobgimg)
        b_img.place(x=0, y=120, width=1520, height=690)
        # ============background image end=================================
        # ===========second row of header start===============================
        title_lbl = Label(b_img, text="STUDENT'S DETAILS", font=(
            "times new roman", 25, "bold"), bg="white", fg="gray")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ================back button code start============================
        b1_1 = Button(title_lbl, text="BACK", command=self.ba , cursor="hand2", font=(
            "cursive", 10, "bold"), bg="white", fg="blue")
        b1_1.place(x=1400, y=5, width=100, height=30)
        # ================back button code end==============================
        # ===========second row of header end===============================

        # ====================main student details background code start==================
        main_frame = Frame(b_img, bd=2)
        main_frame.place(x=20, y=45, width=1480, height=620)
        # ====================main student details background code end====================
        # ====================left label form header,border and background code start==================================
        left_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE,
                                text="Students Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=600, height=600)
        # ====================left form header image code start=========================
        lsfimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\sd.jpg")
        lsfimg = lsfimg.resize((590, 65), Image.ANTIALIAS)
        self.photolsfimg = ImageTk.PhotoImage(lsfimg)

        f_lbl = Label(left_frame, image=self.photolsfimg)
        f_lbl.place(x=5, y=0, width=590, height=65)
        # ====================left form header image code end=========================
        # ====================left label from code start==============================
        # ===============current course infomation label code start===================
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=65, width=585, height=120)
        # ===============department label code start===========================
        d_label = Label(current_course_frame, text="Department",
                        font=("times new roman", 12, "bold"), bg="white")
        d_label.grid(row=0, column=0, sticky=W)

        d_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=20, state="readonly")
        d_combo["values"] = ("Select Your Department",
                             "Infomation Technology", "Computer Science", "Electronics")
        d_combo.current(0)
        d_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # ===============department label code end===========================
        # ===============course label code start=============================
        c_label = Label(current_course_frame, text="Courses",
                        font=("times new roman", 12, "bold"), bg="white")
        c_label.grid(row=0, column=2, sticky=W)

        c_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=20, state="readonly")
        c_combo["values"] = ("Select Your Course", "IT", "CSE", "EE")
        c_combo.current(0)
        c_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        # ===============course label code end=============================
        # ===============year label code start===========================
        y_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        y_label.grid(row=1, column=0, sticky=W, pady=5)

        y_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=20, state="readonly")
        y_combo["values"] = ("Select Your Year",
                             "2021-22", "2022-23", "2023-24")
        y_combo.current(0)
        y_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        # ===============year label code end=============================
        # ===============Semerter label code start===========================
        s_label = Label(current_course_frame, text="Semester",
                        font=("times new roman", 12, "bold"), bg="white")
        s_label.grid(row=1, column=2, sticky=W, pady=5)

        s_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), width=20, state="readonly")
        s_combo["values"] = ("Select Your Semester", "1st Sem",
                             "2nd Sem", "3rd sem", "4th sem", "5th sem", "6th sem")
        s_combo.current(0)
        s_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # ===============semester label code end=============================
        # ===============current course infomation label code end===================
        # ===============Class students infomation label code start===================
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student's Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=185, width=585, height=320)
        # ===============Sudentid label code start===========================
        enroll_label = Label(class_student_frame, text="ID:", font=(
            "times new roman", 12, "bold"), bg="white")
        enroll_label.grid(row=0, column=0, sticky=W, padx=5)
        enroll_entry = ttk.Entry(
            class_student_frame, textvariable=self.va_sid, width=20, font=("times new roman", 12, "bold"))
        enroll_entry.grid(row=0, column=1, sticky=W)
        # ===============Sudentid label code end=============================
        # ===============Sudentenroll label code start===========================
        enroll_label = Label(class_student_frame, text="Enrollment no:", font=(
            "times new roman", 12, "bold"), bg="white")
        enroll_label.grid(row=0, column=2, sticky=W, padx=5)
        enroll_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_enroll, width=20, font=("times new roman", 12, "bold"))
        enroll_entry.grid(row=0, column=3, sticky=W)
        # ===============Sudentenroll label code end=============================
        # ===============Sudentname label code start===========================
        sn_label = Label(class_student_frame, text="Sudent Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        sn_label.grid(row=1, column=0, sticky=W, padx=5)
        studentname_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_s_name, width=20, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=1, column=1, sticky=W)
        # ===============Sudentname label code end=============================
        # ===============fathername label code start===========================
        fn_label = Label(class_student_frame, text="Father Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        fn_label.grid(row=1, column=2, sticky=W, padx=5, pady=10)
        fathername_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_f_name, width=20, font=("times new roman", 12, "bold"))
        fathername_entry.grid(row=1, column=3, sticky=W)
        # ===============fathername label code end=============================
        # ===============mobile label code start===========================
        mn_label = Label(class_student_frame, text="Contact no:", font=(
            "times new roman", 12, "bold"), bg="white")
        mn_label.grid(row=2, column=0, sticky=W, padx=5, pady=10)
        Mobileno_entry = ttk.Entry(class_student_frame, textvariable=self.var_c_no, width=20, font=(
            "times new roman", 12, "bold"))
        Mobileno_entry.grid(row=2, column=1, sticky=W)
        # ===============mobile label code end=============================
        # ===============Gender label code start===========================
        gn_label = Label(class_student_frame, text="Gender:",
                         font=("times new roman", 12, "bold"), bg="white")
        gn_label.grid(row=2, column=2, sticky=W, padx=5, pady=10)
        # gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=(
        #    "times new roman", 12, "bold"))
        #gender_entry.grid(row=2, column=1, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=8, state="readonly")
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)
        # ===============Gender label code end=============================
        # ===============Email label code start===========================
        en_label = Label(class_student_frame, text="E-mail:",
                         font=("times new roman", 12, "bold"), bg="white")
        en_label.grid(row=3, column=0, sticky=W, padx=5, pady=10)
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, sticky=W)
        # ===============Email label code end=============================
        # ===============hod label code start===========================
        hod_label = Label(class_student_frame, text="HOD Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        hod_label.grid(row=3, column=2, sticky=W, padx=5, pady=10)
        HOD_entry = ttk.Entry(class_student_frame, textvariable=self.var_h_name, width=20, font=(
            "times new roman", 12, "bold"))
        HOD_entry.grid(row=3, column=3, sticky=W)
        # ===============hod label code end=============================
        # ===============dob label code start===========================
        dob_label = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=4, column=0, sticky=W, padx=5, pady=10)
        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        DOB_entry.grid(row=4, column=1, sticky=W)
        # ===============dob label code end=============================
        # ================radio buttons code start======================
        self.var_r1 = StringVar()
        rabtn1 = ttk.Radiobutton(
            class_student_frame, text="Take a Photo Sample", value="Yes", variable=self.var_r1)
        rabtn1.grid(row=6, column=0)

        rabtn2 = ttk.Radiobutton(
            class_student_frame, text="No Take a Photo Sample", value="No", variable=self.var_r1)
        rabtn2.grid(row=6, column=1)
        # ================radio buttons code end========================
        # ================buttons frame code start======================
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=227, width=580, height=37)
        # =================save btn code start=======================
        save_btn = Button(btn_frame, text="Submit", command=self.add_data, font=(
            "times new roman", 12, "bold"), bg="green", fg="lightgreen", width=15)
        save_btn.grid(row=0, column=0)
        # =================save btn code end=========================
        # =================update btn code start=======================
        upd_btn = Button(btn_frame, text="Update Data", command=self.up_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="lightblue", width=15)
        upd_btn.grid(row=0, column=1)
        # =================update btn code end=========================
        # =================delete btn code start=======================
        del_btn = Button(btn_frame, text="Delete Data", command=self.del_data, font=(
            "times new roman", 12, "bold"), bg="red", fg="white", width=15)
        del_btn.grid(row=0, column=2)
        # =================delete btn code end=========================
        # =================reset btn code start=======================
        re_btn = Button(btn_frame, text="Reset Form Data", command=self.re_data, font=(
            "times new roman", 12, "bold"), bg="orange", fg="darkred", width=15)
        re_btn.grid(row=0, column=3)
        # =================reset btn code end============
        # ================buttons frame code end=====================================
        # ================second buttons frame code start=====================================
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=259, width=580, height=37)
        # =================photo sam btn code start=======================
        tps_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, font=(
            "times new roman", 12, "bold"), bg="orange", fg="darkred", width=33)
        tps_btn.grid(row=0, column=0)
        # =================photo sam btn code end=========================
        # =================upphoto sam btn code start=======================
        utps_btn = Button(btn_frame1, text="Update Photo Sample", font=(
            "times new roman", 12, "bold"), bg="orange", fg="darkred", width=33)
        utps_btn.grid(row=0, column=1)
        # =================upphoto sam btn code end=========================
        # ================second buttons frame code end=====================================

        # ===============Class students infomation label code end===================

        # ====================left label from code end================================

        # ====================left label form header,border and background code end==================================
        # ====================right label form code start==================================
        right_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE,
                                 text="Student's Details Search System", font=("times new roman", 12, "bold"))
        right_frame.place(x=620, y=10, width=840, height=600)

        # ====================right form header image code start=========================
        rsfimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\sdd.jpg")
        rsfimg = rsfimg.resize((840, 65), Image.ANTIALIAS)
        self.photorsfimg = ImageTk.PhotoImage(rsfimg)

        f_lbl = Label(right_frame, image=self.photorsfimg)
        f_lbl.place(x=5, y=0, width=820, height=65)
        # ====================right form header image code end=========================
        # ========================students data search system code start==================
        # ===============search system frame code start===================
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Student's Data Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=60, width=820, height=70)
        # =================search bar code start==============================
        searchbar_label = Label(search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="aqua", fg="white")
        searchbar_label.grid(row=0, column=0, sticky=W, padx=5)

        searchbar_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), width=10, state="readonly")
        searchbar_combo["values"] = (
            "Select", "Enrollment", "Student Name", "E-mail", "Contact No:")
        searchbar_combo.current(0)
        searchbar_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        HODsearchb_entry = ttk.Entry(
            search_frame, width=20, font=("times new roman", 12, "bold"))
        HODsearchb_entry.grid(row=0, column=2, sticky=W)

        se_btn = Button(search_frame, text="Search", font=(
            "times new roman", 12, "bold"), bg="orange", fg="darkred", width=13)
        se_btn.grid(row=0, column=3, padx=4)

        show_btn = Button(search_frame, text="Show All", font=(
            "times new roman", 12, "bold"), bg="orange", fg="darkred", width=13)
        show_btn.grid(row=0, column=4)
        # ================search bar code end=================================
        # ===============search system frame code start===================
        # =================database table frame code start==============================
        dtbl_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        dtbl_frame.place(x=5, y=133, width=820, height=440)

        scroll_x = ttk.Scrollbar(dtbl_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(dtbl_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(dtbl_frame, columns=("dep", "course", "year", "sem", "sid", "enroll", "s_name", "f_name",
                                          "c_no", "gender", "email", "dob", "h_name", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("sid", text="SID")
        self.student_table.heading("enroll", text="Enrollment")
        self.student_table.heading("s_name", text="Student Name")
        self.student_table.heading("f_name", text="Father Name")
        self.student_table.heading("c_no", text="Contact No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="E-mail")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("h_name", text="HOD Name")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("sid", width=100)
        self.student_table.column("enroll", width=100)
        self.student_table.column("s_name", width=100)
        self.student_table.column("f_name", width=100)
        self.student_table.column("c_no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("h_name", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_curs)
        self.fetch_data()

        # ===============database table frame code end===================
        # ========================students data search system code end====================
        # ====================right label form code end==================================
    # ====================data save to database function code start=======================
    def add_data(self):
        if self.var_dep.get() == "Select Your Department" or self.var_s_name.get() == " " or self.var_enroll.get() == " ":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="myminorproject")
                m_cur = conn.cursor()
                m_cur.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.va_sid.get(), self.var_enroll.get(
                ), self.var_s_name.get(), self.var_f_name.get(), self.var_c_no.get(), self.var_gender.get(), self.var_email.get(), self.var_dob.get(), self.var_h_name.get(), self.var_r1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Your Details Has Been Successfully Submitted", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ====================data save to database function code end=========================
    # ====================data display to software window code start======================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="myminorproject")
        m_cur = conn.cursor()
        m_cur.execute("select * from student_details")
        da = m_cur.fetchall()

        if len(da) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in da:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # ====================data display to software window code end========================
    # ====================get cursor code start===========================================

    def get_curs(self, event=""):
        curso_focus = self.student_table.focus()
        cont = self.student_table.item(curso_focus)
        dat = cont["values"]

        self.var_dep.set(dat[0]),
        self.var_course.set(dat[1]),
        self.var_year.set(dat[2]),
        self.var_sem.set(dat[3]),
        self.va_sid.set(dat[4]),
        self.var_enroll.set(dat[5]),
        self.var_s_name.set(dat[6]),
        self.var_f_name.set(dat[7]),
        self.var_c_no.set(dat[8]),
        self.var_gender.set(dat[9]),
        self.var_email.set(dat[10]),
        self.var_dob.set(dat[11]),
        self.var_h_name.set(dat[12]),
        self.var_r1.set(dat[13])
    # ====================get cursor code end=============================================
    # ====================details update function code start==============================

    def up_data(self):
        if self.var_dep.get() == "Select Your Department" or self.var_s_name.get() == " " or self.var_enroll.get() == " ":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update your details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="1234", database="myminorproject")
                    m_cur = conn.cursor()
                    m_cur.execute("update student_details set dep=%s,course=%s,year=%s,sem=%s,s_name=%s,f_name=%s,c_no=%s,gender=%s,email=%s,dob=%s,h_name=%s,photo=%s,enroll=%s where sid=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(
                    ), self.var_sem.get(), self.var_enroll.get(), self.var_s_name.get(), self.var_f_name.get(), self.var_c_no.get(), self.var_gender.get(), self.var_email.get(), self.var_dob.get(), self.var_h_name.get(), self.var_r1.get(), self.va_sid.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Your Details are Successfully Updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)
    # ====================details update function code end================================
    # ====================delete data function code start=================================

    def del_data(self):
        if self.var_enroll.get() == " ":
            messagebox.showerror(
                "Error", "Student enrollment no must be required", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno(
                    "Student Detail Delete Page", "Do you want delete your details", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="myminorproject")
                    m_cur = conn.cursor()
                    sql = "delete from student_details where enroll=%s"
                    val = (self.var_enroll.get(),)
                    m_cur.execute(sql, val)
                else:
                    if not Delete:
                        return
                messagebox.showinfo(
                    "Success", "Your Details are Successfully Deleted", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)
    # ====================delete data function code end===================================
    # ====================reset form data function code start=============================

    def re_data(self):
        self.var_dep.set("Select Your Department")
        self.var_course.set("Select Your Course")
        self.var_year.set("Select Your Year")
        self.var_sem.set("Select Your Semester")
        self.va_sid.set("")
        self.var_enroll.set("")
        self.var_s_name.set("")
        self.var_f_name.set("")
        self.var_c_no.set("")
        self.var_gender.set("Male")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_h_name.set("")
        self.var_r1.set("")
    # ====================reset form data function code end===============================
    # ====================Generate data set or Take photo samples code start=========================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Your Department" or self.var_s_name.get() == " " or self.var_enroll.get() == " ":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="myminorproject")
                m_cur = conn.cursor()
                m_cur.execute("select * from student_details")
                myres = m_cur.fetchall()
                id = 0
                for x in myres:
                    id += 1
                m_cur.execute("update student_details set dep=%s,course=%s,year=%s,sem=%s,s_name=%s,f_name=%s,c_no=%s,gender=%s,email=%s,dob=%s,h_name=%s,photo=%s,enroll=%s where sid=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(
                ), self.var_sem.get(), self.var_enroll.get(), self.var_s_name.get(), self.var_f_name.get(), self.var_c_no.get(), self.var_gender.get(), self.var_email.get(), self.var_dob.get(), self.var_h_name.get(), self.var_r1.get(), self.va_sid.get() == id+1))
                conn.commit()
                self.fetch_data()
                self.re_data()
                conn.close()
                # ================ Load predifiend data on face frantals from dlib/open[cv] code start=======================
                face_classified = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def fac_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classified.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # minimun neighbor=5
                    for (x, y, w, h) in faces:
                        fac_cropped = img[y:y+h, x:x+w]
                        return fac_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, m_frame = cap.read()
                    if fac_cropped(m_frame) is not None:
                        img_id += 1
                        face = cv2.resize(fac_cropped(m_frame), (350, 350))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Capture_faces/student." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Face Captured Panal", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Your Images Are Captured Successfull!!!!!")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)
                # ================ Load predifiend data on face frantals from dlib/open[cv] code end=========================
    # ====================Generate data set or Take photo samples code end===========================
    def ba(self):
        if self.ba:
            self.root.destroy()
        else:
            return
# ==============Student Main class end=====================


# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
# =========main class calling code start==========
