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

# ==============developer Main class start=====================


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Developer Details")
        self.root.wm_iconbitmap("face.ico")
    # ===========first row of header start=============================
        title_lbl = Label(self.root, text="Developer's Section", font=(
            "times new roman", 25, "bold"), bg="white", fg="purple")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ================back button code start============================
        b1_1 = Button(self.root, text="BACK", cursor="hand2", command=self.ba , font=(
            "cursive", 10, "bold"), bg="white", fg="blue")
        b1_1.place(x=1400, y=10, width=100, height=30)
        # ================back button code end==============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\GUI.jpg")
        img = img.resize((1520, 745), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=1520, height=745)
    # ===========first row of header end===============================
    # ====================main developer details background code start==================
        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=815, y=0, width=700, height=305)
        
    # ====================developer image or details====================================
        dpimg = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\developer.jpg")
        dpimg = dpimg.resize((200, 300), Image.ANTIALIAS)
        self.photodpimg = ImageTk.PhotoImage(dpimg)

        f_lbl = Label(main_frame, image=self.photodpimg)
        f_lbl.place(x=495, y=0, width=200, height=300)
        
        d_label = Label(main_frame, text="1. HEAD DEVELOPER NAME IS:- ARYAV VARSHNEY",font=("times new roman", 10, "bold"))
        d_label.place(x=0,y=5)
        d1_label = Label(main_frame, text="2. ASSISTENT DEVELOPER's NAMES IS:- SIDDHARTH TOMAR & AKASH",font=("times new roman", 10, "bold"))
        d1_label.place(x=0,y=25)
        d2_label = Label(main_frame, text="3. HEAD DEVELOPER IS A FULL PROJECT DEVELOPER",font=("times new roman", 10, "bold"))
        d2_label.place(x=0,y=45)
        d3_label = Label(main_frame, text="4. ASSISTENT 1 SIDDHARTH TOMAR IS MANAGING DATABASE",font=("times new roman", 10, "bold"))
        d3_label.place(x=0,y=65)
        d4_label = Label(main_frame, text="5. ASSISTENT 2 AKASH IS MANAGING XSL & EMAIL",font=("times new roman", 10, "bold"))
        d4_label.place(x=0,y=85)
        
        img23 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\puy.jpg")
        img23 = img23.resize((490, 195), Image.ANTIALIAS)
        self.photoimg23 = ImageTk.PhotoImage(img23)

        f_lbl = Label(main_frame, image=self.photoimg23)
        f_lbl.place(x=0, y=105, width=490, height=195)
    # ====================developer image or details====================================
    # ====================main developer details background code end====================
    def ba(self):
        if self.ba:
            self.root.destroy()
        else:
            return

# ==============Student Main class end========================

# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
# =========main class calling code end============