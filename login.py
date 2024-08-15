from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import os
import re


def main():
    win=Tk()
    app=login_Window(win)
    win.mainloop()



class login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mihir\Desktop\LOGIN_FORM\image\new1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="navyblue")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\mihir\Desktop\LOGIN_FORM\image\dd.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new romen",20,"bold"),fg="white",bg="navyblue")
        get_str.place(x=95,y=100)

        #label
        username=lal=Label(frame,text="Username",font=("times new romen",15,"bold"),fg="white",bg="navyblue")
        username.place(x=100,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new romen",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lal=Label(frame,text="Password",font=("times new romen",15,"bold"),fg="white",bg="navyblue")
        password.place(x=100,y=235)

        self.txtpass=ttk.Entry(frame,font=("times new romen",15,"bold"))
        self.txtpass.place(x=40,y=265,width=270)

        #======Icon Images======
        img2=Image.open(r"C:\Users\mihir\Desktop\LOGIN_FORM\image\dd.png")
        img2= img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=680,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\mihir\Desktop\LOGIN_FORM\image\dd.png")
        img3= img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=680,y=410,width=25,height=25)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new romen",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new romen",10,"bold"),borderwidth=0,fg="white",bg="navyblue",activeforeground="white",activebackground="navyblue")
        registerbtn.place(x=15,y=350,width=160)

        #forgot password button
        loginbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new romen",10,"bold"),borderwidth=0,fg="white",bg="navyblue",activeforeground="white",activebackground="navyblue")
        loginbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    #=========password validation===============
    def validate_password(self, password):
        # Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password)
    
    
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required")
        elif not self.validate_password(self.txtpass.get()):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character")
        elif self.txtuser.get()=="fruit" and self.txtpass.get()=="Mango":
            messagebox.showinfo("Success","Welcome to our project Student Management System ")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sakec@1234",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()                                                                                        
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username And Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Student(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
        #============password vaildation================
    def validate_password(self, password):
        # Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password)


          #================= reset password=====================
            
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        elif not self.validate_password(self.txt_newpass.get()):
            messagebox.showerror("Error","Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sakec@1234",database="sys")
            my_cursor=conn.cursor()
            quary=("select * from register where email=%s and securityQ=%s and secorityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(quary,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has reset ,please login new password",parent=self.root2)
                self.root2.destroy()

    

          #===============forgot  password window=============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to resent password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sakec@1234",database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new romen",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new romen",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new romen",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new romen",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new romen",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new romen",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new romen",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new romen",20,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)






                    

            



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
         
      #===================variables==================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #======bg image=====
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\mihir\Desktop\LOGIN_FORM\image\new_add.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #======left image=====
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\mihir\Desktop\LOGIN_FORM\image\ass4.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=100,y=100,width=470,height=550)

        #=====main frame=======
        frame=Frame(self.root,bg="white")
        frame.place(x=570,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new romen",25,"bold"),fg="#37aba6",bg="white")
        register_lbl.place(x=20,y=20)

        #========label and entry======

        #===============row1
        fname=Label(frame,text="First Name",font=("times new romen",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new romen",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new romen",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new romen",15))
        self.txt_lname.place(x=370,y=130,width=250)


        #========================row2
        contact=Label(frame,text="Contact No",font=("times new romen",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new romen",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new romen",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new romen",15))
        self.txt_email.place(x=370,y=200,width=250)

        #=====================row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new romen",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new romen",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new romen",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new romen",15))
        self.txt_security.place(x=370,y=270,width=250)

        #====================row4
        pswd=Label(frame,text="Password",font=("times new romen",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new romen",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confim Password",font=("times new romen",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new romen",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #====================ckeak button====================
        self.var_ckeck=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_ckeck,text="I Agree The Terms And Conditons",font=("times new romen",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #====================buttons==================
        img=Image.open(r"C:\Users\mihir\Desktop\LOGIN_FORM\image\register.jpg")
        img = img.resize((200, 50), Image.BILINEAR)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new romen",15,"bold"))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\mihir\Desktop\LOGIN_FORM\image\ber.jpg")
        img1 = img1.resize((200, 50), Image.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new romen",15,"bold"))
        b1.place(x=330,y=420,width=200)

 #==================validation for contact number=======
    def validate_contact_number(self, number):
        pattern = r'^[0-9]{10}$'  # Matches 10 digits
        return re.match(pattern, number)
    
    #======================validation for email==========
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Basic email format
        return re.match(pattern, email)
    
    #===============vaildation to password=============
    def validate_password(self, password):
        # Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password)



    #================function declaration==================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Conform password must be same",parent=self.root)
        elif self.var_ckeck.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
        elif not self.validate_contact_number(self.var_contact.get()):
            messagebox.showerror("Error", "Invalid contact number",parent=self.root)
        elif not self.validate_email(self.var_email.get()):
            messagebox.showerror("Error", "Invalid email address",parent=self.root)
        elif not self.validate_password(self.var_pass.get()):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character", parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="Sakec@1234",database="sys")
           my_cursor=conn.cursor()
           query=("select*from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
                messagebox.showerror("Error","User already exist, please try another email",parent=self.root)
           else:
                my_cursor.execute("INSERT INTO register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()

                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()


# =================student management code======================

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

          
        # 1st
        img_2=Image.open(r"image\see.jpg")
        img_2=img_2.resize((510,160),Image.BICUBIC)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_1=Button(self.root,command=self.open_img,image=self.photoimg_2,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        # 2st
        img=Image.open(r"image\images (2).jpg")
        img=img.resize((510,160),Image.BICUBIC)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_2=Button(self.root,command=self.open_img_2,image=self.photoimg,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=160)

        # 3st
        img_3=Image.open(r"image\download.png")
        img_3=img_3.resize((510,160),Image.BICUBIC)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,command=self.open_img_3,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=1000,y=0,width=540,height=160)

        #=========bg image=============
        img_4=Image.open(r"image\ass6.jpg")
        img_4=img_4.resize((1530,710),Image.BICUBIC)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)

        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new romem",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)


        # manage frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=55,width=1500,height=560)

        
        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="STUDENT INFORMATION",font=("times new romem",12,"bold"),fg="purple",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=540)

        #img
        img_5=Image.open(r"image\ab.png")
        img_5=img_5.resize((650,120),Image.BICUBIC)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(self.root,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=33,y=250,width=650,height=150)

        # Current course LabelFrame Information
        std_lb1_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new romem",12,"bold"),fg="purple",bg="white")
        std_lb1_info_frame.place(x=0,y=150,width=650,height=115)

        #Labels and Combobox
        # department
        lb1_dep=Label(std_lb1_info_frame,text="Department:",font=("arial",12,"bold"),bg="white")
        lb1_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil","AIDS","ECS")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_std=Label(std_lb1_info_frame,font=("arial",12,"bold"),bg="white",text="Courses:")
        course_std.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        com_txtcourse_std=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_course,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        current_year=Label(std_lb1_info_frame,font=("arial",12,"bold"),bg="white",text="Year:")
        current_year.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        com_txt_current_year=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_year,font=("arial",12,"bold"),width=17,state="readonly")
        com_txt_current_year["value"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        current_semester=Label(std_lb1_info_frame,font=("arial",12,"bold"),bg="white",text="Semester:")
        current_semester.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        com_txt_current_semester=ttk.Combobox(std_lb1_info_frame,textvariable=self.var_semester,font=("arial",12,"bold"),width=17,state="readonly")
        com_txt_current_semester["value"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        com_txt_current_semester.current(0)
        com_txt_current_semester.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student ClassLabelFrame Information
        std_lb1_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Course Information",font=("times new romem",12,"bold"),fg="purple",bg="white")
        std_lb1_class_frame.place(x=0,y=265,width=650,height=250)

        #label entry
        #id
        lb1_id=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="StudentID:")
        lb1_id.grid(row=0,column=0,padx=2,pady=7,sticky=W)

        id_entry=ttk.Entry(std_lb1_class_frame,textvariable=self.va_std_id,font=("arial",12,"bold"),width=22)
        id_entry.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        #Name
        lb1_Name=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Student Name:")
        lb1_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(std_lb1_class_frame,textvariable=self.var_std_name,font=("arial",11,"bold"))
        txt_Name.grid(row=0,column=3,padx=2,pady=7,sticky=W)


        #Division
        lb1_Div=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Division:")
        lb1_Div.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        com_txt_div=ttk.Combobox(std_lb1_class_frame,textvariable=self.var_div,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_div["value"]=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        #Roll
        lb1_Roll=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Roll No:")
        lb1_Roll.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_Roll=ttk.Entry(std_lb1_class_frame,textvariable=self.var_roll,font=("arial",11,"bold"),width=22)
        txt_Roll.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        #gender
        lb1_gender=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Class Gender:")
        lb1_gender.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(std_lb1_class_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender["value"]=("Select Division","Male","Female")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #DOB
        lb1_dob=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="DOB:")
        lb1_dob.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(std_lb1_class_frame,textvariable=self.var_dob,font=("arial",11,"bold"),width=22)
        txt_dob.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #Email
        lb1_email=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Email:")
        lb1_email.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(std_lb1_class_frame,textvariable=self.var_email,font=("arial",11,"bold"),width=22)
        txt_email.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        #phone
        lb1_phone=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Phone No:")
        lb1_phone.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(std_lb1_class_frame,textvariable=self.var_phone,font=("arial",11,"bold"),width=22)
        txt_phone.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        #Address
        lb1_address=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Address:")
        lb1_address.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(std_lb1_class_frame,textvariable=self.var_address,font=("arial",11,"bold"),width=22)
        txt_address.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        #Teacher
        lb1_teacher=Label(std_lb1_class_frame,font=("arial",11,"bold"),bg="white",text="Mentor Name:")
        lb1_teacher.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_teacher=ttk.Entry(std_lb1_class_frame,textvariable=self.var_teacher,font=("arial",11,"bold"),width=22)
        txt_teacher.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #button frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=480,width=650,height=38)

        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_Reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Reset.grid(row=0,column=3,padx=1)



        #right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="STUDENT INFORMATION",font=("times new romem",12,"bold"),fg="purple",bg="white")
        DataRightFrame.place(x=690,y=10,width=800,height=540)

         #img1
        img_6=Image.open(r"image\abcd.png")
        img_6=img_6.resize((780,200),Image.BICUBIC)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img=Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)

        #right frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="SEARCH STUDENT INFORMATION",font=("times new romem",12,"bold"),fg="purple",bg="white")
        Search_Frame.place(x=0,y=200,width=790,height=70)

        
        search_by=Label(Search_Frame,font=("arial",11,"bold"),bg="white",text="Search By:",fg="purple")
        search_by.grid(row=0,column=0,padx=2,pady=7,sticky=W)

        # search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)

        com_txt_search["value"]=("Select Option","Roll","Phone","student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=2,pady=7)

        btn_search=Button(Search_Frame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=15,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_Showall=Button(Search_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),width=15,bg="blue",fg="white")
        btn_Showall.grid(row=0,column=4,padx=5)


        #STUDENT TABLE and scroll bar
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollno","gender","DOB","email","phoneno","address","mentorname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phoneno",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("mentorname",text="Mentor Name")

        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("mentorname",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# =============validation for email and password===========
    def validate_email(self, email):
        """
        Validate an email address using a regular expression.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def validate_phone_number(self, phone_number):
        """
        Validate a phone number using a regular expression.
        """
        pattern = r'^\+?[1-9]\d{1,14}$'
        return re.match(pattern, phone_number)

    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.va_std_id.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.validate_email(self.var_email.get()):
            messagebox.showerror("Error", "Invalid email address",parent=self.root)
        elif not self.validate_phone_number(self.var_phone.get()):
            messagebox.showerror("Error", "Invalid phone number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sakec@1234",database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get()

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    


        # fetch Funtion
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sakec@1234",database="mydata")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


        # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])


    def update_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.va_std_id.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sakec@1234",database="mydata")
                    my_cursur=conn.cursor()
                    my_cursur.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(
                                                                                                                                            self.var_dep.get(),
                                                                                                                                            self.var_course.get(),
                                                                                                                                            self.var_year.get(),
                                                                                                                                            self.var_semester.get(),
                                                                                                                                            self.var_std_name.get(),
                                                                                                                                            self.var_div.get(),
                                                                                                                                            self.var_roll.get(),
                                                                                                                                            self.var_gender.get(),
                                                                                                                                            self.var_dob.get(),
                                                                                                                                            self.var_email.get(),
                                                                                                                                            self.var_phone.get(),
                                                                                                                                            self.var_address.get(),
                                                                                                                                            self.var_teacher.get(),
                                                                                                                                            self.va_std_id.get()

                                                                                                                                            ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # delete 
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to delete this student",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sakec@1234",database="mydata")
                    my_cursur=conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.va_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your student has been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    # search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_com_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sakec@1234",database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursur.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # open image
    def open_img(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwdb(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img=Image.open(fln)
        img_browse=img.resize((510,160),Image.BICUBIC)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)

    # open image
    def open_img_2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwdb(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img_1=Image.open(fln)
        img_browse_1=img_1.resize((510,160),Image.BICUBIC)
        self.photoimg_browse_1=ImageTk.PhotoImage(img_browse_1)
        self.btn_2.config(image=self.photoimg_browse_1)

    # open image
    def open_img_3(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwdb(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img_2=Image.open(fln)
        img_browse_2=img_2.resize((510,160),Image.BICUBIC)
        self.photoimg_browse_2=ImageTk.PhotoImage(img_browse_2)
        self.btn_3.config(image=self.photoimg_browse_2)
             

            
if __name__ == "__main__":
    main()
    

