from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # STUDENT DETAILS
        b1_1=Button(text="STUDENT DETAILS",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # FACE DECTECTOR
        b1_1=Button(text="FACE DETECTOR",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        # ATTENDANCE
        b1_1=Button(text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # HELP DESK
        b1_1=Button(text="HELP DESK",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # TRAIN DATA
        b1_1=Button(text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=500,width=220,height=40)

        # PHOTOS
        b1_1=Button(text="PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=500,width=220,height=40)


        # DEVELOPER
        b1_1=Button(text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=500,width=220,height=40)

        # EXIT
        b1_1=Button(text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=500,width=220,height=40)        


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()