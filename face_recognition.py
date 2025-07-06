from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import title, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
# ==============Face_recognition Main class start=====================


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Capture Attendance")
        self.root.wm_iconbitmap("face.ico")

        self.var_sub = StringVar()
    # ===========first row of header start===============================
        title_lbl = Label(self.root, text="Face Recognition Attendance System", font=(
            "times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1520, height=50)
        # ================back button code start============================
        b1_1 = Button(title_lbl, text="BACK", cursor="hand2", command=self.ba , font=(
            "cursive", 10, "bold"), bg="white", fg="blue")
        b1_1.place(x=1400, y=10, width=100, height=30)
        # ================back button code end==============================
    # ===========first row of header end===============================
        # Image first.
        img = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\fdas.jpg")
        img = img.resize((760, 740), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=50, width=760, height=740)

        # Image second.
        img1 = Image.open(
            r"C:\Users\Hp\Desktop\Minor Project Face_Recognition Attendance\header, buttons icons and Background Images\fdsas.jpg")
        img1 = img1.resize((760, 740), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=765, y=50, width=760, height=740)
        # =============train face data set code start====================
        b1_1 = Button(f_lbl, text="Capture Your Attandance", command=self.cap_your_attendance, cursor="hand2", font=(
            "cursive", 18, "bold"), bg="lightblue", fg="blue")
        b1_1.place(x=230, y=600, width=300, height=40)
        # =============train face data set code end======================
    #==================attendance mark fucntion code start============================
    def mark_attendanace(self,i,en,sn,d):
        with open("att\Attendances.csv","r+",newline="\n") as f:
            mydataattendancelist=f.readlines()
            name_list=[]
            for line in mydataattendancelist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (en not in name_list) and (sn not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{en},{sn},{d},{dtString},{d1},Present")
    #==================attendance mark fucntion code end==============================
    # ===================Capture your attendance code start===========================

    def cap_your_attendance(self):
        def d_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feat = classifier.detectMultiScale(
                gray_img, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in feat:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="myminorproject")
                m_cur = conn.cursor()
                m_cur.execute(
                    "Select enroll from student_details where sid="+str(id))
                en = m_cur.fetchone()
                en = "+".join(en)
                m_cur.execute(
                    "Select s_name from student_details where sid="+str(id))
                sn = m_cur.fetchone()
                sn = "+".join(sn)
                m_cur.execute(
                    "Select dep from student_details where sid="+str(id))
                d = m_cur.fetchone()
                d = "+".join(d)
                m_cur.execute(
                    "Select sid from student_details where sid="+str(id))
                i = m_cur.fetchone()
                i = "+".join(i)
                if confidence > 88:
                    cv2.putText(
                        img, f"SID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    cv2.putText(
                        img, f"roll:{en}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    cv2.putText(
                        img, f"name:{sn}", (x, y-35), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    cv2.putText(
                        img, f"dep:{d}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    self.mark_attendanace(i,en,sn,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)
                    cv2.putText(img, "Unknown Person", (x, y-15),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recog(img, clf, facecascade):
            coord = d_boundray(img, facecascade, 1.1, 10,
                               (255, 25, 255), "Face", clf)
            return img
        facecascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        vid_cap = cv2.VideoCapture(0)
        while True:
            ret, img = vid_cap.read()
            img = recog(img, clf, facecascade)
            cv2.imshow("Attendance Capture Panel", img)
            if cv2.waitKey(1) == 13:
                break
        vid_cap.release()
        cv2.destroyAllWindows()


    # ===================Capture your attendance code end=============================
    def ba(self):
        if self.ba:
            self.root.destroy()
        else:
            return
# ==============Face_recognition Main class end=======================
# =========main class calling code start==========
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
# =========main class calling code start==========
