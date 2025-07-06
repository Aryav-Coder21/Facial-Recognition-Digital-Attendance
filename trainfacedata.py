from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import title, width
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

# ==============Trainfacedata Main class start=====================


class Trainfacedata:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Train Face Data")
        self.root.wm_iconbitmap("face.ico")
    # ===========first row of header start===============================
        title_lbl = Label(self.root, text="Train Your Face Data Set", font=(
            "times new roman", 25, "bold"), bg="white", fg="gray")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ================back button code start============================
        b1_1 = Button(self.root, text="BACK", cursor="hand2", command=self.ba , font=(
            "cursive", 10, "bold"), bg="white", fg="blue")
        b1_1.place(x=1400, y=10, width=100, height=30)
        # ================back button code end==============================
    # ===========first row of header end===============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\frdp.jpg")
        img = img.resize((1520, 340), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=40, width=1520, height=340)
        # =============train face data set code start====================
        b1_1 = Button(self.root, text="Train Your Face Data", command=self.Train_f, cursor="hand2", font=(
            "cursive", 10, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=0, y=360, width=1520, height=60)
        # =============train face data set code end======================
        # Image second.
        img_bo = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\frdp2.jpg")
        img_bo = img_bo.resize((1520, 370), Image.ANTIALIAS)
        self.photoimgbo = ImageTk.PhotoImage(img_bo)

        f_lbl = Label(self.root, image=self.photoimgbo)
        f_lbl.place(x=0, y=420, width=1520, height=370)

    # ============train module code start====================================
    def Train_f(self):
        da_dr = ("Capture_faces")
        path = [os.path.join(da_dr, file) for file in os.listdir(da_dr)]

        faces = []
        ids = []

        for imge in path:
            img = Image.open(imge).convert('L')  # Convert To Gray Scale Image
            imgNp = np.array(img, 'uint8')
            id = int(os.path.split(imge)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training Face Data", imgNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ================train the classifier and save tha data=========================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Face Data Set Completed!!!")
        self.root.destroy()
        # ================train the classifier and save tha data=========================
    # ============train module code end======================================
    def ba(self):
        if self.ba:
            self.root.destroy()
        else:
            return
# ==============Trainfacedata Main class end=======================

# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = Trainfacedata(root)
    root.mainloop()
# =========main class calling code start==========
