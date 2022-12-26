from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1530,height=750)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=640)


        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=715,height=150)

        # Department Label
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSD","CSE","ECE","IT","CSC","CSM","AID","AIM","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Year Label
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        # Semester Label
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","First","Second")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10)

        # Course Label
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","SFD","DAA","DBMS","OS","SSPE","Python Lab","DBMS Lab","OS Lab","SIP Lab","Additional Course")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)

        # Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=160,width=715,height=450)

        # Roll Number Label
        rollNo_label=Label(class_student_frame,text="Roll Number: ",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=0,column=0,padx=10,pady=2,sticky=W) 

        rollNo_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        rollNo_entry.grid(row=0,column=1,padx=10,pady=2,sticky=W)

        # Student Name Label
        student_name_label=Label(class_student_frame,text="Student Name: ",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=10,pady=2,sticky=W) 

        student_name_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        student_name_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)

        # Gender Label
        gender_label=Label(class_student_frame,text="Gender: ",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=2,sticky=W) 

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        gender_entry.grid(row=2,column=1,padx=10,pady=2,sticky=W)

        # DOB Label
        dob_label=Label(class_student_frame,text="Date of Birth: ",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=3,column=0,padx=10,pady=2,sticky=W) 

        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        dob_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)

        # Email Label
        email_label=Label(class_student_frame,text="Email: ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=4,column=0,padx=10,pady=2,sticky=W) 

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        email_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)

        # Address Label
        address_label=Label(class_student_frame,text="Address: ",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=5,column=0,padx=10,pady=2,sticky=W) 

        address_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        address_entry.grid(row=5,column=1,padx=10,pady=2,sticky=W)

        # Phone Number Label
        phoneNo_label=Label(class_student_frame,text="Phone Number: ",font=("times new roman",12,"bold"),bg="white")
        phoneNo_label.grid(row=6,column=0,padx=10,pady=2,sticky=W) 

        phoneNo_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))       
        phoneNo_entry.grid(row=6,column=1,padx=10,pady=2,sticky=W)

        # Radio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take a Photo Sample", value="Yes")
        radiobtn1.grid(row=7,column=0,padx=10,pady=2,sticky=W)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample", value="Yes")
        radiobtn2.grid(row=7,column=1,padx=10,pady=2,sticky=W)

        # Buttons frame
        btn_frame=Frame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=5,y=240,width=700,height=170)

        save_btn=Button(btn_frame,text="Save",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=0,padx=1)

        delete_btn=Button(btn_frame,text="Delete",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=2,column=0,padx=1)

        reset_btn=Button(btn_frame,text="Reset",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=3,column=0,padx=1)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=4,column=0,padx=1)

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=18,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=4,column=1,padx=1)

        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=560,height=640)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
