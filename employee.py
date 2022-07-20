# from cgitb import text
# from logging import exception
# from math import comb
# from multiprocessing.sharedctypes import Value
# from pyclbr import Function
# from re import L
# from sqlite3 import Cursor
# from textwrap import fill
#from this import s
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
# from tokenize import String
# from turtle import update
from PIL import Image,ImageTk
#from django.db import connection
import mysql.connector
# import sys
# import os



class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title('Employee Management System')
        self.root.configure(background = "light green")


        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()




        lb1_title = Label(self.root, text = 'EMPLOYEE MANAGEMENT SYSTEM', fg = 'white', bg = '#146356', font = ('Montserrat', 37, 'bold' ))
        lb1_title.place(x = 0, y = 0, width = 1530, height = 50)

        # logo
        img_logo_1 = Image.open("college_images/lobo1.jpg")
        img_logo_1 = img_logo_1.resize((50, 50), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo_1)

        self.lobo = Label(self.root, image = self.photo_logo)
        self.lobo.place(x = 270, y = 0, width = 50, height = 50)

        # image frame
        img_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'white')
        img_frame.place(x = 0, y = 50, width = 1530, height = 160)

        # 1st image
        img1 = Image.open("college_images/emp1.jpg")
        img1 = img1.resize((540, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image=self.photo1)
        self.img_1.place(x = 0, y = 0, width = 540, height = 160)

        # 2nd image
        img2 = Image.open("college_images/emp2.jpg")
        img2 = img2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image = self.photo2)
        self.img_2.place(x = 540, y = 0, width = 540, height = 160)

        # 3rd image
        img3 = Image.open("college_images/emp3.jpg")
        img3 = img3.resize((540,160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image = self.photo3)
        self.img_3.place(x = 1000, y = 0, width = 540, height = 160)

        # main Frame
        Main_frame = Frame(self.root, bd = 2, relief = RIDGE, bg = 'white')
        Main_frame.place(x = 10, y = 220, width = 1500, height = 560)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd = 2, relief = RIDGE, bg = 'white', fg ='red', text = 'Employee Information', font = ('times new roman', 11, 'bold'))
        upper_frame.place(x = 10 , y = 10 , width = 1480 , height = 270 )

        # Labels and Entry Fields
        lb1_dep = Label(upper_frame , text = 'Department', font = ('arial', 11, 'bold' ), bg = 'white')
        lb1_dep.grid(row = 0, column = 0, padx = 2, sticky = W )

        combo_dep = ttk.Combobox(upper_frame, textvariable = self.var_dep, font = ('arial', 11, 'bold'), width = 22, state = 'random')
        combo_dep['value'] = ('Select Department', 'HR', 'Software Engineer', 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        # Name
        lb1_name = Label(upper_frame, text = 'Name', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_name.grid(row = 0, column = 2, padx = 2, pady = 7, sticky = W)

        txt_name = ttk.Entry(upper_frame, textvariable = self.var_name, font = ('arial', 11, 'bold'), width = 22)
        txt_name.grid(row = 0, column = 3, padx = 2, pady = 7)

        # Label Designition
        lb1_designition = Label(upper_frame, text='Designition', font=('arial', 12, 'bold'), bg = 'white')
        lb1_designition.grid(row = 1, column = 0, padx = 2, sticky = W, pady = 7)

        txt_designition = ttk.Entry(upper_frame, textvariable = self.var_designition, font = ('arial', 11, 'bold'), width = 22)
        txt_designition.grid(row = 1, column = 1, padx = 2, pady = 7, sticky = W)

        # Email
        lb1_email = Label(upper_frame,text = 'Email', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_email.grid(row = 1, column = 2, padx = 2, sticky = W, pady = 7)

        txt_email = ttk.Entry(upper_frame, textvariable = self.var_email, font = ('arial', 11, 'bold'), width = 22)
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lb1_adress = Label(upper_frame, text = 'Address', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_adress.grid(row = 2, column = 0, padx = 2, sticky = W, pady = 7)

        txt_address = ttk.Entry(upper_frame, textvariable = self.var_address, font = ('arial', 11, 'bold'), width = 22)
        txt_address.grid(row = 2, column = 1, padx = 2, pady = 7)

        # Married 
        lb1_merried_status = Label(upper_frame, text = 'Married States', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_merried_status.grid(row = 2, column = 2,padx = 2, sticky = W, pady = 7)

        com_txt_merried = ttk.Combobox(upper_frame, textvariable = self.var_married, state = "readonly", font=('arial', 11, 'bold'), width = 22)

        com_txt_merried['value'] = ('Married', 'Unmarried')
        com_txt_merried.current(0)
        com_txt_merried.grid(row = 2, column = 3, sticky = W, padx = 2, pady = 7)

        # Date of Birth
        lb1_dob = Label(upper_frame, text = 'DOB', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_dob.grid(row = 3, column = 0, padx = 2, sticky = W, pady = 7)

        txt_dob = ttk.Entry(upper_frame, textvariable = self.var_dob, font = ('arial', 11, 'bold'), width = 22)
        txt_dob.grid(row = 3, column = 1, padx = 2, pady = 7)

        # Date of Joining
        lb1_doj = Label(upper_frame, text = 'DOJ', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_doj.grid(row = 3, column = 2, padx = 2, sticky = W, pady = 7)

        txt_doj = ttk.Entry(upper_frame, textvariable = self.var_doj, font = ('arial', 11, 'bold'), width = 22)
        txt_doj.grid(row = 3, column = 3, padx = 2, pady = 7)

        # Id Proof
        com_txt_proof = ttk.Combobox(upper_frame, textvariable = self.var_idproofcomb, state = "readonly", font = ('arial', 12, 'bold'), width = 22)

        com_txt_proof['value'] = ("Select ID Proof", "PAN CARD", "ADHAR CARD", "DRIVING LICEN")
        com_txt_proof.current(0)
        com_txt_proof.grid(row = 4, column = 0, padx = 2, sticky = W, pady = 7)

        txt_proof = ttk.Entry(upper_frame, textvariable = self.var_idproof, font = ('arial', 11, 'bold'), width = 22)
        txt_proof.grid(row = 4, column = 1, padx = 2, pady = 7)

        # combo_txt_proof=ttk.Combobox(upper_frame,state="readonly",font=('arial',11,'bold'),width=22)
        # combo_txt_proof.grid(row=4,column=0,padx=2,pady=7)
        # combo_txt_proof['value']=('Select ID Proof',"PAN CARD","ADHAR CARD","DRIVING LICEN")
        # combo_txt_proof.current(0)
        # txt_proof=ttk.Entry(upper_frame,font=('arial',11,'bold'),width=22)
        # txt_proof.grid(row=4,column=1,padx=2,pady=7)

        # gender
        lb1_gender = Label(upper_frame, text='Gender', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_gender.grid(row = 4, column = 2, padx = 2, sticky = W, pady = 7)

        com_txt_gender = ttk.Combobox(upper_frame, textvariable = self.var_gender, state = "readonly", font = ('arial', 12, 'bold'), width = 22)

        com_txt_gender['value'] = ('Male', 'Female', "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row = 4, column = 3, sticky = W, padx = 2, pady = 7)

        
        # Phone 
        lb1_phone = Label(upper_frame, text = 'Phone No:', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_phone.grid(row = 0, column = 4, padx = 2, sticky = W, pady = 7)

        txt_phone = ttk.Entry(upper_frame, textvariable = self.var_phone, font = ('arial', 11, 'bold'), width = 22)
        txt_phone.grid(row = 0, column = 5, padx = 2, pady = 7)

        
        # Country
        lb1_country = Label(upper_frame, text = 'Country', font = ('arial', 12, 'bold'), bg = 'white')
        lb1_country.grid(row = 1, column = 4, padx = 2, sticky = W, pady = 7)

        txt_country = ttk.Entry(upper_frame, textvariable = self.var_country, font = ('arial', 11, 'bold'), width = 22)
        txt_country.grid(row = 1, column = 5, padx = 2, pady = 7)

        
        # CTC
        lb1_ctc = Label(upper_frame, text = 'Salary(CTC):', font  =('arial', 12, 'bold'), bg = 'white')
        lb1_ctc.grid(row = 2, column = 4,padx = 2, sticky = W, pady = 7)

        txt_ctc = ttk.Entry(upper_frame, textvariable = self.var_salary, font = ('arial', 11, 'bold'), width = 22)
        txt_ctc.grid(row = 2, column = 5, padx = 2, pady = 7)

        # #Mask image
        # img_mask=Image.open("college_images/mask.jpg")
        # img_mask=img_mask.resize((220,220),Image.ANTIALIAS)
        # self.photo_mask=ImageTk.PhotoImage(img_mask)

        # self.img_2=Label(upper_frame,image=self.photo_mask)
        # self.img_2.place(x=1000,y=0,width=220,height=220)

        # Button Frame
        button_frame = Frame(upper_frame, bd = 2, relief = RIDGE, bg = 'white')
        button_frame.place(x = 1150, y = 10, width = 170, height = 210)

        btn_add = Button(button_frame, text = "save", command = self.add_data, bg = '#f3c892', fg = 'white', font = ('arial', 15, 'bold'), width = 13)
        btn_add.grid(row = 0, column = 0,padx = 1, pady = 5)

        btn_update = Button(button_frame, text = "Update", command = self.update_data, bg = '#595260', fg = 'white', font = ('arial', 15, 'bold'), width = 13)
        btn_update.grid(row = 1, column = 0, padx = 1, pady = 5)

        btn_delete = Button(button_frame, text = "Delete", command = self.delete_data, bg = 'blue', fg = 'white', font = ('arial', 15, 'bold'), width = 13)
        btn_delete.grid(row = 2, column = 0, padx = 1, pady = 5)

        btn_clear = Button(button_frame, text = "Clear", command = self.reset_data, bg = 'blue', fg = 'white', font = ('arial', 15, 'bold'), width = 13)
        btn_clear.grid(row = 3, column = 0, padx = 1, pady = 5)



        # down Frame
        down_frame = LabelFrame(Main_frame, bd = 2, relief = RIDGE, bg = 'white', fg = 'blue', text = 'Employee Information Table', font = ('times new roman', 11, 'bold'))
        down_frame.place(x = 10, y = 280, width = 1480, height = 270)

        # Search Frame
        search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',fg='blue',text='Search Employee Information',font=('times new roman',11,'bold'))
        search_frame.place(x = 0,y = 0, width = 1470, height = 60)

        search_by = Label(search_frame, bg = 'red', fg = 'white', text = 'Search By:', font = ('times new roman', 11, 'bold'))
        search_by.grid(row = 0, column = 0, sticky = W, padx = 5)

        # Search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable = self.var_com_search, state = "readonly", font = ('arial', 12, 'bold'), width = 18)

        com_txt_search['value'] = ("Select Option", "Phone", "id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row = 0, column = 1, padx = 5, sticky = W)
        
        self.var_search = StringVar()

        com_txt_search = ttk.Entry(search_frame, textvariable = self.var_search, font = ('arial', 11, 'bold'), width = 22)
        com_txt_search.grid(row = 0, column = 2, padx = 5)

        btn_search = Button(search_frame, text = "Search", command = self.search_data, bg = 'blue', fg = 'white', font = ('arial', 11, 'bold'), width = 14)
        btn_search.grid(row = 0, column = 3, padx = 5)

        btn_showall = Button(search_frame, text = "Show All", command = self.fetch_data, bg = 'blue', fg = 'white', font = ('arial', 11, 'bold'), width = 14)
        btn_showall.grid(row = 0, column = 4, padx = 5)

        stayhome = Label(search_frame, bg = 'white', fg = 'red', text = 'Wear a Mask', font = ('times new roman', 30, 'bold'))
        stayhome.place(x = 780,y = 0, width = 600, height = 30)

        img_logo_mask = Image.open(r"college_images/mask.jpg")
        img_logo_mask = img_logo_mask.resize((50, 50), Image.ANTIALIAS)
        self.photoimg_logo_mask = ImageTk.PhotoImage(img_logo_mask)

        self.lobo = Label(search_frame, image = self.photoimg_logo_mask)
        self.lobo.place(x = 900, y = 0, width = 50, height = 30)


        #=========== Employee Table =============

        # Table Frame
        table_frame = Frame(down_frame, bd = 3, relief = RIDGE)
        table_frame.place(x = 0, y = 60, width = 1470, height = 170)

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, columns = ("dep", "name", "degi", "email", "address", "married", "dob", "doj", "idproofcomb", "idproof", "gender", "phone", "country", "salary",), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        
        scroll_x.config(command = self.employee_table.xview)
        scroll_y.config(command = self.employee_table.yview)

        self.employee_table.heading('dep', text = 'Department')
        self.employee_table.heading('name', text = 'Name')
        self.employee_table.heading('degi' ,tex = 'Degignition')
        self.employee_table.heading('email', text = 'Email')
        self.employee_table.heading('address', text = 'Address')
        self.employee_table.heading('married', text = 'Married States')
        self.employee_table.heading('dob', text = 'DOB')
        self.employee_table.heading('doj', text = 'DOJ')
        self.employee_table.heading('idproofcomb', text = 'Select ID Proof')
        self.employee_table.heading('idproof', text = 'Select Option')
        self.employee_table.heading('gender', text = 'Gender')
        self.employee_table.heading('phone', text = 'Phone')
        self.employee_table.heading('country', text = 'Country')
        self.employee_table.heading('salary', text ='Salary')

        self.employee_table['show'] = 'headings'

        self.employee_table.column("dep", width = 100)
        self.employee_table.column("name", width = 100)
        self.employee_table.column("degi", width = 100)
        self.employee_table.column("email", width = 100)
        self.employee_table.column("address", width = 100)
        self.employee_table.column("married", width = 100)
        self.employee_table.column("dob", width = 100)
        self.employee_table.column("doj", width = 100)
        self.employee_table.column("idproofcomb", width = 100)
        self.employee_table.column("idproof", width = 100)
        self.employee_table.column("gender", width = 100)
        self.employee_table.column("phone", width = 100)
        self.employee_table.column("phone", width = 100)
        self.employee_table.column("country", width = 100)
        self.employee_table.column("salary", width = 100)
        
        self.employee_table.pack(fill = BOTH, expand = 1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # ************************* Function Declarations **********************
    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
             messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host = 'localhost', username = 'root', password = 'Ganesh', database = 'employee')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into emp values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_designition.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_idproofcomb.get(),
                                                                                                                self.var_idproof.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_salary.get()



                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showerror('Success', 'Employee has been added!', parent = self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent = self.root)


    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host = 'localhost', username = 'root', password = 'Ganesh', database = 'employee')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from emp')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values = i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self, event = ""):
        Cursor_row = self.employee_table.focus()
        content = self.employee_table.item(Cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
             messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'are sure update this employee data')
                if update > 0:
                    conn=mysql.connector.connect(host = 'localhost', username = 'root', password = 'Ganesh', database = 'employee')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update emp set Deparment=%s, Name=%s, Designition=%s, Email=%s, Address=%s, Married_status=%s, DOB=%s, DOJ=%s, id_proof_type=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s where id_proof=%s', (
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_designition.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_married.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_doj.get(),
                                                                                                                                                                                                                            self.var_idproofcomb.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_country.get(),
                                                                                                                                                                                                                            self.var_salary.get(),
                                                                                                                                                                                                                            self.var_idproof.get()

                                                                                                                                                                                                                             ))
                
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo('Success', 'Employee Successfully updated', parent = self.root)
            
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent = self.root)

    def delete_data(self):
        if self.var_idproof.get() == "":
            messagebox.showerror('Error', "All Field are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete', 'Are you sure delete this employee', parent = self.root)
                if Delete > 0:
                    conn=mysql.connector.connect(host = 'localhost', username = 'root', password = 'Ganesh', database = 'employee')
                    my_cursor = conn.cursor()
                    sql = 'delete from emp where id_proof=%s'
                    value = (self.var_idproof.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Employee Successfully Deleted',parent = self.root)
            
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent = self.root)                                                                                                                                                                                                                                         

    def reset_data(self):

        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    #Search
    def search_data(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', "Ple select option")
        else:
            try:
                conn=mysql.connector.connect(host = 'localhost', username = 'root', password = 'Ganesh', database = 'employee')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from emp where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values = i)
                    conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}', parent = self.root)                                                                                                                                                                                                                                         


if __name__=="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
    