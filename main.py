import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
# import customtkinter
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # STUDENT DETAILS
        b1_1 = Button(text="STUDENT DETAILS", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)

        # FACE DETECTOR
        b1_1 = Button(text="FACE DETECTOR", command=self.face_data,cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=400, y=300, width=220, height=40)

        # ATTENDANCE
        b1_1 = Button(text="ATTENDANCE", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=700, y=300, width=220, height=40)

        # HELP DESK
        b1_1 = Button(text="HELP DESK", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=1000, y=300, width=220, height=40)

        # TRAIN DATA
        b1_1 = Button(text="TRAIN DATA", command=self.train_data,cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=100, y=500, width=220, height=40)

        # PHOTOS
        b1_1 = Button(text="PHOTOS", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=400, y=500, width=220, height=40)

        # DEVELOPER
        b1_1 = Button(text="DEVELOPER", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=700, y=500, width=220, height=40)

        # EXIT
        b1_1 = Button(text="EXIT", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=1000, y=500, width=220, height=40)

    # def open_img(self):
        # os.startfile()
    # ====================Functions Buttons=======================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
