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
import os
import csv
from tkinter import filedialog

# ==============Attendance Main class start=====================

myd=[]

class Attendance_p:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Attendances Panel")
        self.root.wm_iconbitmap("face.ico")
        
        # ========text variables start==================
        self.var_attend_id=StringVar()
        self.var_enrollment=StringVar()
        self.var_student_name=StringVar()
        self.var_depart=StringVar()
        self.var_tim=StringVar()
        self.var_dat=StringVar()
        self.var_status=StringVar()
        # ========text variables end====================
        # ===========first row of header start===============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\SmartAttendance.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)
        # Image second.
        img1 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\s2s.jpg")
        img1 = img1.resize((720, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=720, height=200)
        # ===========first row of header end===============================
        # ============background image start===============================
        bgimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\istockphoto.jpg")
        bgimg = bgimg.resize((1520, 690), Image.ANTIALIAS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        b_img = Label(self.root, image=self.photobgimg)
        b_img.place(x=0, y=120, width=1520, height=690)
        # ============background image end=================================
        # ===========second row of header start===============================
        title_lbl = Label(b_img, text="STUDENT'S ATTENDANCES", font=(
            "times new roman", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ================back button code start============================
        b1_1 = Button(title_lbl, text="BACK", cursor="hand2", command=self.ba , font=(
            "cursive", 10, "bold"), bg="white", fg="blue")
        b1_1.place(x=1400, y=5, width=100, height=30)
        # ================back button code end==============================
        # ===========second row of header end===============================
        # ====================main attendance details background code start==================
        main_frame = Frame(b_img, bd=2)
        main_frame.place(x=20, y=45, width=1480, height=620)
        # ====================main attendance details background code end====================
        # ====================left label form header,border and background code start==================================
        left_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE,
                                text="Students Attendances Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=600, height=600)
        # ====================left form header image code start=========================
        lsfimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\atfff.jpg")
        lsfimg = lsfimg.resize((585, 95), Image.ANTIALIAS)
        self.photolsfimg = ImageTk.PhotoImage(lsfimg)

        f_lbl = Label(left_frame, image=self.photolsfimg)
        f_lbl.place(x=5, y=0, width=585, height=95)
        # ====================left form header image code end=========================
        # ====================left label form header,border and background code end====================================
        #=====================left inside label code start=======================================
        lft_inside_frame = Frame(left_frame, bd=2,relief=RIDGE,bg="white")
        lft_inside_frame.place(x=5, y=100, width=585, height=350)
        #=====================left inside label code end=========================================
        #=====================left label code start=======================================
        #=====================Labels & Entry Fields code start============================
        # ===============attendanceid label code start===========================
        attendanceid_label = Label(lft_inside_frame, text="AttendanceID:", font=(
            "times new roman", 12, "bold"), bg="white")
        attendanceid_label.grid(row=0, column=0, sticky=W, padx=5)
        attendanceid_entry = ttk.Entry(
            lft_inside_frame, width=20, textvariable=self.var_attend_id , font=("times new roman", 12, "bold"))
        attendanceid_entry.grid(row=0, column=1, sticky=W, pady=5)
        # ===============attendanceid label code end=============================
        # ===============enrollmentno label code start===========================
        enrollmentno_label = Label(lft_inside_frame, text="Enrollment No:", font=(
            "times new roman", 12, "bold"), bg="white")
        enrollmentno_label.grid(row=0, column=2, sticky=W, padx=5)
        enrollmentno_entry = ttk.Entry(
            lft_inside_frame, width=20, textvariable=self.var_enrollment, font=("times new roman", 12, "bold"))
        enrollmentno_entry.grid(row=0, column=3, sticky=W)
        # ===============enrollmentno label code end=============================
        # ===============Sudentname label code start===========================
        sn_label = Label(lft_inside_frame, text="Sudent Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        sn_label.grid(row=1, column=0, sticky=W, padx=5, pady=10)
        studentname_entry = ttk.Entry(
            lft_inside_frame, width=20, textvariable=self.var_student_name, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=1, column=1, sticky=W, pady=10)
        # ===============Sudentname label code end=============================
        # ===============department label code start===========================
        dep_label = Label(lft_inside_frame, text="Department:", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, sticky=W, padx=5, pady=10)
        department_entry = ttk.Entry(
            lft_inside_frame, width=20, textvariable=self.var_depart, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, sticky=W, pady=10)
        # ===============department label code end=============================
        # ===============Time label code start===========================
        tm_label = Label(lft_inside_frame, text="Time:", font=(
            "times new roman", 12, "bold"), bg="white")
        tm_label.grid(row=2, column=0, sticky=W, padx=5, pady=10)
        time_entry = ttk.Entry(
            lft_inside_frame, width=20, textvariable=self.var_tim, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, sticky=W, pady=10)
        # ===============Time label code end=============================
        # ===============Date label code start===========================
        dt_label = Label(lft_inside_frame, text="Date:", font=(
            "times new roman", 12, "bold"), bg="white")
        dt_label.grid(row=2, column=2, sticky=W, padx=5, pady=10)
        date_entry = ttk.Entry(
            lft_inside_frame, width=20, textvariable=self.var_dat, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, sticky=W, pady=10)
        # ===============Date label code end=============================
        # ===============attendance label code start===========================
        at_label = Label(lft_inside_frame, text="Sudent Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        at_label.grid(row=3, column=0)
        self.atten_entry = ttk.Combobox(lft_inside_frame,width=20,textvariable=self.var_status,font="comicsansns 11 bold",state="readonly")
        self.atten_entry["values"]=("Status","Present","Absent")
        self.atten_entry.grid(row=3, column=1, pady=10)
        self.atten_entry.current(0)
        # ===============attendance label code end=============================
        # ================buttons frame code start======================
        btn_frame = Frame(lft_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=60, y=280, width=440, height=37)
        # =================save btn code start=======================
        importcsv_btn = Button(btn_frame, text="Import XSL", command=self.im_csv , font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        importcsv_btn.grid(row=0, column=0)
        # =================save btn code end=========================
        # =================update btn code start=======================
        exportcsv_btn = Button(btn_frame, text="Export XSL", command=self.ex_csv , font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        exportcsv_btn.grid(row=0, column=1)
        # =================update btn code end=========================
        # =================delete btn code start=======================
        #del_btn = Button(btn_frame, text="Update", font=(
            #"times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        #del_btn.grid(row=0, column=2)
        # =================delete btn code end=========================
        # =================reset btn code start=======================
        re_btn = Button(btn_frame, text="Reset Form Data", command=self.rset ,font=(
            "times new roman", 12, "bold"), bg="blue", fg="white", width=15)
        re_btn.grid(row=0, column=2)
        # =================reset btn code end============
        # ================buttons frame code end=====================================
        #=====================Labels & Entry Fields code end==============================
        #=====================left label code end=========================================
        # ====================right label form header,border and background code start==================================
        right_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE,
                                 text="Student's Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=620, y=10, width=840, height=600)
        # ====================right label form header,border and background code end====================================
        # ================buttons frame code start======================
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=820, height=565)
        # ================buttons frame code end=====================================
        # ================scroll bar code start======================================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.ART=ttk.Treeview(table_frame,columns=("id","enrollment","name","department","time","date","attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.ART.xview)
        scroll_y.config(command=self.ART.yview)
        
        self.ART.heading("id",text="Student ID")
        self.ART.heading("enrollment",text="Enrollment No")
        self.ART.heading("name",text="Student Name")
        self.ART.heading("department",text="Department")
        self.ART.heading("time",text="Time")
        self.ART.heading("date",text="Date")
        self.ART.heading("attend",text="Attendance")
        
        self.ART["show"]="headings"
        
        self.ART.column("id",width=100)
        self.ART.column("enrollment",width=100)
        self.ART.column("name",width=100)
        self.ART.column("department",width=100)
        self.ART.column("time",width=100)
        self.ART.column("date",width=100)
        self.ART.column("attend",width=100)
        
        self.ART.pack(fill=BOTH,expand=1)
        self.ART.bind("<ButtonRelease>",self.cur)
        # ================scroll bar code end========================================
    # =====================import data from xsl file code start================================
    def fet_dat(self,rows):
        self.ART.delete(*self.ART.get_children())
        for i in rows:
            self.ART.insert("",END,values=i)
    
    def im_csv(self):
        global myd
        myd.clear()
        fl=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fl) as myfl:
            csvread=csv.reader(myfl,delimiter=",")
            for i in csvread:
                myd.append(i)
            self.fet_dat(myd)
    # =====================import data from xsl file code end===================================
    # =====================export data from table to database code start========================
    def ex_csv(self):
        try:
            if len(myd)<1:
                messagebox.showerror("No Data","NO Data Found To Export in Database",parent=self.root)
                return False
            fl=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fl,mode="w",newline="") as myf:
                exp_w=csv.writer(myf,delimiter=",")
                for i in myd:
                    exp_w.writerow(i)
                messagebox.showinfo("Data","Your Data Exported to "+os.path.basename(fl)+" successfully")
        except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)
    # =====================export data from table to database code end==========================
    # =====================cursor code start========================================
    def cur(self,ev=""):
        curs_r=self.ART.focus()
        content=self.ART.item(curs_r)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_enrollment.set(rows[1])
        self.var_student_name.set(rows[2])
        self.var_depart.set(rows[3])
        self.var_tim.set(rows[4])
        self.var_dat.set(rows[5])
        self.var_status.set(rows[6])
    # =====================cursor code end==========================================
    # =====================reset code start=========================================
    def rset(self):
        self.var_attend_id.set("")
        self.var_enrollment.set("")
        self.var_student_name.set("")
        self.var_depart.set("")
        self.var_tim.set("")
        self.var_dat.set("")
        self.var_status.set("Status")
    # =====================reset code end===========================================
    def ba(self):
        if self.ba:
            self.root.destroy()
        else:
            return
        
# ==============Attendance Main class end=======================
        
        
# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = Attendance_p(root)
    root.mainloop()
# =========main class calling code start==========