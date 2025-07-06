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


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Help Desk")
        self.root.wm_iconbitmap("face.ico")
        
        # ===========first row of header start=============================
        title_lbl = Label(self.root, text="HELP DESK", font=(
            "times new roman", 25, "bold"), bg="white", fg="darkred")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ================back button code start============================
        b1_1 = Button(self.root, text="BACK", cursor="hand2", command=self.ba , font=(
            "cursive", 10, "bold"), bg="white", fg="blue")
        b1_1.place(x=1400, y=5, width=100, height=30)
        # ================back button code end==============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\help.jpg")
        img = img.resize((1520, 745), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=1520, height=745)
    # ===========first row of header end===============================
    # ===========help detials code start===============================
        d_label = Label(f_lbl, text="HEAD DEVELOPER EMAIL ID:- yashvarshney57@gmail.com & MOBILE NO:- 9719421238",font=("times new roman", 10, "bold"))
        d_label.place(x=10,y=550)
        d1_label = Label(f_lbl, text="FIRST ASSISTENT DEVELOPER EMAIL :- Thakursiddharthtomar@gmail.com & MOBILE NO:- 9149266476",font=("times new roman", 7, "bold"))
        d1_label.place(x=550,y=550)
        d2_label = Label(f_lbl, text="SECOND ASSISTENT DEVELOPER EMAIL :- Kumarakash05438@gmail.com & MOBILE NO:- 8859400134",font=("times new roman", 7, "bold"))
        d2_label.place(x=1040,y=550)
    # ===========help detials code end=================================
    def ba(self):
        if self.ba:
            self.root.destroy()
        else:
            return

# ==============Student Main class end=====================


# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
# =========main class calling code start==========