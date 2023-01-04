from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connecter
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman",35,"bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # button
        b1_1=Button(self.root,text="TRAIN DATA", command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

    def train_classifier(self):
        data_dir=("dataset")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') # gray scale image
            imageNP=np.array(img,'uint8')
            id=os.path.split(image)[1].split('.')[1]

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #============= Train the classifier and save ==============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Training datasets completed!!")
        
