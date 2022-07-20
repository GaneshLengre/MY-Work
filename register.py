from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #=========== Variable ===========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sequrityQ=StringVar()
        self.var_sequrityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()




        #=======bg_image=======
        self.bg_image=ImageTk.PhotoImage(file="images/bg_image2.png")
        bg_lbl=Label(self.root,image=self.bg_image,bd=0,bg="white")
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #======= Main frame=======
        frame=Frame(self.root,bg="white",bd=0)
        frame.place(x=240,y=100,width=465,height=530)

        #=======Register details=======
        register_lbl=Label(frame,text="Resister Here",font=("time new roman",20,"bold"),bg="white",fg="#767171")
        register_lbl.place(x=0,y=0)

        # txt_username=Entry(frame,textvariable=self.username,font=("time new roman",15),bg="#ECECEC")
        # txt_username.place(x=50,y=140,width=250)

        #=======Label and entry=======
        fname=Label(frame,text="User Name",font=("time new roman",15),bg="white",fg="#767171")
        fname.place(x=0,y=50)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",15))
        self.fname_entry.place(x=150,y=50,width=250)

        l_name=Label(frame,text="Last Name",font=("time new roman",15),bg="white",fg="#767171")
        l_name.place(x=0,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",15))
        self.txt_lname.place(x=150,y=100,width=250)

        contact=Label(frame,text="Contact",font=("time new roman",15),bg="white",fg="#767171")
        contact.place(x=0,y=150)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",15))
        self.txt_contact.place(x=150,y=150,width=250)

        

        email=Label(frame,text=("Email"),font=("time new roman",15),bg="white",fg="#767171")
        email.place(x=0,y=200)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",15))
        self.txt_email.place(x=150,y=200,width=250)

        sequrity_Q=Label(frame,text="Select Sequrity Quetions",font=("time new roman",15),bg="white",fg="#767171")
        sequrity_Q.place(x=0,y=250)

        self.comb_sequrity_Q=ttk.Combobox(frame,textvariable=self.var_sequrityQ,font=("time new roman",13),state="readonly")
        self.comb_sequrity_Q["values"]=("Select","your pet name","Your Birth Place","Your School Name")
        self.comb_sequrity_Q.place(x=250,y=250,width=150)
        self.comb_sequrity_Q.current(0)

        sequrity_A=Label(frame,text="Sequrity Answer",font=("time new roman",15),bg="white",fg="#767171")
        sequrity_A.place(x=0,y=300)

        self.txt_sequrity_A=ttk.Entry(frame,textvariable=self.var_sequrityA,font=("time new roman",15))
        self.txt_sequrity_A.place(x=150,y=300,width=250)

        pass_=Label(frame,text="Password",font=("time new roman",15),bg="white",fg="#767171")
        pass_.place(x=0,y=350)

        self.txt_pass=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",15))
        self.txt_pass.place(x=150,y=350,width=250)

        confirm_pass=Label(frame,text="Confirm Pswd",font=("time new roman",15),bg="white",fg="#767171")
        confirm_pass.place(x=0,y=400)

        self.txt_confirm_pass=ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",15))
        self.txt_confirm_pass.place(x=150,y=400,width=250)

        #======= Check Button =======
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to all terms and conditions",font=("time new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=0,y=450)   

        #======= Buttons =======
        btn1=Button(frame,command=self.register_data,text="Register Now",font=("time new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=50,y=500)

        login_now=Button(frame,text="Login Now",font=("time new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=250,y=500)

        #======= Function Declaretion =======

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sequrityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to all terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ganesh",database="mydata1")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row!=None:
                messagebox.showerror("Error","Email already exists")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_sequrityQ.get(),
                                                                                            self.var_sequrityA.get(),
                                                                                            self.var_pass.get()
                                                                                         ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successful")

                   



if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

