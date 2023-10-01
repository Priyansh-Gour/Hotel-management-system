from tkinter import *
from PIL import Image,ImageTk




class HotelManagementSystem:
    def __init__(self,root) :
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')

        # First image
        img1=Image.open(r"C:\Users\priya\OneDrive\Desktop\My programs\py.programs\Hotel Management system\images\hotel1.webp")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lable_img1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lable_img1.place(x=0,y=0,width=1550,height=140)

        # Logo
        img2=Image.open(r"C:\Users\priya\OneDrive\Desktop\My programs\py.programs\Hotel Management system\images\Logo.webp")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lable_img2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lable_img2.place(x=0,y=0,width=230,height=140)

        # Title
        Label_title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('times new roman ',40,'bold'),bg="black",fg="gold",bd=4,relief=RIDGE)
        Label_title.place(x=0,y=140,width=1550,height=50)


        # frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        # menu
        lable_menu=Label(main_frame,text='MENU',font=('times new roman ',20,'bold'),bg="black",fg="gold",bd=4,relief=RIDGE)
        lable_menu.place(x=0,y=0,width=230)

        # button
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="Customer",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="Room",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        detail_btn=Button(btn_frame,text="Details",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        detail_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="Report",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logOut_btn=Button(btn_frame,text="Log Out",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logOut_btn.grid(row=4,column=0,pady=1)

        # right image
        img3=Image.open(r"C:\Users\priya\OneDrive\Desktop\My programs\py.programs\Hotel Management system\images\hotel1.webp")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lable_img3=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lable_img3.place(x=225,y=0,width=1310,height=590)

if __name__=='__main__':
    root= Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()     