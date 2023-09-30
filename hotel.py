from tkinter import *
from PIL import Image,ImageTk




class HotelManagementSystem:
    def __init__(self,root) :
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')

        # First image
        img1=Image.open(r"C:\Users\priya\OneDrive\Desktop\My programs\py.programs\hms\hotel\hotel1.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lable_img1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lable_img1.place(x=0,y=0,width=1550,height=140)

        # Logo
        img2=Image.open(r"C:\Users\priya\OneDrive\Desktop\My programs\py.programs\hms\hotel\logohotel.png")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img1)

        lable_img2=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lable_img2.place(x=0,y=0,width=230,height=140)



if __name__=='__main__':
    root= Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()     