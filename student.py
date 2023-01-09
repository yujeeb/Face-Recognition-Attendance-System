from tkinter import *
from tkinter import ttk
import os
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://instantattendance-fa6e1-default-rtdb.firebaseio.com/",
    'storageBucket': "instantattendance-fa6e1.appspot.com"
})

ref = db.reference('Students')


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # =======================Variables=====================
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_course = StringVar()
        self.var_rollNo = StringVar()
        self.var_stName = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phoneNo = StringVar()

        title_lbl = Label(text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1530, height=750)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=380, height=640)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=0, width=365, height=170)

        # Department Label
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "CSD", "CSE", "ECE","IT", "CSC", "CSM", "AID", "AIM", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Year Label
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2022-2026", "2021-2025", "2020-2024", "2019-2023")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

        # Semester Label
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=2, column=0, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2")
        semester_combo.current(0)
        semester_combo.grid(row=2, column=1, padx=2, pady=10)

        # Course Label
        # course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        # course_label.grid(row=3,column=0,padx=10,sticky=W)

        # course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        # course_combo["values"]=("Select Course","SFD","DAA","DBMS","OS","SSPE","Python Lab","DBMS Lab","OS Lab","SIP Lab","Additional Course")
        # course_combo.current(0)
        # course_combo.grid(row=3,column=1,padx=2,pady=10)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,text="CLASS STUDENT INFORMATION", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=180, width=365, height=430)

        # Roll Number Label
        rollNo_label = Label(class_student_frame, text="Roll Number: ", font=("times new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)

        rollNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_rollNo, width=20, font=("times new roman", 12, "bold"))
        rollNo_entry.grid(row=0, column=1, padx=10, pady=2, sticky=W)

        # Student Name Label
        student_name_label = Label(class_student_frame, text="Student Name: ", font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_stName, width=20, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        # Gender Label
        gender_label = Label(class_student_frame, text="Gender: ", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=2, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=2)

        # DOB Label
        dob_label = Label(class_student_frame, text="Date of Birth: ", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=3, column=0, padx=10, pady=2, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=3, column=1, padx=10, pady=2, sticky=W)

        # Email Label
        email_label = Label(class_student_frame, text="Email: ", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=4, column=0, padx=10, pady=2, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=4, column=1, padx=10, pady=2, sticky=W)

        # Address Label
        address_label = Label(class_student_frame, text="Address: ", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=5, column=0, padx=10, pady=2, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=5, column=1, padx=10, pady=2, sticky=W)

        # Phone Number Label
        phoneNo_label = Label(class_student_frame, text="Phone Number: ", font=("times new roman", 12, "bold"), bg="white")
        phoneNo_label.grid(row=6, column=0, padx=10, pady=2, sticky=W)

        phoneNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_phoneNo, width=20, font=("times new roman", 12, "bold"))
        phoneNo_entry.grid(row=6, column=1, padx=10, pady=2, sticky=W)

        # Radio Buttons

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take a Photo Sample", value="Yes")
        radiobtn1.grid(row=7, column=0, padx=10, pady=2, sticky=W)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=7, column=1, padx=10, pady=2, sticky=W)



        # Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=5, y=230, width=350, height=169)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=1)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=1, column=0, padx=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=2, column=0, padx=1)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=3, column=0, padx=1)

        take_photo_btn = Button(btn_frame, text="Take Photo Sample", command=self.generate_dataset, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=4, column=0, padx=1)

        update_photo_btn = Button(btn_frame, text="Upload Photo Sample", command=self.upload_photo, width=18, font=("times new roman", 12, "bold"), bg="green", fg="white")
        update_photo_btn.grid(row=4, column=1, padx=1)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        Right_frame.place(x=400, y=10, width=945, height=640)

        # search information
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,text="SEARCH SYSTEM", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=5, width=930, height=600)

        search_label = Label(search_frame, text="Search By: ", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Search By", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=2, sticky=W)

        search_btn = Button(search_frame, text="Search", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        Showall_btn = Button(search_frame, text="Show all", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        Showall_btn.grid(row=0, column=4, padx=4)

        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=80, width=930, height=525)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("rollNo", "stName", "dep", "year", "sem", "gender", "dob","email", "address", "phoneNo", "photoSample","refID"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("rollNo", text="Roll Number")
        self.student_table.heading("stName", text="Student Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phoneNo", text="Phone Number")
        self.student_table.heading("photoSample", text="Photo Sample")
        self.student_table.heading("refID", text="Reference ID")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =============fetch data===========

    def fetch_data(self):
        try:
            cursor_focus = self.student_table.focus()
            content = self.student_table.item(cursor_focus)
            student_table_data = content["values"]
            # ref_id = student_table_data[11]

            student_info = db.reference('Students/').get()
            print(student_info)
            student_info = student_info[1:]
            student_value = ()
            for dicts in student_info:
                # print(key)
                # print(attributes)
                try:
                    student_value = (dicts['Roll Number'] if "Roll Number" in dicts else "None Provided",
                                     dicts['Student Name'] if "Student Name" in dicts else "None Provided",
                                     dicts['Department'] if "Department" in dicts else "None Provided",
                                     dicts['Year'] if "Year" in dicts else "None Provided",
                                     dicts['Semester'] if "Semester" in dicts else "None Provided",
                                     dicts['Gender'] if "Gender" in dicts else "None Provided",
                                     dicts['Date of Birth'] if "Date of Birth" in dicts else "None Provided",
                                     dicts['Email'] if "Email" in dicts else "None Provided",
                                     dicts['Address'] if "Address" in dicts else "None Provided",
                                     dicts['Phone Number'] if "Phone Number" in dicts else "None Provided",
                                     dicts['Photo Sample'] if "Photo Sample" in dicts else "None Provided",
                                     dicts['Reference ID'] if "Reference ID" in dicts else "None Provided")

                    self.student_table.insert("", END, values=student_value)
                except Exception as es:
                    print(es)
        except Exception as es:
            print(es)

    # =================get cursor===========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        student_table_data = content["values"]

        self.var_rollNo.set(student_table_data[0]),
        self.var_stName.set(student_table_data[1]),
        self.var_dep.set(student_table_data[2]),
        self.var_year.set(student_table_data[3]),
        self.var_sem.set(student_table_data[4]),
        self.var_gender.set(student_table_data[5]),
        self.var_dob.set(student_table_data[6]),
        self.var_email.set(student_table_data[7]),
        self.var_address.set(student_table_data[8]),
        self.var_phoneNo.set(student_table_data[9]),
        self.var_radio1.set(student_table_data[10])

    # ================Function Description=====================
    def proceed(self):
        if self.var_rollNo.get() == "" or self.var_stName.get() == "" or self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_gender.get() == "Gender" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_address.get() == "" or self.var_phoneNo.get() == "" or self.var_radio1.get() == "":
            return True
        else:
            return False

    def add_data(self):
        if self.proceed():
            messagebox.showerror("ERROR", "Fill all the fields", parent=self.root)
        else:
            try:
                student_id = db.reference('ref_count').get()
                student_id += 1
                data = {
                    str(student_id):
                        {
                            "Department": self.var_dep.get(),
                            "Year": self.var_year.get(),
                            "Semester": self.var_sem.get(),
                            "Roll Number": self.var_rollNo.get(),
                            "Student Name": self.var_stName.get(),
                            "Gender": self.var_gender.get(),
                            "Date of Birth": self.var_dob.get(),
                            "Email": self.var_email.get(),
                            "Address": self.var_address.get(),
                            "Phone Number": self.var_phoneNo.get(),
                            "Photo Sample": self.var_radio1.get(),
                            "Reference ID": str(student_id)
                    }
                }
                self.student_table.insert(parent="", index='end', values=(
                    self.var_rollNo.get(),
                    self.var_stName.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phoneNo.get(),
                    self.var_radio1.get(),
                    student_id
                ))
                for key, value in data.items():
                    ref.child(key).set(value)

                db.reference("ref_count").set(student_id)

                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

        # ===============update data=================

    def update_data(self):
        if self.proceed():
            messagebox.showerror("ERROR", 'Fill all fields. \nFill "NA" for fields with unknown values.', parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure to update these details?", parent=self.root)
                if update > 0:
                    cursor_focus = self.student_table.focus()
                    content = self.student_table.item(cursor_focus)
                    student_table_data = content["values"]
                    ref_id = student_table_data[11]

                    ref.update(value={ref_id: {
                        "Department": self.var_dep.get(),
                        "Year": self.var_year.get(),
                        "Semester": self.var_sem.get(),
                        "Roll Number": self.var_rollNo.get(),
                        "Student Name": self.var_stName.get(),
                        "Gender": self.var_gender.get(),
                        "Date of Birth": self.var_dob.get(),
                        "Email": self.var_email.get(),
                        "Address": self.var_address.get(),
                        "Phone Number": self.var_phoneNo.get(),
                        "Photo Sample": self.var_radio1.get(),
                        "Reference ID": ref_id
                    }})
                    self.student_table.item(self.student_table.focus(), text="", values=(
                        db.reference(f'Students/{ref_id}/Roll Number').get(),
                        db.reference(f'Students/{ref_id}/Student Name').get(),
                        db.reference(f'Students/{ref_id}/Department').get(),
                        db.reference(f'Students/{ref_id}/Year').get(),
                        db.reference(f'Students/{ref_id}/Semester').get(),
                        db.reference(f'Students/{ref_id}/Gender').get(),
                        db.reference(f'Students/{ref_id}/Date of Birth').get(),
                        db.reference(f'Students/{ref_id}/Email').get(),
                        db.reference(f'Students/{ref_id}/Address').get(),
                        db.reference(f'Students/{ref_id}/Phone Number').get(),
                        db.reference(f'Students/{ref_id}/Photo Sample').get(),
                        db.reference(f'Students/{ref_id}/Reference ID').get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # ===================delete function=======================
    def delete_data(self):
        if self.var_rollNo.get() == "":
            messagebox.showerror("Error", "Roll Number is required", parent=self.root)
        else:
            try:
                cursor_focus = self.student_table.focus()
                content = self.student_table.item(cursor_focus)
                student_table_data = content["values"]
                ref_id = student_table_data[11]
                student_info = ref.get()[1:]
                delete = messagebox.askyesno("Confirmation", "Do you want to delete this student's details?", parent=self.root)
                if delete > 0:
                        # for dicts in student_info:
                        # for k, v in dicts.items():
                        # if dicts['Reference ID'] == int(ref_id):
                    db.reference('Students').child(str(ref_id)).delete()
                else:
                    if not delete:
                        return

                self.student_table.delete(self.student_table.selection()[0])
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # =================reset=======================
    def reset_data(self):
        self.var_rollNo.set(""),
        self.var_stName.set(""),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_gender.set("Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_phoneNo.set(""),
        self.var_radio1.set("")

    # =========================generate data set or take photo samples===================

    def generate_dataset(self):
        if self.proceed():
            messagebox.showerror("ERROR", "Fill all the fields", parent=self.root)
        else:
            try:
                # ========Load predefined data on face frontals from opencv==========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                cursor_focus = self.student_table.focus()
                content = self.student_table.item(cursor_focus)
                student_table_data = content["values"]
                refID = student_table_data[11]

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimum neighbour = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                # try:
                #     os.chdir("dataset")
                #     os.mkdir(f"{roll}")
                # except Exception as es:
                #     pass

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        dataset_path = r"dataset/user." + str(refID) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(dataset_path, face)
                        cv2.putText(face, str(img_id), (50, 50),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Collecting data", face)

                        # bucket = storage.bucket()
                        # blob = bucket.blob(face)
                        # blob.upload_from_file(face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                ref.update(value={refID: {
                    "Department": self.var_dep.get(),
                    "Year": self.var_year.get(),
                    "Semester": self.var_sem.get(),
                    "Roll Number": self.var_rollNo.get(),
                    "Student Name": self.var_stName.get(),
                    "Gender": self.var_gender.get(),
                    "Date of Birth": self.var_dob.get(),
                    "Email": self.var_email.get(),
                    "Address": self.var_address.get(),
                    "Phone Number": self.var_phoneNo.get(),
                    "Photo Sample": "Yes",
                    "Reference ID": refID
                }})
                self.student_table.item(self.student_table.focus(), text="", values=(
                    db.reference(f'Students/{refID}/Roll Number').get(),
                    db.reference(f'Students/{refID}/Student Name').get(),
                    db.reference(f'Students/{refID}/Department').get(),
                    db.reference(f'Students/{refID}/Year').get(),
                    db.reference(f'Students/{refID}/Semester').get(),
                    db.reference(f'Students/{refID}/Gender').get(),
                    db.reference(f'Students/{refID}/Date of Birth').get(),
                    db.reference(f'Students/{refID}/Email').get(),
                    db.reference(f'Students/{refID}/Address').get(),
                    db.reference(f'Students/{refID}/Phone Number').get(),
                    db.reference(f'Students/{refID}/Photo Sample').get(),
                    db.reference(f'Students/{refID}/Reference ID').get()
                ))



        # folderPath = f'{str(roll)}'
        # pathList = os.listdir(folderPath)
        # print(pathList)
        # imgList = []
        # studentIds = []

                # folderRoll = str(roll)
                # for folderRoll in pathList:
        # for path in pathList:
        #     imgList.append(cv2.imread(os.path.join(folderPath, path)))
        #     studentIds.append(os.path.splitext(path)[0])
        #
        #     fileName = f'{folderPath}/{path}'
        #     bucket = storage.bucket()
        #     blob = bucket.blob(fileName)
        #     blob.upload_from_filename(fileName)
                # bucket = storage.bucket()
                # blob = bucket.blob(filename)
                # blob.upload_from_filename(filename)
                # messagebox.showinfo("Result", "Generating dataset completed successfully.")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def upload_photo(self):
        if self.proceed():
            messagebox.showerror("ERROR", "Fill all the fields", parent=self.root)
        else:
            try:
                folderPath = 'Dataset'
                pathList = os.listdir(folderPath)
                print(pathList)
                imgList = []
                studentIds = []

                for path in pathList:
                    imgList.append(cv2.imread(os.path.join(folderPath, path)))
                    studentIds.append(os.path.splitext(path)[0])

                    fileName = f'{folderPath}/{path}'
                    bucket = storage.bucket()
                    blob = bucket.blob(fileName)
                    blob.upload_from_filename(fileName)

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
