from tkinter import *
from tkinter import ttk
from turtle import title
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from trainfacedata import Trainfacedata
from face_recognition import Face_recognition
from Attendance import Attendance_p
from developer import developer
from helpdesk import Help
# ==============Main class=====================


class F_R_S:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition & Digital Attandence")
        self.root.wm_iconbitmap("face.ico")
        # ===========first row of header start===============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\mmit-hathras-340403.jpg")
        img = img.resize((500, 120), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=120)
        # Image second.
        img1 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\s.jpg")
        img1 = img1.resize((500, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=120)
        # Image third.
        img2 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\mmit h.jpg")
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
        title_lbl = Label(b_img, text="FACE RECOGNITION & DIGITAL ATTENDANCE SYSTEM SOFTWARE", font=(
            "cursive", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ======================time=======================================
        def t():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, t)
        lbl = Label(title_lbl, font= ('times new roman',14,'bold'),background='white',foreground='black')
        lbl.place(x=0,y=0,width=110,height=60)
        t()
        # ======================time=======================================
        # ===========second row of header end===============================
        # =============All Types of Buttons row start=======================
        # ===========Student's Detail Button code start=====================
        stdtimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\s1.jpg")
        stdtimg = stdtimg.resize((150, 150), Image.ANTIALIAS)
        self.photostdtimg = ImageTk.PhotoImage(stdtimg)
        b1 = Button(b_img, image=self.photostdtimg,
                    command=self.student_details, cursor="hand2")
        b1.place(x=150, y=100, width=150, height=150)

        b1_1 = Button(b_img, text="Student's details", command=self.student_details,
                      cursor="hand2", font=("cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=150, y=250, width=150, height=35)
        # ===========Student's Detail Button code end=====================
        # ===========Train Button code start=====================
        timg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\tr.jpg")
        timg = timg.resize((150, 150), Image.ANTIALIAS)
        self.phototimg = ImageTk.PhotoImage(timg)
        b1 = Button(b_img, image=self.phototimg,
                    command=self.train_data, cursor="hand2")
        b1.place(x=450, y=100, width=150, height=150)

        b1_1 = Button(b_img, text="Train Your Face Data", command=self.train_data, cursor="hand2", font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=450, y=250, width=150, height=35)
        # ===========Train Button code end=====================
        # ===========Face Detect Button code start=====================
        fdimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\fd.jpg")
        fdimg = fdimg.resize((150, 150), Image.ANTIALIAS)
        self.photofdimg = ImageTk.PhotoImage(fdimg)
        b1 = Button(b_img, image=self.photofdimg,
                    command=self.face_data, cursor="hand2")
        b1.place(x=750, y=100, width=150, height=150)

        b1_1 = Button(b_img, text="Face Recognition", command=self.face_data, cursor="hand2", font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=750, y=250, width=150, height=35)
        # ===========Face Detect Button code end=====================
        # ===========help Button code start=====================
        himg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\hpl.png")
        himg = himg.resize((150, 150), Image.ANTIALIAS)
        self.photohimg = ImageTk.PhotoImage(himg)
        b1 = Button(b_img, image=self.photohimg, command=self.help , cursor="hand2")
        b1.place(x=600, y=350, width=150, height=150)

        b1_1 = Button(b_img, text="Help Desk", command=self.help , cursor="hand2", font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=600, y=500, width=150, height=35)
        # ===========help Button code end=====================
        # ===========photo Button code start=====================
        pimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\p.png")
        pimg = pimg.resize((150, 150), Image.ANTIALIAS)
        self.photopimg = ImageTk.PhotoImage(pimg)
        b1 = Button(b_img, image=self.photopimg,
                    cursor="hand2", command=self.open_im)
        b1.place(x=300, y=350, width=150, height=150)

        b1_1 = Button(b_img, text="See Your Photos", cursor="hand2", command=self.open_im, font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=300, y=500, width=150, height=35)
        # ===========photo Button code end=====================
        # ===========Attendance Button code start=====================
        atimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\at.jpg")
        atimg = atimg.resize((150, 150), Image.ANTIALIAS)
        self.photoatimg = ImageTk.PhotoImage(atimg)
        b1 = Button(b_img, image=self.photoatimg, cursor="hand2", command=self.attenda)
        b1.place(x=1050, y=100, width=150, height=150)

        b1_1 = Button(b_img, text="See Your Attendance", cursor="hand2", command=self.attenda, font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=1050, y=250, width=150, height=35)
        # ===========Attendance Button code end=====================
        # ===========Developer Button code start=====================
        deimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\d.png")
        deimg = deimg.resize((150, 150), Image.ANTIALIAS)
        self.photodeimg = ImageTk.PhotoImage(deimg)
        b1 = Button(b_img, image=self.photodeimg, command=self.deve , cursor="hand2")
        b1.place(x=900, y=350, width=150, height=150)

        b1_1 = Button(b_img, text="See Developer Detail's", command=self.deve , cursor="hand2", font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=900, y=500, width=150, height=35)
        # ===========Developer Button code end=====================
        # ===========exit Button code start=====================
        eimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\exi.jpg")
        eimg = eimg.resize((150, 150), Image.ANTIALIAS)
        self.photoeimg = ImageTk.PhotoImage(eimg)
        b1 = Button(b_img, image=self.photoeimg, command=self.Iexit , cursor="hand2")
        b1.place(x=1200, y=350, width=150, height=150)

        b1_1 = Button(b_img, text="Exit", command=self.Iexit , cursor="hand2", font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=1200, y=500, width=150, height=35)
        # ===========exit Button code end=====================
    # ================capture image display function code start==================

    def open_im(self):
        os.startfile("Capture_faces")
        
    def Iexit(self):
        self.Iexit=tkinter.messagebox.askyesno("Face Recognition & Digital Attandence","Are you sure exit this project",parent=self.root)
        if self.Iexit>0:
            self.root.destroy()
        else:
            return
    # ================capture image display function code end====================
    # ===========Function of 8 button code start=====================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Trainfacedata(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
    
    def attenda(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance_p(self.new_window)
    
    def deve(self):
        self.new_window = Toplevel(self.root)
        self.app = developer(self.new_window)
        
    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


    # ===========Function of 8 button code end=======================
# ==============Main class end=====================
# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = F_R_S(root)
    root.mainloop()
# =========main class calling code start==========
