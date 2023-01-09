from tkinter import*
import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': "https://instantattendance-fa6e1-default-rtdb.firebaseio.com/",
#     'storageBucket': "instantattendance-fa6e1.appspot.com"
# })


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        b1_1=Button(self.root,text="FACE RECOGNITION",command = self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_1.place(x=350,y=600,width=200,height=40)

        # ---------------------FACE -------------------#

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                fid,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                # conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                # my_cursor=conn.cursor()

                # my_cursor.execute("select Name from student where Studend_id="+str(id))
                # n=my_cursor.fetchone()
                # n="+".join(n)
                #
                # my_cursor.execute("select Roll from student where Studend_id="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)
                #
                # my_cursor.execute("select Dept from student where Studend_id="+str(id))
                # d=my_cursor.fetchone()
                # d="+".join(d)

                n = db.reference(f'Students/{fid}/Student Name').get()
                r = db.reference(f'Students/{fid}/Roll Number').get()
                d = db.reference(f'Students/{fid}/Department').get()

                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(img, f"Face in DB", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]

            return coord
    
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()