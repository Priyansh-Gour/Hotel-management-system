from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img_bg = Image.open(r"..\Hotel Management system\images\Login-bg.jpg")
        img_bg=img_bg.resize((1550,800),Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(img_bg)
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open("..\Hotel Management system\images\LoginIconAppl.png")
        img1 = img1.resize((100,100),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=100,height=100)

        get_start = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_start.place(x=95,y=100)

        username_lbl = Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.testUser = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.testUser.place(x=40,y=180,width=270)

        password_lbl = Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.passwordUser = ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.passwordUser.place(x=40,y=250,width=270)

        # icons
        img2 = Image.open("..\Hotel Management system\images\LoginIconAppl.png")
        img2 = img2.resize((25,25),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimg2,bg="black",borderwidth=0)
        lbl_img2.place(x=650,y=323,width=25,height=25)

        img3 = Image.open("..\Hotel Management system\images\kir.png")
        img3 = img3.resize((25,25),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimg3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=395,width=25,height=25)

        loginbtn=Button(frame,command=self.login, text="Login",font=("times new roman",20,"bold"),bd=3,relief=RAISED,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame, command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=15,y=350,width=160)

        btn_login=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        btn_login.place(x=10,y=370,width=160)

    def register_window(self):
          self.new_window = Toplevel(self.root)
          self.app = Register(self.new_window)

    def login(self):
        if self.testUser.get()=="" or self.passwordUser.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.testUser.get()=="Yogesh" and self.passwordUser.get()=="a":
            messagebox.showinfo("Welcome","Your are logged In")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s",(self.testUser.get(),self.passwordUser.get()))
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("error","Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()
    
    def forgot_password_window(self):
        if self.testUser.get()=="":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.testUser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="White")
                l.place(x=0,y=10,relwidth=1,)


                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.como_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.como_security_Q["values"]=("Select","Your Birth Place","Your Favorite Place","Your Pet Name")
                self.como_security_Q.place(x=50,y=110,width=250)          
                self.como_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn = Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

    def reset_password(self):
        if self.como_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter The answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("error","Please Enter the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
            my_cursor=conn.cursor()

            query = ("select * from register where email = %s and securityQ = %s and securityA = %s")
            value = (self.testUser.get(),self.como_security_Q.get(),self.txt_security.get())

            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("error","Please enter the correct Answer",parent=self.root2)
            else:
                query = ("update register set password = %s where email =%s ")
                value = (self.txt_new_password.get(),self.testUser.get())

                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Infor","Your password has been Reset,Please login new password",parent=self.root2)

                self.root2.destroy()

    

# register class
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        self.var_fname=StringVar()
        self.var_lname=StringVar()        
        self.var_contact=StringVar()        
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        img_bg = Image.open(r"..\Hotel Management system\images\Left-imgg.jpg")
        img_bg=img_bg.resize((1600,900),Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(img_bg)
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # leftImage
        img_left = Image.open(r"..\Hotel Management system\images\background.jpg")
        img_left=img_left.resize((470,550),Image.LANCZOS)

        self.bg1 = ImageTk.PhotoImage(img_left)
        lbl_bg1 = Label(self.root,image=self.bg1)
        lbl_bg1.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame, text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)   

    # label
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        #row1

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)


#row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

#row3

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.como_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.como_security_Q["values"]=("Select","Your Birth Place","Your Favorite Place","Your Pet Name")
        self.como_security_Q.place(x=50,y=270,width=250)          
        self.como_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)


#row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        # checkButton
        self.var_check=IntVar()
        self.var_checkbtn=Checkbutton(frame,text="I agree the Terms & conditions",variable=self.var_check,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.var_checkbtn.place(x=50,y=380)

        # buttons
        img=Image.open(r"..\Hotel Management system\images\register-now-button1.jpg")
        img=img.resize((200,55),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,font=("times new roman",15,"bold"),borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"..\Hotel Management system\images\loginpng.png")
        img1=img1.resize((200,45),Image.LANCZOS)    
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,command=self.return_login,image=self.photoimage1,font=("times new roman",15,"bold"),borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)

    # functions    
     
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
            my_cursor = conn.cursor()
            query=("select * from register where email = %s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("error","User already exists,please try another email")
            else:
                my_cursor.execute("INSERT INTO register VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (self.var_fname.get(), self.var_lname.get(), self.var_contact.get(),
                    self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get(),
                    self.var_pass.get()))
                

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()

if __name__ =="__main__":
    main()