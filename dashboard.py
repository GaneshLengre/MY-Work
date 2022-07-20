
from tkinter import*
from PIL import Image,ImageTk


class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("institute Management System | Developer By Python Developer")

        #======= Title ======
        title=Label(self.root,text="Institute Management System",font=("time new roman",40,"bold"),bg="#00B4D8",fg="black",anchor="w",padx=20,bd=4,relief=RIDGE)
        title.place(x=0,y=0,relwidth=1,height=70)

        # self.icon_title=ImageTk.PhotoImage(file="images/logo1.jpg")
        # title=Label(self.root,text="institute Management System",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#FF9F45",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #===== btn_logout ======
        btn_logout=Button(self.root,text="Logout",compound=RIGHT,font=("time new roman",15,"bold"),cursor="hand2",bg="#00B0F0",anchor="w",padx=20)
        btn_logout.place(x=1200,y=10,width=120,height=50)

        #========= Dashboard Frame =======
        frame1=Frame(self.root,bg="#00B4D8",bd=4,relief=RIDGE)
        frame1.place(x=0,y=70,width=310,height=630)

        frame2=Frame(self.root,bg="white",bd=4,relief=RIDGE)    #,relief=RIDGE
        frame2.place(x=310,y=70,width=1055,height=630)

      
        #========= Dashboard Frame1 Button =======
  
        dashb_btn1=Button(frame1,text="Enquiry",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn1.place(x=0,y=0,width=300,height=65)

        dashb_btn2=Button(frame1,text="Followup",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn2.place(x=0,y=70,width=300,height=65)

        dashb_btn3=Button(frame1,text="Students",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn3.place(x=0,y=140,width=300,height=65)

        dashb_btn4=Button(frame1,text="Collection",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn4.place(x=0,y=210,width=300,height=65)

        dashb_btn5=Button(frame1,text="Expenses",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn5.place(x=0,y=280,width=300,height=65)

        dashb_btn6=Button(frame1,text="Report",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn6.place(x=0,y=350,width=300,height=65)

        dashb_btn7=Button(frame1,text="Account",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn7.place(x=0,y=420,width=300,height=65)

        dashb_btn8=Button(frame1,text="Settings",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn8.place(x=0,y=490,width=300,height=65)

        dashb_btn9=Button(frame1,text="Log Out",font=("time new roman",15,"bold"),cursor="hand2",bg="#00B4D8",padx=20)
        dashb_btn9.place(x=0,y=560,width=300,height=65)

        

    


 




        

root=Tk()
obj=dashboard(root)
root.mainloop()
