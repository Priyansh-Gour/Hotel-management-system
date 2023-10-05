from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk



class CustomerWindow:
    def __init__(self,root) :
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220') 
                                # title
        Label_title=Label(self.root,text='Add Customer Details',font=('times new roman ',20,'bold'),bg="#052403",fg="gold",bd=4,relief=RIDGE)
        Label_title.place(x=0,y=0,width=1295,height=40)
                                # logo
        img2=Image.open(r"..\Hotel Management system\images\Logo.webp")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lable_img2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,border=0)
        lable_img2.place(x=0,y=0,width=100,height=40)

        # lable frame
        labelFrame_left=LabelFrame(self.root,border=2,relief=RIDGE,text="Customer Details",padx=2,font=('times new roman ',12,'bold'))
        labelFrame_left.place(x=5,y=50,width=425,height=490)

        # labels and entries
        custRef_label=Label(labelFrame_left,text="Customer Ref:",font=('times new roman ',12,'bold'),padx=2,pady=6)
        custRef_label.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        entry_ref.grid(row=0,column=1)


        cust_name=Label(labelFrame_left,text="Customer Name:",font=('times new roman ',12,'bold'),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        textName=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        textName.grid(row=1,column=1)


        mother_Name=Label(labelFrame_left,text="Mother Name:",font=('times new roman ',12,'bold'),padx=2,pady=6)
        mother_Name.grid(row=2,column=0,sticky=W)

        entry_mother=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        entry_mother.grid(row=2,column=1)


        gender=Label(labelFrame_left,text="Gender",font=('times new roman ',12,'bold'),padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)

        entry_gender=ttk.Combobox(labelFrame_left,width=27,font=('times new roman ',13,'bold'),state="readonly")
        entry_gender["value"]=("Male","Female","Other","Sandeep")
        entry_gender.current(0)
        entry_gender.grid(row=3,column=1)


        lblPostCode=Label(labelFrame_left,text="PostCode:",font=('times new roman ',12,'bold'),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        textPostCode=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        textPostCode.grid(row=4,column=1)


        mobileNumber=Label(labelFrame_left,text="Mobile:",font=('times new roman ',12,'bold'),padx=2,pady=6)
        mobileNumber.grid(row=5,column=0,sticky=W)

        textMobile=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        textMobile.grid(row=5,column=1)


        email_lbl=Label(labelFrame_left,text="Email:",font=('times new roman ',12,'bold'),padx=2,pady=6)
        email_lbl.grid(row=6,column=0,sticky=W)

        textEmail=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        textEmail.grid(row=6,column=1)


        lblNationality=Label(labelFrame_left,text="Nationality",font=('times new roman ',12,'bold'),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        entry_Nationality=ttk.Combobox(labelFrame_left,width=27,font=('times new roman ',13,'bold'),state="readonly")
        entry_Nationality["value"]=("India","European","America","British")
        entry_Nationality.current(0)
        entry_Nationality.grid(row=7,column=1)


        lblIDProof=Label(labelFrame_left,text="Id Proof Type :-",font=('times new roman ',12,'bold'),padx=2,pady=6)
        lblIDProof.grid(row=8,column=0,sticky=W)

        entry_Proof=ttk.Combobox(labelFrame_left,width=27,font=('times new roman ',13,'bold'),state="readonly")
        entry_Proof["value"]=("AdharCard","DrivingLicense","Passport")
        entry_Proof.current(0)
        entry_Proof.grid(row=8,column=1)


        lblIDNumber=Label(labelFrame_left,text="Id Number",font=('times new roman ',12,'bold'),padx=2,pady=6)
        lblIDNumber.grid(row=9,column=0,sticky=W)

        textIdNumber=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        textIdNumber.grid(row=9,column=1)


        lblAddress=Label(labelFrame_left,text="Address",font=('times new roman ',12,'bold'),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        textAddress=ttk.Entry(labelFrame_left,width=30,font=('times new roman ',13,'bold'))
        textAddress.grid(row=10,column=1)

        # button
        btn_Frame=Frame(labelFrame_left,border=2,relief=RIDGE)
        btn_Frame.place(x=0,y=400,width=412,height=40)

        btnADD=Button(btn_Frame,text="Add",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnADD.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_Frame,text="Update",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnReset=Button(btn_Frame,text="Reset",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnReset.grid(row=0,column=2,padx=1)

        btnDelete=Button(btn_Frame,text="Delete",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnDelete.grid(row=0,column=3,padx=1)

        #  label Frame
        TableFrame=LabelFrame(self.root,border=2,relief=RIDGE,text="View Details And Search System",padx=2,font=('times new roman ',12,'bold'))
        TableFrame.place(x=435,y=50,width=860,height=490)

        # search System
        lblSearchBY=Label(TableFrame,text="Search By",font=('times new roman ',12,'bold'),bg="red",fg="white")
        lblSearchBY.grid(row=0,column=0,sticky=W)

        combo_search=ttk.Combobox(TableFrame,width=24,font=('times new roman ',13,'bold'),state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        textAddress=Entry(TableFrame,width=29,font=('times new roman ',13,'bold'))
        textAddress.grid(row=0,column=2,padx=2)

        btnSearch=Button(TableFrame,text="Search",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(TableFrame,text="Show All",font=('times new roman ',12,'bold'),bg='black',fg='gold',width=9)
        btnShowAll.grid(row=0,column=4,padx=1)

        # To show data in Table
        dataFrame=LabelFrame(TableFrame,border=2,relief=RIDGE)
        dataFrame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(dataFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dataFrame,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(dataFrame,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No.")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)






        



if __name__=="__main__":
    root=Tk()
    obj=CustomerWindow(root)
    root.mainloop()