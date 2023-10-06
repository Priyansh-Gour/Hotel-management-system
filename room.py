from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management system")
        self.root.geometry("1295x550+230+220")

        # Variables For Fetching Data
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # Title
        Label_title=Label(self.root,text='Room Booking',font=('times new roman ',20,'bold'),bg="#052403",fg="gold",bd=4,relief=RIDGE)
        Label_title.place(x=0,y=0,width=1295,height=40)

        # logo

        img2=Image.open(r"..\Hotel Management system\images\Logo.webp")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lable_img2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,border=0)
        lable_img2.place(x=0,y=0,width=100,height=40)

        # lable frame
        labelframeleft=LabelFrame(self.root,border=2,relief=RIDGE,text="RoomBooking Details",padx=2,font=('times new roman ',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # Entries

        #cust Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))   
        entry_contact.grid(row=0,column=1, sticky=W)

        # fetch data button
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)


        #Check in Date
        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("arial",13,"bold")) 
        txtcheck_in_date.grid(row=1,column=1)

        #check_out_date
        lbl_Check_out=Label(labelframeleft,text="Check_Out_date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("arial",13,"bold"))   #ttk used for stylish 
        txt_Check_out.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        # conn=mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
        # my_cursor=conn.cursor()
        # my_cursor.execute("select RoomType from details")
        # rows=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly") 
        combo_RoomType["value"]=("Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))  
        txtMeal.grid(row=5,column=1)

        #No of Days
        lblNoofDays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=6,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("arial",13,"bold"))  
        txtNoofDays.grid(row=6,column=1)


        #Paid Tax
        lblNoofDays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=7,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("arial",13,"bold"))  
        txtNoofDays.grid(row=7,column=1)


        #Sub Total
        lblNoofDays=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofDays.grid(row=8,column=0,sticky=W)
        txtNoofDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"))   
        txtNoofDays.grid(row=8,column=1)


        #Total Cost
        lblIdNumber=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("arial",13,"bold"))    
        txtIdNumber.grid(row=9,column=1)

        # buttton

        btnBill=Button(labelframeleft,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        btn_Frame=Frame(labelframeleft,border=2,relief=RIDGE)
        btn_Frame.place(x=0,y=400,width=412,height=40)

        btnADD=Button(btn_Frame,text="Add",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnADD.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_Frame,text="Update",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_Frame,text="Delete",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnDelete.grid(row=0,column=3,padx=1)
        btnReset=Button(btn_Frame,text="Reset",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnReset.grid(row=0,column=2,padx=1)

        # Right SideImage
        img3=Image.open(r"..\Hotel Management system\images\bed.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=300)

        # tTable Search System

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("arial",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=('times new roman ',12,'bold'),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")   
        combo_Serach["value"]=("Contact","Room")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)      

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(Table_Frame,text="Search",font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #======================Show Data Table=====================
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")        
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfdays")


        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)

        # self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        # self.fetch_data()

    # def get_cursor(self,event):
    #     cursor_row=self.room_table.focus()
    #     content=self.room_table.item(cursor_row)  #cursor_row is a variable
    #     row=content["values"]

    #     self.var_contact.set(row[0]),
    #     self.var_checkin.set(row[1]),
    #     self.var_checkout.set(row[2]),
    #     self.var_roomtype.set(row[3]),
    #     self.var_roomavailable.set(row[4]),
    #     self.var_meal.set(row[5]),        
    #     self.var_noofdays.set(row[6]),

    
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Details",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mypassword@123",database="hms")
            my_cursor=conn.cursor()
            query=("SELECT Name from customer WHERE Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter a Valid Number ",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,border=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                # for Displaying Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Mypassword@123",database="hms")
                my_cursor=conn.cursor()
                query=("SELECT Gender from customer WHERE Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                #for displaying Email
                conn=mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
                my_cursor=conn.cursor()   
                query=("SELECT Email FROM customer WHERE Mobile=%s")
                Value=(self.var_contact.get(),)
                my_cursor.execute(query,Value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #For Nationality

                conn=mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
                my_cursor=conn.cursor()   
                query=("select Nationality from customer where Mobile=%s")
                Value=(self.var_contact.get(),)
                my_cursor.execute(query,Value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)


                # for Addres
                conn=mysql.connector.connect(host="localhost",user="root",password="Mypassword@123",database="hms")
                my_cursor=conn.cursor()   
                query=("select Address from customer where Mobile=%s")
                Value=(self.var_contact.get(),)
                my_cursor.execute(query,Value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)






if __name__=='__main__':
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()     