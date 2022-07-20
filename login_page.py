from re import M
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text=("Institute Management System"),font=("time new roman",40,"bold"),bg="#00B4D8",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)


        self.var_username=StringVar()
        self.var_password=StringVar()



        #======== login image ======

        self.login_image=ImageTk.PhotoImage(file="images/Login1.png")
        self.lbl_login_image=Label(self.root,image=self.login_image,bd=0).place(x=0,y=80,width=900,height=560)

        #====Login_frame====
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=900,y=110,width=350,height=500)

        #===== login title ======
        login_title=Label(login_frame,text=("Login System"),font=("Elephant",30,"bold"),bg="white")
        login_title.place(x=0,y=30,relwidth=1)

        #=====login_username=====
        login_user=Label(login_frame,text=("User name"),font=("time new roman",15),bg="white",fg="#767171")
        login_user.place(x=50,y=100)

        self.txtuser=ttk.Entry(login_frame,textvariable=self.var_username,font=("time new roman",15))
        self.txtuser.place(x=50,y=140,width=250)

        #=====login_password=====
        login_pass=Label(login_frame,text=("Password"),font=("time new roman",15),bg="white",fg="#767171")
        login_pass.place(x=50,y=200)


        self.txtpass=ttk.Entry(login_frame,textvariable=self.var_password,show="*",font=("time new roman",15))
        self.txtpass.place(x=50,y=240,width=250)

        #=====login_btn=====
        btn_login=Button(login_frame,text="Login In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2")
        btn_login.place(x=50,y=300,width=250,height=35)

        #===== Extra Label =========
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)

        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("time new roman",15)).place(x=150,y=355)

        #=====forgot password=====
        btn_forget=Button(login_frame,text="Forget Password",font=("time new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)


        #=====Register==
        btn_new_account=Button(login_frame,text="Create New Account",font=("time new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=90,y=420)

             # #====== frame2 ======
        # register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        # register_frame.place(x=900,y=550,width=350,height=60)
        # lbl_reg=Label(register_frame,text="Don't have an account?",font=("time new roman",13),bg="white").place(x=40,y=20)

        #===== Animation ======
        self.im1=ImageTk.PhotoImage(file="images/Login1.png")
        self.im2=ImageTk.PhotoImage(file="images/Login2.png")
        self.im3=ImageTk.PhotoImage(file="images/Login3.png")
        self.im4=ImageTk.PhotoImage(file="images/Login4.png")
        self.im5=ImageTk.PhotoImage(file="images/Login5.png")
        self.im6=ImageTk.PhotoImage(file="images/Login6.png")
        self.im7=ImageTk.PhotoImage(file="images/Login7.png")


        self.lbl_change_image=Label(self.root,image=self.im1,bd=0)
        self.lbl_change_image.place(x=0,y=80,width=900,height=560)

        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im4
        self.im4=self.im5
        self.im5=self.im6
        self.im6=self.im7
        self.im7=self.im


        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)

  
    def login(self):
        if self.var_username.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","All fields are required")
        
        # elif self.txt_username.get()!="Ganesh" or self.txt_pass.get()!="0709":
        #     messagebox.showerror("Error","Invalid username or Password\nTry again with correct credentionals")
        
        # elif self.var_username.get()=="Ganesh" and self.var_password.get()=="0709":
        #     messagebox.showerror("Success","Welcome to Successfully")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ganesh",database="mydata1")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into login values(%s,%s)",(self.var_username.get(),self.var_password.get()))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Login Successful")




if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()

