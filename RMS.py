import tkinter as tk             #importing all necessary packages
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import math,random
import os
import pymysql                   #importing pymysql library
from PIL import Image,ImageTk    #importing image library
root=tk.Tk()
root.geometry("1530x800+0+0") #dimensions of the homescreen, set according to your pc/laptop
root.title("Retail Management System") #you can put any title here of your choice, this is your app title
root.iconbitmap("../RMS/res/billingsoftwareicon.ico") #app image/logo
global uname,Password,aname,apassword,clicked,clicked1,clicked2,q,custname,custphone,custbillno,cname_text,cphn_text,quantitye,ID,pname,pcategory,psubcategory,pquantity,pprice,pnamee,pcategorye,psubcategorye,pquantitye,ppricee,EID,empname,empcontact,empaddress,empaadhar,empusername,emppassword,f_uname,adharno,f_pname,f_pname1
uname=StringVar()       #String type variables used to store data retreived from databases
Password=StringVar()
aname=StringVar()
apassword=StringVar()
f_uname = StringVar()
adharno = StringVar()    #you can use any unique identification code of your country to indentify an individual
q=IntVar()                    #int type as quantity is stored
custname = StringVar()
custphone = StringVar()
custbillno = StringVar()
x=random.randint(10000,99999) #selects a random number to name a particular bill
custbillno.set(str(x))
custbillsearch = StringVar()
ID = IntVar()                
BID = StringVar()
pname = StringVar()
pcategory = StringVar()
psubcategory = StringVar()
pquantity = StringVar()
pprice = StringVar()
EID = IntVar()
empname = StringVar()
empcontact = StringVar()
empaddress = StringVar()
empaadhar = StringVar()
empusername = StringVar()
emppassword = StringVar()
f_pname = StringVar()
f_pname1 = StringVar()
def home():
    os.chdir("../RMS")         #opens the directory folder RMS in this case
    uname.set("")
    Password.set("")
    aname.set("")
    apassword.set("")
    #you can just toggle around with things here below as these are all are a part of ui
    global background, bgimg,my_button1,b1,my_button2,my_label1 ,l1,f1background,f1login,f1back,f1logout,f2search,atc,clear,remove,Exit,generate,total,employees_button,inventory_button,invoices_button,aboutus_button,logout,search,addproduct,updateproduct,deleteproduct,showallproducts,addemployee,updateemployee,removeemployee,showallemployees,Exita,add,cleara,update1,quantitye,viewbill,showallbills,deletebill,forgot,go
    background = ImageTk.PhotoImage(Image.open("../RMS/res/bg.jpg"))
    bgimg= tk.Label(root,image=background)
    bgimg.place(x=0,y=0)   
    my_button1 = ImageTk.PhotoImage(Image.open("../RMS/res/emp.png"))
    b1= tk.Button(root,bd=0,image=my_button1,bg="#FEFEFE",activebackground="#FEFEFE",command=employee)
    b1.place(x=620,y=350)

    my_button2 = ImageTk.PhotoImage(Image.open("../RMS/res/admin.png"))
    b1= tk.Button(root,bd=0,image=my_button2,bg="#FEFEFE",activebackground="#FEFEFE",command=admin)
    b1.place(x=770,y=350)
    #retreibing all images from res folder in individual variables
    my_label1 = ImageTk.PhotoImage(Image.open("../RMS/res/login.png"))
    l1= tk.Label(root,bd=15,image=my_label1,bg="purple")
    l1.place(x=560,y=120)
    f1background = ImageTk.PhotoImage(Image.open("../RMS/res/img.jpg"))
    f1login= ImageTk.PhotoImage(Image.open("../RMS/res/loginbutton.png"))
    go = ImageTk.PhotoImage(Image.open("../RMS/res/go.png"))
    f1back= ImageTk.PhotoImage(Image.open("../RMS/res/backbutton.png"))
    f1logout= ImageTk.PhotoImage(Image.open("../RMS/res/logoutbutton.png"))
    f2search= ImageTk.PhotoImage(Image.open("../RMS/res/searchbutton.png"))
    atc = ImageTk.PhotoImage(Image.open("../RMS/res/atcbutton.png"))
    clear= ImageTk.PhotoImage(Image.open("../RMS/res/clearbutton.png"))
    Exit= ImageTk.PhotoImage(Image.open("../RMS/res/exitbutton.png"))
    remove= ImageTk.PhotoImage(Image.open("../RMS/res/removebutton.png"))
    generate= ImageTk.PhotoImage(Image.open("../RMS/res/generatebutton.png"))
    total= ImageTk.PhotoImage(Image.open("../RMS/res/totalbutton.png"))
    employees_button = ImageTk.PhotoImage(Image.open("../RMS/res/employees.png"))
    inventory_button = ImageTk.PhotoImage(Image.open("../RMS/res/inventory.png"))
    invoices_button = ImageTk.PhotoImage(Image.open("../RMS/res/invoices.png"))
    aboutus_button = ImageTk.PhotoImage(Image.open("../RMS/res/aboutus.png"))
    logout = ImageTk.PhotoImage(Image.open("../RMS/res/logout.png"))
    search= ImageTk.PhotoImage(Image.open("../RMS/res/search.png"))
    addproduct = ImageTk.PhotoImage(Image.open("../RMS/res/addproduct.png"))
    updateproduct = ImageTk.PhotoImage(Image.open("../RMS/res/update.png"))
    deleteproduct = ImageTk.PhotoImage(Image.open("../RMS/res/delete.png"))
    showallproducts = ImageTk.PhotoImage(Image.open("../RMS/res/showall.png"))
    
    addemployee = ImageTk.PhotoImage(Image.open("../RMS/res/adde.png"))
    updateemployee = ImageTk.PhotoImage(Image.open("../RMS/res/updatee.png"))
    removeemployee = ImageTk.PhotoImage(Image.open("../RMS/res/removee.png"))
    showallemployees = ImageTk.PhotoImage(Image.open("../RMS/res/showalle.png"))
    add = ImageTk.PhotoImage(Image.open("../RMS/res/add.png"))
    cleara = ImageTk.PhotoImage(Image.open("../RMS/res/clear.png"))
    Exita = ImageTk.PhotoImage(Image.open("../RMS/res/exita.png"))
    update1 = ImageTk.PhotoImage(Image.open("../RMS/res/update1.png"))

    viewbill = ImageTk.PhotoImage(Image.open("../RMS/res/viewb.png"))
    showallbills = ImageTk.PhotoImage(Image.open("../RMS/res/showallb.png"))
    deletebill = ImageTk.PhotoImage(Image.open("../RMS/res/deleteb.png"))

    forgot = ImageTk.PhotoImage(Image.open("../RMS/res/forgot pass.png"))
#function to reset admin variables
def admin_del():
    aus.delete(0,END)
    aps.delete(0,END)
    admin()   #calling admin function
#admin function creates the ui of admin page when you click admin button on the homescreen
def admin():
    global aus,aps
    f1=Frame()
    f1.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f1,image=f1background)
    f2 = Frame(f1,bg="white",bd=5,pady=2)
    f2.place(x=500,y=100,width=550,height=600)
    bgimg.place(x=0,y=0) 
    l1= Label(f2,bd=15,text="Admin Login",font=("Calibri",30,"bold"),bg="white")
    l1.place(x=145,y=20)
    us= Label(f2,bd=15,text="Username",font=("Calibri",20,"bold"),bg="white")
    us.place(x=190,y=100)
    aus=Entry(f2,bd=5,textvariable=aname,font=("Calibri",20),bg="white",width=20,fg="black")
    aus.place(x=120,y=160)
    ps= Label(f2,bd=15,text="Password",font=("Calibri",20,"bold"),bg="white")
    ps.place(x=190,y=220)
    aps=Entry(f2,show="*",textvariable=apassword,bd=5,font=("Calibri",20,"bold"),bg="white",width=20,fg="black")
    aps.place(x=120,y=280)
    lb=Button(f2,image=f1login,bd=0,bg="#FFFFFF",command=adminlogin)
    lb.place(x=150,y=400)
    rb=Button(f2,image=f1back,bd=0,bg="#FFFFFF",command=home)
    rb.place(x=100,y=450)
#same thing as admin
def employee_del():
    eus.delete(0,END)
    eps.delete(0,END)
    employee()
#same as admin
def employee():
    global eus,eps
    f1=Frame()
    f1.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f1,image=f1background)
    bgimg.place(x=0,y=0) 
    f2 = Frame(f1,bg="white",bd=5,pady=2)
    f2.place(x=500,y=100,width=550,height=600)
    l1= Label(f2,bd=15,text="Login",font=("Calibri",30,"bold"),bg="white")
    l1.place(x=200,y=20)
    us= Label(f2,bd=15,text="Username",font=("Calibri",20,"bold"),bg="white")
    us.place(x=190,y=100)
    eus=Entry(f2,bd=5,textvariable=uname,font=("Calibri",20),bg="white",width=20,fg="black")
    eus.place(x=120,y=160)
    ps= Label(f2,bd=15,text="Password",font=("Calibri",20,"bold"),bg="white")
    ps.place(x=190,y=220)
    eps=Entry(f2,show="*",textvariable=Password,bd=5,font=("Calibri",20,"bold"),bg="white",width=20,fg="black")
    eps.place(x=120,y=280)
    lb=Button(f2,image=f1login,bd=0,bg="#FFFFFF",command=emplogin)
    lb.place(x=150,y=400)
    rb=Button(f2,image=f1back,bd=0,bg="#FFFFFF",command=home)
    rb.place(x=100,y=450)

    fpb = Button(f2,image=forgot,bd=0,bg="#FFFFFF",command = forgot_password)
    fpb.place(x=125,y=500)
#forgot password section for employees
def forgot_password():
    global flag1,cp1
    flag1=0
    cp1 = Toplevel(root)
    cp1.geometry("1000x700+0+0")
    cp1.title("Change Password")
    bgimg= Label(cp1,image=f1background)
    bgimg.place(x=0,y=0) 
    f2 = Frame(cp1,bg="white")
    f2.place(x=260,y=100,width=450,height=500)
    us= Label(f2,bd=15,text="Enter Username:",font=("Calibri",20),bg="white")
    us.place(x=110,y=50)
    eus=Entry(f2,bd=5,textvariable=f_uname,font=("Calibri",20),bg="white",width=20,fg="black")
    eus.place(x=75,y=110)
    #in place of adhar you can use any indentification critera
    us= Label(f2,bd=15,text="Enter Aadhar Number:",font=("Calibri",20),bg="white")
    us.place(x=85,y=170)
    eus=Entry(f2,bd=5,textvariable=adharno,font=("Calibri",20),bg="white",width=20,fg="black")
    eus.place(x=75,y=230)
    gob=Button(f2,image=go,bd=0,bg="#FFFFFF",command=go_to)
    gob.place(x=165,y=350)
#fetching data from the database and validating it
def go_to():
    global cp
    con=pymysql.connect(host="localhost",user="root",password='',database="employee_management")
    sql = "select * from employee"
    cur=con.cursor()
    cur.execute(sql)
    dt = cur.fetchall()
    if f_uname.get()=="" or adharno.get()=="":
        messagebox.showerror("error","All Fields Are Required!")
    else:
        for i in dt:
            if f_uname.get()==i[5] and adharno.get()==i[4]:
                flag1 = 1
                messagebox.showinfo("Success!","User Found")
                cp1.destroy()
                cp = Toplevel(root)
                cp.geometry("1000x700+30+20")
                cp.title("Change Password")    
                bgimg= Label(cp,image=f1background)
                bgimg.place(x=0,y=0) 
                f2 = Frame(cp,bg="white")
                f2.place(x=260,y=100,width=450,height=500)
                us= Label(f2,bd=15,text="Enter New Password:",font=("Calibri",20),bg="white")
                us.place(x=90,y=50)
                eus=Entry(f2,bd=5,textvariable=f_pname,font=("Calibri",20),bg="white",width=20,fg="black")
                eus.place(x=75,y=110)
                us= Label(f2,bd=15,text="Confirm New Password:",font=("Calibri",20),bg="white")
                us.place(x=75,y=170)
                eus=Entry(f2,bd=5,textvariable=f_pname1,font=("Calibri",20),bg="white",width=20,fg="black")
                eus.place(x=75,y=230)
                gob=Button(f2,image=go,bd=0,bg="#FFFFFF",command=go_to_2)
                gob.place(x=165,y=350)
                break
            else:
                flag1 = 2
    if flag1 == 2:
        messagebox.showerror("Error","Invalid Username Or Aadhar Number")
    cur.close()
    con.close()
#change password section if data validation is correct in above function
def go_to_2():
    global flag2
    flag2 = 0
    if f_pname.get()=="" or f_pname1.get()=="":
        messagebox.showerror("error","All Fields Are Required!")
    if f_pname.get()==f_pname1.get():
        flag2 = 1
        con=pymysql.connect(host="localhost",user="root",password='',database="employee_management")
        cur=con.cursor()
        sql1 = "UPDATE employee SET Password = %s WHERE Username=%s"
        cur.execute(sql1,(f_pname.get(),f_uname.get()))
        messagebox.showinfo("Success!","Password Changed Successfully")
        cp.destroy()
    else:
        flag2 = 2
    if flag2 == 2:
        messagebox.showerror("Error","New Password and Confirm Password does not match")
    con.commit()
    cur.close()
    con.close()
#employee login page (fetching data and validating)
def emplogin():
    global flag
    flag = 0
    con=pymysql.connect(host="localhost",user="root",password='',database="employee_management")
    sql = "select * from employee"
    cur=con.cursor()
    cur.execute(sql)
    dt = cur.fetchall()
    if uname.get()=="" or Password.get()=="":
        messagebox.showerror("error","All Fields Are Required!")
    else:
        for i in dt:
            if uname.get()==i[5] and Password.get()==i[6]:
                flag = 1
                messagebox.showinfo("Success","Welcome "+ uname.get())     
                billingsystem()
                break
            else:
                flag = 2
    if flag == 2:
        messagebox.showerror("Error","Invalid Username Or Password")
    cur.close()
    con.close()
#same as employee
def adminlogin():
    global flag
    flag = 0
    con=pymysql.connect(host="localhost",user="root",password='',database="admin_login")
    sql1 = "select * from login"
    cur=con.cursor()
    cur.execute(sql1)
    dt = cur.fetchall()
    if aname.get()=="" or apassword.get()=="":
        messagebox.showerror("error","All Fields Are Required!")
    else:
        for j in dt:
            if aname.get()==j[5] and apassword.get()==j[6]:
                flag = 1
                messagebox.showinfo("Success","Welcome "+ aname.get())
                admin_fun()
                break
            else:
                flag = 2
    if flag==2:
        messagebox.showerror("Error","Invalid Username Or Password")
    cur.close()
    con.close()
#billing system function in employee functions
def billingsystem():
    #part of ui you can toggle around
    f=Frame(bg="white")
    f.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f,image=f1background)
    bgimg.place(x=0,y=0) 
    f1=Frame(bg="white")
    f1.place(x=50,y=50,width=1430,height=720)
    title=Label(f1,text="Billing System",bg="white",fg="black",font=("calibri",40,"bold"),pady=2).pack()
    l1= Label(f1,bd=15,text=uname.get(),font=("Calibri",15,"bold"),bg="white")
    l1.place(x=25,y=0)
    logout_button=Button(f1,image=f1logout,bd=0,bg="#FFFFFF",command=employee_del)
    logout_button.place(x=20,y=40)
    l2= Label(f1,bd=15,text="",font=("Calibri",15,"bold"),bg="white")
    l2.place(x=1150,y=0)
    l3= Label(f1,bd=15,text="",font=("Calibri",15,"bold"),bg="white")
    l3.place(x=1150,y=40)
    l4= Label(f1,bd=15,text="",font=("Calibri",15,"bold"),bg="white")
    l4.place(x=1270,y=40)
    #this function fetches current time and places it in the home screen
    def clock():
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        day = time.strftime("%A")
        day1 = time.strftime("%d/%m/%Y")
        l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
        l2.after(1000,clock)
        l3.config(text = day1 +",")
        l4.config(text = day)
        return day1
    clock()
    #-----------------Customer Frame-------------------- 
    f2 = LabelFrame(f1,text="Customer Details",bg="white",fg="black",font=("times new roman",15),pady=2)
    f2.place(x=10,y=90,width=1400,height=80)


    cname_lbl = Label(f2,text="Customer Name",bg="white",fg="black",font=("times new roman",15)).grid(row=0,column=3,pady=10)
    cname_text = Entry(f2,textvariable=custname,bg="white",bd=7,relief=SUNKEN,fg="black",width=20,font=("times new roman",15)).grid(row=0,column=4,padx=10,pady=5)

    cphn_lbl = Label(f2,text="Contact Number",bg="white",fg="black",font=("times new roman",15)).grid(row=0,column=5,pady=10)
    cphn_text = Entry(f2,textvariable=custphone,bg="white",bd=7,relief=SUNKEN,fg="black",width=20,font=("times new roman",15)).grid(row=0,column=6,padx=10,pady=5)

    #----------------Product Details--------------------
    f3 = LabelFrame(f1,text="Products",bg="white",fg="black",font=("times new roman",15),pady=2)
    f3.place(x=10,y=170,width=500,height=420) 
    clicked=StringVar()
    clicked1=StringVar()
    clicked2=StringVar()
    Product = Label(f3,text="Select Product",bg="white",fg="black",font=("times new roman",15)).grid(row=4,column=0,pady=10,sticky=W)
    Products = ttk.Combobox(f3,width=50,state="readonly",textvariable=clicked2)
    Products.grid(row=5,column=0,padx=2,sticky=W)
    #============categories=================
    sel_category = Label(f3,text="Select Category",bg="white",fg="black",font=("times new roman",15)).grid(row=0,column=0,pady=10,sticky=W)
    categories = ttk.Combobox(f3,width=50,state="readonly",textvariable=clicked)
    categories.grid(row=1,column=0,padx=2,sticky=W)
    db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
    cursor = db.cursor()
    sql1 = "SELECT Category from inventory"
    cursor.execute(sql1)
    datas = cursor.fetchall()
    l = list(datas)
    res=[]
    for i in l: 
        if i not in res: 
            res.append(i) 
    categories['values'] = res
    db.commit()
    cursor.close()
    db.close()
#============subcategories=================  
    def getsubcategories(event):
        subcategories.set("")
        Products.set("")
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        sql = "SELECT Subcategory from inventory WHERE Category=%s"
        cursor.execute(sql,clicked.get())
        datas = cursor.fetchall()
        l = list(datas)
        res=[]
        for i in l: 
            if i not in res: 
                res.append(i)
        subcategories['values'] = res 
        db.commit()
        cursor.close()
        db.close()
    sub_category = Label(f3,text="Select Sub Category",bg="white",fg="black",font=("times new roman",15)).grid(row=2,column=0,pady=10,sticky=W)
    subcategories = ttk.Combobox(f3,width=50,state="readonly",textvariable=clicked1)
    subcategories.grid(row=3,column=0,padx=2,sticky=W) 
    stock = Label(f3,text="In Stock:",bg="white",fg="black",font=("times new roman",15))
    stock.grid(row=8,column=0,pady=10,sticky=W)
    global qwerty
    qwerty = {} 
    global pfin
    pfin = {}
#============products=================
    def getproducts(event):
        Products.set("")
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        sql1 = "SELECT Name from inventory WHERE Subcategory=%s"
        cursor.execute(sql1,clicked1.get())
        datas = cursor.fetchall()
        l = list(datas)
        Products['values'] = l
        db.commit()
        cursor.close()
        db.close()
    def product_list():
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        sql1 = "SELECT Name from inventory"
        cursor.execute(sql1)
        datas = cursor.fetchall()
        a = list(datas)
        for i in a:
            l = ("".join(map(str,i)))
            pfin[l] = 0
            qwerty[l] = 0
    product_list()
    def getstock(event):
        global l
        l = 0
        if (clicked2.get())!="":
            db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
            cursor = db.cursor()
            sql = "SELECT InStock from inventory WHERE Name=%s"
            cursor.execute(sql,clicked2.get())
            datas = cursor.fetchone()
            a = list(datas)
            l = int("".join(map(str,a))) 
            stock.config(text="In Stock:"+str(l)) 
    
    categories.bind('<<ComboboxSelected>>',getsubcategories)
    subcategories.bind('<<ComboboxSelected>>',getproducts)
    Products.bind('<<ComboboxSelected>>',getstock)
    
    quantity = Label(f3,text="Quantity",bg="white",fg="black",font=("times new roman",15)).grid(row=6,column=0,pady=10,sticky=W)
    quantitye= Entry(f3,textvariable=q,bg="white",bd=2,fg="black",width=32,font=("times new roman",15)).grid(row=7,column=0,padx=2)  
    global total_cost
    total_cost = 0.0  
    def add_to_cart():
        c = 0
        global total_cost
        global l 
        if clicked.get() == "" or clicked1.get() == "" or clicked2.get() == "":
            messagebox.showerror("Error!","Select Products First") 
        elif custname.get()=="" or custphone.get()=="":
            messagebox.showerror("Error!","Enter Customer Details First")
        elif custname.get().isdigit()==True and custphone.get().isdigit()==False:
            messagebox.showerror("Error!","Both Customer Name and Customer Contact Number is Invalid")
        elif custname.get().isdigit() == True:
            messagebox.showerror("Error!","Customer Name is Invalid")
        elif custphone.get().isdigit() == False:
            messagebox.showerror("Error!","Customer Contact Number is Invalid")
        elif len(custphone.get())!=10:
            messagebox.showerror("Error!","Enter a Valid Contact Number")
        else:
            if clicked2.get() in qwerty:
                x = qwerty[(clicked2.get())]
                st = q.get() + x
                qwerty[clicked2.get()] = st 
                a = getprice(st)
            if clicked2.get() in pfin:
                x = pfin[(clicked2.get())]
                st =  float(a) 
                pfin[clicked2.get()] = st 
            if int(l) == 0:
                messagebox.showerror("Sorry","Product Out Of Stock")
            else:
                if q.get() == 0:
                    messagebox.showerror("Error","Select atleast 1 quantity")
                elif q.get()>int(l):
                    messagebox.showerror("Error","Invalid Quantity")
                elif q.get() < 0:
                    messagebox.showerror("Error","Invalid Quantity")

                else:
                    while(c==0):
                        l = int(l)-q.get()
                        c=c+1
                        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
                        cursor = db.cursor()
                        sql = "UPDATE inventory SET InStock = %s WHERE Name=%s"
                        cursor.execute(sql,(int(l),clicked2.get()))
                        db.commit()
                        db.close() 
                    stock.config(text="In Stock:"+str(l))
                    bill_section()       
    global count
    count = 0
    #this is the bill section you can change it according to your requirements
    def bill_section():
        day = clock()
        txtarea.delete('1.0',END)
        txtarea.insert(INSERT,'''                                          THE FANTOM STORE
                                SHOP NO. A-10, IN HOUSE NO.100/95-96,
                                      STREET 95, AMSTERDAM,
                                          UNITED KINGDOM 
                                        TEL NO: 1234567890                                                    ''')
        txtarea.insert(INSERT,"--------------------------------------------------------------------------------------------------\n")
        txtarea.insert(END,"\nCustomer Name: "+custname.get()+"\t\t\t\t\t\t\t\t\t\t")                               
        txtarea.insert(INSERT,"Phone Number: "+ custphone.get())
        txtarea.insert(END,"\n")
        txtarea.insert(END,"\nBill Number: "+custbillno.get()+"\t\t\t\t\t\t\t\t\t\t") 
        txtarea.insert(INSERT,"Date: "+day+"\n")
        txtarea.insert(INSERT,"---------------------------------------------------------------------------------------------------------\n")
        txtarea.insert(END,"Product Name\t\t\t\t\t\tQuantity(Qty.)\t\t\t\t\tPrice\n")   
        txtarea.insert(INSERT,"---------------------------------------------------------------------------------------------------------\n")        
        for i in qwerty:
            if qwerty[i] != 0:
                txtarea.insert(END,i+"\t\t\t\t\t\t"+str(qwerty[i])+"\t\t\t\t\t"+"£ "+str(pfin[i]))
                txtarea.insert(INSERT,"\n" ) 
    #if a product is added and customer wants to remove it
    def remove_previous():
        global l
        if clicked.get() == "" or clicked1.get() == "" or clicked2.get() == "":
            messagebox.showerror("Error!","Add Products First to Remove")
        elif clicked2.get() in qwerty:
            if qwerty[clicked2.get()] != 0:
                x = qwerty[(clicked2.get())]
                if x<q.get():
                    messagebox.showerror("Error!","Not Enough Quantity To Remove")
                else:
                    st = x - q.get()
                    qwerty[clicked2.get()] = st
                    a = getprice(st)
                    pfin[clicked2.get()] = a
                    l = int(l) + q.get()
                    db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
                    cursor = db.cursor()
                    sql = "UPDATE inventory SET InStock = %s WHERE Name=%s"
                    cursor.execute(sql,(int(l),clicked2.get()))
                    db.commit()
                    db.close() 
                    stock.config(text="In Stock:"+str(l))
                    bill_section()
            else:
                messagebox.showerror("Error!","{0} not included in the bill".format(clicked2.get()))
    #function to calculate total cost
    def total_cost_func():
        global total_cost
        total_cost = 0.0
        c = 0
        for i in pfin:
            if pfin[i] != 0:
                c = c+1       
            total_cost = total_cost + float(pfin[i])
        if c==0:
            messagebox.showerror("error","Add Products First")
        else:
            txtarea.insert(INSERT,"\n---------------------------------------------------------------------------------------------------------\n")
            txtarea.insert(INSERT,"\nTotal:                                                                                  "+"Rs. "+str(total_cost)+"\n")    
    #function to clear all/deselect all choices made by user
    def clear_all():
        categories.set("")
        subcategories.set("")
        Products.set("")
        q.set(0)
        custname.set("")
        custphone.set("")
        stock.config(text="In Stock:")
    b1 = Button(f3,image=atc,bd=0,command=add_to_cart,bg="#FFFFFF").place(x=0,y=340)
    b2 = Button(f3,image=remove,command=remove_previous,bd=0,bg="#FFFFFF").place(x=190,y=340)
    b3 = Button(f3,image=clear,bd=0,bg="#FFFFFF",command=clear_all).place(x=350,y=340)

     #-----------------Bill Window Frame-------------------- 
    f5 = LabelFrame(f1,text="Bill Window",bg="white",fg="black",font=("times new roman",15),pady=2)
    f5.place(x=540,y=170,width=870,height=533)
    scroll_y = Scrollbar(f5,orient=VERTICAL)
    txtarea = Text(f5,width=870,height=265,yscrollcommand=scroll_y.set)
    def getprice(st):
        if (clicked2.get())!="":
            db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
            cursor = db.cursor()
            sql = "SELECT MRP from inventory WHERE Name=%s"
            cursor.execute(sql,clicked2.get())
            datas = cursor.fetchone()
            a = list(datas)
            l = ''.join(a)
            b = float(l)
            p = st*b
            pp = str(p)
            return pp
    def reset_qwerty_pfin():
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        sql1 = "SELECT Name from inventory"
        cursor.execute(sql1)
        datas = cursor.fetchall()
        a = list(datas)
        for i in a:
            l = ("".join(map(str,i)))
            pfin[l] = 0
            qwerty[l] = 0
    def billarea():
        txtarea.insert(INSERT,'''                                          THE FANTOM STORE
                                SHOP NO. A-10, IN HOUSE NO.100/95-96,
                                      STREET 95, AMSTERDAM,
                                          UNITED KINGDOM 
                                        TEL NO: 1234567890                                                    ''')
        txtarea.insert(INSERT,"--------------------------------------------------------------------------------------------------\n")
        txtarea.insert(END,"\nCustomer Name: "+"\t\t\t\t\t\t\t\t\t\t")                               
        txtarea.insert(INSERT,"Phone Number: ")
        txtarea.insert(END,"\n")
        txtarea.insert(END,"\nBill Number: "+"\t\t\t\t\t\t\t\t\t\t") 
        txtarea.insert(INSERT,"Date: "+"\n")
        txtarea.insert(INSERT,"---------------------------------------------------------------------------------------------------------\n")
        txtarea.insert(END,"Product Name\t\t\t\t\t\tQuantity(Qty.)\t\t\t\t\tPrice\n")   
        txtarea.insert(INSERT,"---------------------------------------------------------------------------------------------------------")
    #save the bill in local directory
    def save_bill():
        bill_data = txtarea.get('1.0',END)
        os.chdir("../RMS")
        bl = open("bills/"+str(custbillno.get())+".txt","w")
        bl.write(bill_data)
        bl.close()
    #generate bill function
    def generate_bill():
        if custname.get()=="":
            messagebox.showerror("Error","Please Enter a Name!")
        elif custphone.get()=="":
            messagebox.showerror("Error","Please Enter a Phone Number!")
        elif total_cost == 0.0:
            messagebox.showerror("Error","Bill Empty or Total Not Calculated ")
        else:
            save_bill()
            c=0
            db = pymysql.connect(host="localhost",user="root",password='',database="bills")
            cursor = db.cursor()
            sql = "SELECT Sno from cust_bills"
            cursor.execute(sql)
            datas = cursor.fetchall()
            for i in datas:
                c=c+1
            sql1 = "INSERT into cust_bills values(%s,%s,%s,%s)"
            cursor.execute(sql1,(c+1,custbillno.get(),custname.get(),custphone.get()))
            db.commit()
            db.close()            
            messagebox.showinfo("Success","Bill Generated Successfully!!")
            txtarea.delete('1.0',END)
            custname.set("")
            custphone.set("")
            clear_all()
            reset_qwerty_pfin()
            x=random.randint(10000,99999)
            custbillno.set(str(x))
            billarea()
    #search a bill using bill number saved in local directory(all bills are stored with bill number as names)
    def search_bill():
        if custbillsearch.get()=="":
            messagebox.showerror("Error!","Enter a Bill Number")
        else:
            present = "no"
            os.chdir("../RMS/bills")
            for i in os.listdir("bills/"):
                if i.split('.')[0] == custbillsearch.get():
                    messagebox.showinfo("Success!","Bill Found")
                    il = open(f"bills/{i}","r")
                    txtarea.delete('1.0',END)
                    for d in il:
                        txtarea.insert(END,d)
                    il.close()
                    present = "yes"
            if present == "no":
                messagebox.showerror("Error","Invalid Bill No.")
    #clear the bill 
    def clear_bill():
        txtarea.delete('1.0',END)
        messagebox.showinfo("Success!","Bill Cleared")
        custbillsearch.set("")
        reset_qwerty_pfin()
        x=random.randint(10000,99999)
        custbillno.set(str(x))
        billarea()
    cbill_lbl = Label(f2,text="Bill Number",bg="white",fg="black",font=("times new roman",15)).grid(row=0,column=0,pady=10)
    cbill_text = Entry(f2,bg="white",bd=7,textvariable=custbillsearch,relief=SUNKEN,fg="black",width=20,font=("times new roman",15)).grid(row=0,column=1,padx=10,pady=5)
    bill_btn = Button(f2,image=f2search,bd=0,bg="#FFFFFF",command=search_bill).grid(row=0,column=2,padx=10,pady=5)   
    
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)
    f4 = LabelFrame(f1,text="Bill Options",bg="white",fg="black",font=("times new roman",15),pady=2)
    f4.place(x=10,y=600,width=500,height=100) 
    b4 = Button(f4,image=total,bd=0,bg="#FFFFFF",command=total_cost_func).place(x=0,y=10)
    b5 = Button(f4,image=generate,command=generate_bill,bd=0,bg="#FFFFFF").place(x=110,y=10)
    b6 = Button(f4,image=clear,bd=0,bg="#FFFFFF",command=clear_bill).place(x=260,y=10)
    b7 = Button(f4,image=Exit,bd=0,bg="#FFFFFF",command=home).place(x=360,y=10)
    billarea()
#all the admin functions section
def admin_fun():
    #part of ui you can toggle around
    f=Frame(bg="white")
    f.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f,image=f1background)
    bgimg.place(x=0,y=0) 
    f1=Frame(bg="white")
    f1.place(x=50,y=50,width=1430,height=720)
    Label(f1,text="ADMIN MODE",bg="white",fg="black",font=("calibri",40,"bold"),pady=2).pack()
    l1= Label(f1,bd=15,text=aname.get(),font=("Calibri",15,"bold"),bg="white")
    l1.place(x=25,y=0)
    logout_button=Button(f1,image=logout,bd=0,bg="#FFFFFF",command=admin_del)
    logout_button.place(x=20,y=40)

    b1= tk.Button(f1,bd=0,image=inventory_button,bg="#FEFEFE",activebackground="#FEFEFE",command=inventory_management)
    b1.place(x=450,y=300)

    b2= tk.Button(f1,bd=0,image=employees_button,bg="#FEFEFE",activebackground="#FEFEFE",command=employee_management)
    b2.place(x=650,y=300)

    b3= tk.Button(f1,bd=0,image=invoices_button,bg="#FEFEFE",activebackground="#FEFEFE",command=invoices_management)
    b3.place(x=850,y=300)
#function of admin to manage inventory
def inventory_management():
    #part of ui you can toggle around
    global pnamee,pcategorye,psubcategorye,pquantitye,ppricee
    f=Frame(bg="white")
    f.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f,image=f1background)
    bgimg.place(x=0,y=0) 
    f1=Frame(bg="white")
    f1.place(x=50,y=50,width=1430,height=720)
    Label(f1,text="Inventory Management",bg="white",fg="black",font=("calibri",40,"bold"),pady=2).pack()
    l1= Label(f1,bd=15,text=aname.get(),font=("Calibri",15,"bold"),bg="white")
    l1.place(x=25,y=0)
    logout_button=Button(f1,image=logout,bd=0,bg="#FFFFFF",command=admin_del)
    logout_button.place(x=20,y=40)

    l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
    l2.place(x=1150,y=0)
    def clock():    
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
        l2.after(1000,clock)
    clock()
    f2 = LabelFrame(f1,text="Menu",bg="white",fg="black",font=("times new roman",15),pady=2)
    f2.place(x=10,y=90,width=350,height=605)
    Label(f2,bd=10,text="Product ID",font=("Times New Roman",14,),bg="white").place(x=0,y=15)
    Pid = Entry(f2,textvariable=ID,bg="white",bd=2,fg="black",width=20,font=("times new roman",15))
    Pid.place(x=10,y=60) 
    #add product section in admin functions(ui part)
    def add_product():
        global pnamee,pcategorye,psubcategorye,pquantitye,ppricee
        f=Frame(bg="white")
        f.place(x=0,y=0,width=1530,height=800)
        bgimg= Label(f,image=f1background)
        bgimg.place(x=0,y=0) 
        f1=Frame(bg="white")
        f1.place(x=50,y=50,width=1430,height=720)
        Label(f1,text="Add Product",bg="white",fg="black",font=("calibri",40,"bold"),pady=50).pack()    
        l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
        l2.place(x=1150,y=0)
        def clock():    
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")
            l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
            l2.after(1000,clock)
        clock()
        Label(f1,text="Product Name",font=("Times New Roman",20),bg="white").place(x=100,y=200)
        pnamee=Entry(f1,textvariable=pname,bg="white",bd=2,fg="black",width=83,font=("times new roman",20)).place(x=100,y=250) 
        Label(f1,text="Category",font=("Times New Roman",20),bg="white").place(x=100,y=300)
        pcategorye=Entry(f1,textvariable=pcategory,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=100,y=350) 
        Label(f1,text="Sub-Category",font=("Times New Roman",20),bg="white").place(x=700,y=300)
        psubcategorye=Entry(f1,textvariable=psubcategory,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=700,y=350) 
        Label(f1,text="Quantity",font=("Times New Roman",20),bg="white").place(x=100,y=400)
        pquantitye=Entry(f1,textvariable=pquantity,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=100,y=450) 
        Label(f1,text="Price",font=("Times New Roman",20),bg="white").place(x=700,y=400)
        ppricee=Entry(f1,textvariable=pprice,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=700,y=450) 
        add_button=Button(f1,image=add,bd=0,bg="#FFFFFF",command=add_product_in_database)
        add_button.place(x=570,y=550)
        clear_button=Button(f1,image=cleara,bd=0,bg="#FFFFFF",command=clear)
        clear_button.place(x=700,y=550)
        exit_button1=Button(f1,image=Exita,bd=0,bg="#FFFFFF",command=Exit_to_inventory)
        exit_button1.place(x=635,y=600)
    #update a product of inventory in database
    def update_product_in_inventory():
        x = table.selection()
        productdata=[]
        for i in x:
            productdata.append(table.item(i)['values'])
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        if pname.get()=="" or pcategory.get()=="" or psubcategory.get()=="" or pquantity.get()=="" or pprice.get()=="":
            messagebox.showerror("Error!","Enter Complete Details")
        elif pquantity.get().isdigit()!=True:
            messagebox.showerror("Error!","Invalid Quantity")
        elif pprice.get().replace('.', '', 1).isdigit()!=True:
            messagebox.showerror("Error!","Invalid Price")
        else:
            sql = "UPDATE inventory SET Name = %s WHERE ProductID=%s"
            cursor.execute(sql,(pname.get(),productdata[0][0]))
            sql1 = "UPDATE inventory SET Category = %s WHERE ProductID=%s"
            cursor.execute(sql1,(pcategory.get(),productdata[0][0]))
            sql2 = "UPDATE inventory SET Subcategory = %s WHERE ProductID=%s"
            cursor.execute(sql2,(psubcategory.get(),productdata[0][0]))
            sql3 = "UPDATE inventory SET InStock = %s WHERE ProductID=%s"
            cursor.execute(sql3,(pquantity.get(),productdata[0][0]))
            sql4 = "UPDATE inventory SET MRP = %s WHERE ProductID=%s"
            cursor.execute(sql4,(pprice.get(),productdata[0][0]))
            messagebox.showinfo("Success!","Product Updated!")
            db.commit()
            db.close()    
    #update product section(ui part)
    def update_product():
        x = table.selection()
        productdata=[]
        if x==():
            messagebox.showerror("error!","Select a Product first!")
        else:
            for i in x:
                productdata.append(table.item(i)['values'])
            global pnamee,pcategorye,psubcategorye,pquantitye,ppricee
            f=Frame(bg="white")
            f.place(x=0,y=0,width=1530,height=800)
            bgimg= Label(f,image=f1background)
            bgimg.place(x=0,y=0) 
            f1=Frame(bg="white")
            f1.place(x=50,y=50,width=1430,height=720)
            Label(f1,text="Update Product",bg="white",fg="black",font=("calibri",40,"bold"),pady=50).pack()    
            l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
            l2.place(x=1150,y=0)
            def clock():    
                hour = time.strftime("%I")
                minute = time.strftime("%M")
                second = time.strftime("%S")
                am_pm = time.strftime("%p")
                l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
                l2.after(1000,clock)
            clock()
            Label(f1,text="Product Name",font=("Times New Roman",20),bg="white").place(x=100,y=200)
            pnamee=Entry(f1,textvariable=pname,bg="white",bd=2,fg="black",width=83,font=("times new roman",20))
            pnamee.place(x=100,y=250) 
            pnamee.insert(0,productdata[0][1])
            Label(f1,text="Category",font=("Times New Roman",20),bg="white").place(x=100,y=300)
            pcategorye=Entry(f1,textvariable=pcategory,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            pcategorye.place(x=100,y=350) 
            pcategorye.insert(0,productdata[0][2])
            Label(f1,text="Sub-Category",font=("Times New Roman",20),bg="white").place(x=700,y=300)
            psubcategorye=Entry(f1,textvariable=psubcategory,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            psubcategorye.place(x=700,y=350) 
            psubcategorye.insert(0,productdata[0][3])
            Label(f1,text="Quantity",font=("Times New Roman",20),bg="white").place(x=100,y=400)
            pquantitye=Entry(f1,textvariable=pquantity,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            pquantitye.place(x=100,y=450) 
            pquantitye.insert(0,productdata[0][4])
            Label(f1,text="Price",font=("Times New Roman",20),bg="white").place(x=700,y=400)
            ppricee=Entry(f1,textvariable=pprice,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            ppricee.place(x=700,y=450) 
            ppricee.insert(0,productdata[0][5])
            update1_button=Button(f1,image=update1,bd=0,bg="#FFFFFF",command=update_product_in_inventory)
            update1_button.place(x=555,y=550)
            clear_button=Button(f1,image=cleara,bd=0,bg="#FFFFFF",command=clear)
            clear_button.place(x=700,y=550)
            exit_button1=Button(f1,image=Exita,bd=0,bg="#FFFFFF",command=Exit_to_inventory)
            exit_button1.place(x=632,y=600)
    #remove product of inventory from database
    def remove_product_from_inventory():
        x = table.selection()
        productdata=[]
        if x==():
            messagebox.showerror("error!","Select a Product first!")
        else:
            answer = messagebox.askyesno("DELETE PRODUCT","Are You Sure?")
            if answer==True:
                for i in x:
                    productdata.append(table.item(i)['values'])
                for record in x:
                    table.delete(record)
                for i in productdata:
                    db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
                    cursor = db.cursor()
                    sql = "DELETE from inventory WHERE ProductID=%s"
                    cursor.execute(sql,i[0])
                    db.commit()
                    db.close()
                messagebox.showinfo("success!","Item deleted successfully!")   
            else:
                pass     
    def Exit_to_inventory():
        ide = Entry(f2,textvariable=ID,bg="white",bd=2,fg="black",width=20,font=("times new roman",15))
        ide.delete(0,END)
        clear()
        inventory_management()
    #function to add a particular product in database
    def add_product_in_database():
        c=0
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        sql = "SELECT ProductID from inventory"
        cursor.execute(sql)
        datas = cursor.fetchall()
        for i in datas:
            c=c+1
        if pname.get()=="" or pcategory.get()=="" or psubcategory.get()=="" or pquantity.get()=="" or pprice.get()=="":
            messagebox.showerror("Error!","Enter Complete Details")
        elif pquantity.get().isdigit()!=True:
            messagebox.showerror("Error!","Invalid Quantity")
        elif pprice.get().replace('.', '', 1).isdigit()!=True:
            messagebox.showerror("Error!","Invalid Price")
        else:
            sql1 = "INSERT into inventory values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql1,(c+1,pname.get(),pcategory.get(),psubcategory.get(),pquantity.get(),pprice.get()))
            messagebox.showinfo("success!","Product added successfully")
            db.commit()
            db.close()
    
    def clear():
        pnamee=Entry(f1,textvariable=pname,bg="white",bd=2,fg="black",width=83,font=("times new roman",20))
        pcategorye=Entry(f1,textvariable=pcategory,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)) 
        psubcategorye=Entry(f1,textvariable=psubcategory,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)) 
        pquantitye=Entry(f1,textvariable=pquantity,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
        ppricee=Entry(f1,textvariable=pprice,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)) 
        pnamee.delete(0,END)
        pcategorye.delete(0,END)
        psubcategorye.delete(0,END)  
        pquantitye.delete(0,END)
        ppricee.delete(0,END)
    #show all inventory products
    def showall():
        db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
        cursor = db.cursor()
        sql = "SELECT * from inventory"
        cursor.execute(sql)
        datas = cursor.fetchall()
        table.delete(*table.get_children())
        for i in datas:
            table.insert('',END,values=i)
        db.commit()
        db.close()
    #search a particular product from inventory using its product id
    def search_product():
        flag=0
        c=0
        if ID.get()==0 or ID.get()<0 :
            messagebox.showerror("error!","Invalid Product ID")
        elif ID.get()=="":
            messagebox.showerror("error!","Enter Product ID")
        else:
            db = pymysql.connect(host="localhost",user="root",password='',database="inventory management")
            cursor = db.cursor()
            sql = "SELECT ProductID from inventory"
            cursor.execute(sql)
            dd = cursor.fetchall()
            for i in dd:
                c=c+1
                if ID.get()!=i[0]:
                    flag =flag+1  
            if flag==c:
                messagebox.showerror("Error!","Product Not Found")
                flag=0
            else:
                pass 
            sql1 = "SELECT ProductID from inventory where ProductID=%s"
            cursor.execute(sql1,ID.get())
            d = cursor.fetchone()
            sql2 = "SELECT * from inventory where ProductID=%s"
            cursor.execute(sql2,d[0])
            datas = cursor.fetchall()
            if ID.get() == d[0]:
                messagebox.showinfo("Success!","Product Found")
                table.delete(*table.get_children())
                for i in datas:
                    table.insert('',END,values=i)
                db.commit()
                db.close()    
    #exit to admin home page        
    def exit_to_admin_fun():
        Pid.delete(0,END)
        Pid.insert(0,0)
        admin_fun()
    search_button=Button(f2,image=search,bd=0,bg="#FFFFFF",command=search_product)
    search_button.place(x=220,y=58)
    Label(f2,bd=10,text="Product Options",font=("Times New Roman",14,),bg="white").place(x=0,y=110)
    showall_button=Button(f2,image=showallproducts,bd=0,bg="#FFFFFF",command=showall)
    showall_button.place(x=40,y=150)

    addproduct_button=Button(f2,image=addproduct,bd=0,bg="#FFFFFF",command=add_product)
    addproduct_button.place(x=40,y=200)

    updateproduct_button=Button(f2,image=updateproduct,bd=0,bg="#FFFFFF",command=update_product)
    updateproduct_button.place(x=40,y=250)

    deleteproduct_button=Button(f2,image=deleteproduct,bd=0,bg="#FFFFFF",command=remove_product_from_inventory)
    deleteproduct_button.place(x=40,y=300)

    exit_button=Button(f2,image=Exita,bd=0,bg="#FFFFFF",command=exit_to_admin_fun)
    exit_button.place(x=115,y=500)

    f3 = Frame(f1,bg="white",pady=2)
    f3.place(x=380,y=100,width=1000,height=605)
    scroll_x = Scrollbar(f3,orient=HORIZONTAL)
    scroll_y = Scrollbar(f3,orient=VERTICAL)
    table = ttk.Treeview(f3,columns=("ProductID","Name","Category","Sub-Category","In Stock","Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=table.xview)
    scroll_y.config(command=table.yview)
    table.heading("ProductID",anchor=W,text="ProductID")
    table.heading("Name",anchor=W,text="Name")
    table.heading("Category",anchor=W,text="Category")
    table.heading("Sub-Category",anchor=W,text="Sub-Category")
    table.heading("In Stock",anchor=W,text="In Stock")
    table.heading("Price",anchor=W,text="Price")
    table['show']='headings'
    table.column("ProductID",width=50)
    table.column("Name",width=100)
    table.column("Category",width=100)
    table.column("Sub-Category",width=100)
    table.column("In Stock",width=100)
    table.column("Price",width=100)
    table.pack(fill=BOTH,expand=1)
    showall()
#employee management function under admin functions
#same add, update,remove functions as done in inventory management, nothing new here
def employee_management():
    f=Frame(bg="white")
    f.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f,image=f1background)
    bgimg.place(x=0,y=0) 
    f1=Frame(bg="white")
    f1.place(x=50,y=50,width=1430,height=720)
    Label(f1,text="Employee Management",bg="white",fg="black",font=("calibri",40,"bold"),pady=2).pack()
    l1= Label(f1,bd=15,text=aname.get(),font=("Calibri",15,"bold"),bg="white")
    l1.place(x=25,y=0)
    logout_button=Button(f1,image=logout,bd=0,bg="#FFFFFF",command=admin_del)
    logout_button.place(x=20,y=40)

    l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
    l2.place(x=1150,y=0)
    def clock():    
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
        l2.after(1000,clock)
    clock()
    f2 = LabelFrame(f1,text="Menu",bg="white",fg="black",font=("times new roman",15),pady=2)
    f2.place(x=10,y=90,width=350,height=605)
    Label(f2,bd=10,text="Employee ID",font=("Times New Roman",14,),bg="white").place(x=0,y=15)
    Eid = Entry(f2,textvariable=EID,bg="white",bd=2,fg="black",width=20,font=("times new roman",15))
    Eid.place(x=10,y=60) 
    def add_employee():
        f=Frame(bg="white")
        f.place(x=0,y=0,width=1530,height=800)
        bgimg= Label(f,image=f1background)
        bgimg.place(x=0,y=0) 
        f1=Frame(bg="white")
        f1.place(x=50,y=50,width=1430,height=720)
        Label(f1,text="Add Employee",bg="white",fg="black",font=("calibri",40,"bold"),pady=50).pack()    
        l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
        l2.place(x=1150,y=0)
        def clock():    
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")
            l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
            l2.after(1000,clock)
        clock()
        Label(f1,text="Employee Name",font=("Times New Roman",20),bg="white").place(x=100,y=200)
        empnamee=Entry(f1,textvariable=empname,bg="white",bd=2,fg="black",width=83,font=("times new roman",20)).place(x=100,y=250) 
        
        Label(f1,text="Contact No.",font=("Times New Roman",20),bg="white").place(x=100,y=300)
        empcontacte=Entry(f1,textvariable=empcontact,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=100,y=350) 
        
        Label(f1,text="Address",font=("Times New Roman",20),bg="white").place(x=700,y=300)
        empaddresse=Entry(f1,textvariable=empaddress,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=700,y=350) 
        
        Label(f1,text="Aadhar No.",font=("Times New Roman",20),bg="white").place(x=100,y=400)
        empaadhare=Entry(f1,textvariable=empaadhar,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=100,y=450) 
        
        Label(f1,text="Username",font=("Times New Roman",20),bg="white").place(x=700,y=400)
        empusernamee=Entry(f1,textvariable=empusername,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=700,y=450)
        
        Label(f1,text="Password",font=("Times New Roman",20),bg="white").place(x=100,y=500)
        emppassworde=Entry(f1,textvariable=emppassword,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)).place(x=100,y=550)  
        
        add_button=Button(f1,image=add,bd=0,bg="#FFFFFF",command=add_employee_in_database)
        add_button.place(x=570,y=550)
        clear_button=Button(f1,image=cleara,bd=0,bg="#FFFFFF",command=clear)
        clear_button.place(x=700,y=550)
        exit_button1=Button(f1,image=Exita,bd=0,bg="#FFFFFF",command=Exit_to_inventory)
        exit_button1.place(x=635,y=600)
    def update_employee_in_database():
        x = table.selection()
        employeedata=[]
        for i in x:
            employeedata.append(table.item(i)['values'])
        db = pymysql.connect(host="localhost",user="root",password='',database="employee_management")
        cursor = db.cursor()
        if empname.get()=="" or empcontact.get()=="" or empaddress.get()=="" or empusername.get()=="" or emppassword.get()=="":
            messagebox.showerror("Error!","Enter Complete Details")
        elif empname.get().isdigit()==True:
            messagebox.showerror("Error!","Invalid Name")
        elif len(empcontact.get())!= 10:
            messagebox.showerror("Error!","Invalid Contact Number")
        elif empcontact.get().isdigit()!=True:
            messagebox.showerror("Error!","Invalid Contact Number")
        elif empaadhar.get().isdigit()!=True:
            messagebox.showerror("Error!","Invalid Aadhar Number")
        elif len(empaadhar.get())!=12:
            messagebox.showerror("Error!","Invalid Aadhar Number")
        else:
            sql = "UPDATE employee SET Name = %s WHERE Name=%s"
            cursor.execute(sql,(empname.get(),employeedata[0][1]))
            sql1 = "UPDATE employee SET Contact = %s WHERE Contact=%s"
            cursor.execute(sql1,(empcontact.get(),employeedata[0][2]))
            sql2 = "UPDATE employee SET Address = %s WHERE Address=%s"
            cursor.execute(sql2,(empaddress.get(),employeedata[0][3]))
            sql3 = "UPDATE employee SET AadharNo = %s WHERE AadharNo=%s"
            cursor.execute(sql3,(empaadhar.get(),employeedata[0][4]))
            sql4 = "UPDATE employee SET Username = %s WHERE Username=%s"
            cursor.execute(sql4,(empusername.get(),employeedata[0][5]))
            sql5 = "UPDATE employee SET Password = %s WHERE Password=%s"
            cursor.execute(sql5,(emppassword.get(),employeedata[0][6]))
            messagebox.showinfo("Success!","Employee Details Updated!")
            db.commit()
            db.close()    
    def update_employee():
        x = table.selection()
        employeedata=[]
        if x==():
            messagebox.showerror("error!","Select a Employee first!")
        else:
            for i in x:
                employeedata.append(table.item(i)['values'])
            f=Frame(bg="white")
            f.place(x=0,y=0,width=1530,height=800)
            bgimg= Label(f,image=f1background)
            bgimg.place(x=0,y=0) 
            f1=Frame(bg="white")
            f1.place(x=50,y=50,width=1430,height=720)
            Label(f1,text="Update Employee",bg="white",fg="black",font=("calibri",40,"bold"),pady=50).pack()    
            l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
            l2.place(x=1150,y=0)
            def clock():    
                hour = time.strftime("%I")
                minute = time.strftime("%M")
                second = time.strftime("%S")
                am_pm = time.strftime("%p")
                l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
                l2.after(1000,clock)
            clock()
            
            Label(f1,text="Employee Name",font=("Times New Roman",20),bg="white").place(x=100,y=200)
            empnamee=Entry(f1,textvariable=empname,bg="white",bd=2,fg="black",width=83,font=("times new roman",20))
            empnamee.place(x=100,y=250) 
            empnamee.insert(0,employeedata[0][1])
            
            Label(f1,text="Contact No.",font=("Times New Roman",20),bg="white").place(x=100,y=300)
            empcontacte=Entry(f1,textvariable=empcontact,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            empcontacte.place(x=100,y=350) 
            empcontacte.insert(0,employeedata[0][2])
            
            Label(f1,text="Address",font=("Times New Roman",20),bg="white").place(x=700,y=300)
            empaddresse=Entry(f1,textvariable=empaddress,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            empaddresse.place(x=700,y=350) 
            empaddresse.insert(0,employeedata[0][3])
            
            Label(f1,text="Aadhar No.",font=("Times New Roman",20),bg="white").place(x=100,y=400)
            empaadhare=Entry(f1,textvariable=empaadhar,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            empaadhare.place(x=100,y=450) 
            empaadhare.insert(0,employeedata[0][4])
            
            Label(f1,text="Username",font=("Times New Roman",20),bg="white").place(x=700,y=400)
            empusernamee=Entry(f1,textvariable=empusername,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            empusernamee.place(x=700,y=450) 
            empusernamee.insert(0,employeedata[0][5])
            
            Label(f1,text="Password",font=("Times New Roman",20),bg="white").place(x=100,y=500)
            emppassworde=Entry(f1,textvariable=emppassword,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
            emppassworde.place(x=100,y=550) 
            emppassworde.insert(0,employeedata[0][6])
            
            update1_button=Button(f1,image=update1,bd=0,bg="#FFFFFF",command=update_employee_in_database)
            update1_button.place(x=555,y=550)
            clear_button=Button(f1,image=cleara,bd=0,bg="#FFFFFF",command=clear)
            clear_button.place(x=700,y=550)
            exit_button1=Button(f1,image=Exita,bd=0,bg="#FFFFFF",command=Exit_to_inventory)
            exit_button1.place(x=632,y=600)

    def remove_employee():
        x = table.selection()
        employeedata=[]
        if x==():
            messagebox.showerror("error!","Select a Employee first!")
        else:
            answer = messagebox.askyesno("FIRE EMPLOYEE","Are You Sure?")
            if answer==True:
                for i in x:
                    employeedata.append(table.item(i)['values'])
                for record in x:
                    table.delete(record)
                for i in employeedata:
                    db = pymysql.connect(host="localhost",user="root",password='',database="employee_management")
                    cursor = db.cursor()
                    sql = "DELETE from employee WHERE EmployeeID=%s"
                    cursor.execute(sql,i[0])
                    db.commit()
                    db.close()
                messagebox.showinfo("success!","Employee removed successfully!") 
            else:
                pass       
    def Exit_to_inventory():
        ide = Entry(f2,textvariable=EID,bg="white",bd=2,fg="black",width=20,font=("times new roman",15))
        ide.delete(0,END)
        clear()
        employee_management()
    def add_employee_in_database():
        c=0
        d=0
        flag = 0
        db = pymysql.connect(host="localhost",user="root",password='',database="employee_management")
        cursor = db.cursor()
        sql = "SELECT Username from employee"
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            if empusername.get()== i[d]:
                messagebox.showerror("error!","Username already taken!")
                flag = 1
            else:
                d=d+1
            d = 0
        if flag == 0:
            sql1 = "SELECT EmployeeID from employee"
            cursor.execute(sql1)
            datas = cursor.fetchall()
            for i in datas:
                c=c+1
            if empname.get()=="" or empcontact.get()=="" or empaddress.get()=="" or empusername.get()=="" or emppassword.get()=="":
                messagebox.showerror("Error!","Enter Complete Details")
            elif empname.get().isdigit()==True:
                messagebox.showerror("Error!","Invalid Name")
            elif len(empcontact.get())!= 10:
                messagebox.showerror("Error!","Invalid Contact Number")
            elif empcontact.get().isdigit()!=True:
                messagebox.showerror("Error!","Invalid Contact Number")
            elif empaadhar.get().isdigit()!=True:
                messagebox.showerror("Error!","Invalid Aadhar Number")
            elif len(empaadhar.get())!=12:
                messagebox.showerror("Error!","Invalid Aadhar Number")
            else:
                sql2 = "INSERT into employee values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql2,(c+1,empname.get(),empcontact.get(),empaddress.get(),empaadhar.get(),empusername.get(),emppassword.get()))
                messagebox.showinfo("success!","Employee added successfully")
                db.commit()
                db.close()
        else:
            pass
    def clear():
        empnamee=Entry(f1,textvariable=empname,bg="white",bd=2,fg="black",width=83,font=("times new roman",20))
        empcontacte=Entry(f1,textvariable=empcontact,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)) 
        empaddresse=Entry(f1,textvariable=empaddress,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)) 
        empaadhare=Entry(f1,textvariable=empaadhar,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
        empusernamee=Entry(f1,textvariable=empusername,bg="white",bd=2,fg="black",width=40,font=("times new roman",20))
        emppassworde=Entry(f1,textvariable=emppassword,bg="white",bd=2,fg="black",width=40,font=("times new roman",20)) 
 
        empnamee.delete(0,END)
        empcontacte.delete(0,END)
        empaddresse.delete(0,END)  
        empaadhare.delete(0,END)
        empusernamee.delete(0,END)
        emppassworde.delete(0,END)
    def showall():
        db = pymysql.connect(host="localhost",user="root",password='',database="employee_management")
        cursor = db.cursor()
        sql = "SELECT * from employee"
        cursor.execute(sql)
        datas = cursor.fetchall()
        table.delete(*table.get_children())
        for i in datas:
            table.insert('',END,values=i)
        db.commit()
        db.close()
    def exit_to_admin_fun():
        Eid.delete(0,END)
        Eid.insert(0,0)
        admin_fun()
    def search_employee():
        flag=0
        c=0
        if EID.get()==0 or EID.get()<0 :
            messagebox.showerror("error!","Invalid Employee ID")
        elif EID.get()=="":
            messagebox.showerror("error!","Enter Employee ID")
        else:
            db = pymysql.connect(host="localhost",user="root",password='',database="employee_management")
            cursor = db.cursor()
            sql = "SELECT EmployeeID from employee"
            cursor.execute(sql)
            dd = cursor.fetchall()
            for i in dd:
                c=c+1
                if EID.get()!=i[0]:
                    flag =flag+1  
            if flag==c:
                messagebox.showerror("Error!","Employee Not Found")
                flag=0
            else:
                pass 
            sql1 = "SELECT EmployeeID from employee where EmployeeID=%s"
            cursor.execute(sql1,EID.get())
            d = cursor.fetchone()
            sql2 = "SELECT * from employee where EmployeeID=%s"
            cursor.execute(sql2,d[0])
            datas = cursor.fetchall()
            if EID.get() == d[0]:
                messagebox.showinfo("Success!","Employee Found")
                table.delete(*table.get_children())
                for i in datas:
                    table.insert('',END,values=i)
                db.commit()
                db.close()            
    
    search_button=Button(f2,image=search,bd=0,bg="#FFFFFF",command=search_employee)
    search_button.place(x=220,y=58)
    Label(f2,bd=10,text="Employee Options",font=("Times New Roman",14,),bg="white").place(x=0,y=110)
    showall_button=Button(f2,image=showallemployees,bd=0,bg="#FFFFFF",command=showall)
    showall_button.place(x=40,y=150)

    addemployee_button=Button(f2,image=addemployee,bd=0,bg="#FFFFFF",command=add_employee)
    addemployee_button.place(x=40,y=210)

    updateemployee_button=Button(f2,image=updateemployee,bd=0,bg="#FFFFFF",command=update_employee)
    updateemployee_button.place(x=40,y=270)

    deleteemployee_button=Button(f2,image=removeemployee,bd=0,bg="#FFFFFF",command=remove_employee)
    deleteemployee_button.place(x=40,y=330)

    exit_button=Button(f2,image=Exita,bd=0,bg="#FFFFFF",command=exit_to_admin_fun)
    exit_button.place(x=115,y=500)

    f3 = Frame(f1,bg="white",pady=2)
    f3.place(x=380,y=100,width=1000,height=605)
    scroll_x = Scrollbar(f3,orient=HORIZONTAL)
    scroll_y = Scrollbar(f3,orient=VERTICAL)
    table = ttk.Treeview(f3,columns=("EmployeeID","Name","Contact No.","Address","Aadhar No.","Username","Password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=table.xview)
    scroll_y.config(command=table.yview)
    table.heading("EmployeeID",anchor=W,text="EmployeeID")
    table.heading("Name",anchor=W,text="Name")
    table.heading("Contact No.",anchor=W,text="Contact No.")
    table.heading("Address",anchor=W,text="Address")
    table.heading("Aadhar No.",anchor=W,text="Aadhar No.")
    table.heading("Username",anchor=W,text="Username")
    table.heading("Password",anchor=W,text="Password")
    table['show']='headings'
    table.column("EmployeeID",width=50)
    table.column("Name",width=100)
    table.column("Contact No.",width=100)
    table.column("Address",width=100)
    table.column("Aadhar No.",width=100)
    table.column("Username",width=100)
    table.column("Password",width=100)
    table.pack(fill=BOTH,expand=1)
    showall()
#invoices management function under admin functions
def invoices_management():
    f=Frame(bg="white")
    f.place(x=0,y=0,width=1530,height=800)
    bgimg= Label(f,image=f1background)
    bgimg.place(x=0,y=0) 
    f1=Frame(bg="white")
    f1.place(x=50,y=50,width=1430,height=720)
    Label(f1,text="Invoices Management",bg="white",fg="black",font=("calibri",40,"bold"),pady=2).pack()
    l1= Label(f1,bd=15,text=aname.get(),font=("Calibri",15,"bold"),bg="white")
    l1.place(x=25,y=0)
    logout_button=Button(f1,image=logout,bd=0,bg="#FFFFFF",command=admin_del)
    logout_button.place(x=20,y=40)

    l2= Label(f1,bd=15,text="",font=("Calibri",26,"bold"),bg="white")
    l2.place(x=1150,y=0)
    def clock():    
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        l2.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
        l2.after(1000,clock)
    clock()
    f2 = LabelFrame(f1,text="Menu",bg="white",fg="black",font=("times new roman",15),pady=2)
    f2.place(x=10,y=90,width=350,height=605)
    Label(f2,bd=10,text="Bill Number",font=("Times New Roman",14,),bg="white").place(x=0,y=15)
    Bid = Entry(f2,textvariable=BID,bg="white",bd=2,fg="black",width=20,font=("times new roman",15))
    Bid.place(x=10,y=60) 
    #function to delete a bill(bill is stored first in local directory then its name is stored in database so when deleting we have to delete it from both places)
    def delete_bill():
        x = table.selection()
        billdata=[]
        if x==():
            messagebox.showerror("error!","Select a Bill first!")
        else:
            for i in x:
                billdata.append(table.item(i)['values'])
            for record in x:
                table.delete(record)
            for i in billdata:
                db = pymysql.connect(host="localhost",user="root",password='',database="bills")
                cursor = db.cursor()
                sql = "DELETE from cust_bills WHERE BillNumber=%s"
                cursor.execute(sql,i[1])
                db.commit()
                db.close()
                a = str(i[1])+".txt"
                os.remove(f"../RMS/bills/{a}")
            messagebox.showinfo("success!","Bill deleted successfully!")        
    def Exit_to_admin():
        ide = Entry(f2,textvariable=BID,bg="white",bd=2,fg="black",width=20,font=("times new roman",15))
        ide.delete(0,END)
        BID.set("")
        admin_fun()
    #show all bills
    def showall():
        db = pymysql.connect(host="localhost",user="root",password='',database="bills")
        cursor = db.cursor()
        sql = "SELECT * from cust_bills"
        cursor.execute(sql)
        datas = cursor.fetchall()
        table.delete(*table.get_children())
        for i in datas:
            table.insert('',END,values=i)
        db.commit()
        db.close()
    #search a bill using bill id
    def search_bill_func():
        flag=0
        c=0
        if BID.get()=="":
            messagebox.showerror("error!","Enter Bill Number")
        else:
            db = pymysql.connect(host="localhost",user="root",password='',database="bills")
            cursor = db.cursor()
            sql = "SELECT BillNumber from cust_bills"
            cursor.execute(sql)
            dd = cursor.fetchall()
            for i in dd:
                c=c+1
                if BID.get()!=i[0]:
                    flag =flag+1  
            if flag==c:
                messagebox.showerror("Error!","Bill Not Found")
                flag=0
            else:
                pass 
            sql1 = "SELECT BillNumber from cust_bills where BillNumber=%s"
            cursor.execute(sql1,BID.get())
            d = cursor.fetchone()
            sql2 = "SELECT * from cust_bills where BillNumber=%s"
            cursor.execute(sql2,d[0])
            datas = cursor.fetchall()
            if BID.get() == d[0]:
                messagebox.showinfo("Success!","Bill Found")
                table.delete(*table.get_children())
                for i in datas:
                    table.insert('',END,values=i)
                db.commit()
                db.close()            
    #when you click on a particular bill,
    #the bill number is fetched from database first if the input bill number matches
    #the bill number retrieved from database then the bill is displayed from the local directory
    def view_bill_func():
        x = table.selection()
        billdata=[]
        if x==():
            messagebox.showerror("error!","Select a Bill first!")
        else:
            present="no"
            os.chdir("../RMS")
            new = Toplevel(root)
            new.geometry("870x533")
            new.title("Bill Window")
            new.resizable(False,False)
            f1 = Frame(new,bg="white",pady=2)
            f1.place(x=0,y=0,width=865,height=533)
            scroll_y = Scrollbar(f1,orient=VERTICAL)
            textarea = Text(f1,width=870,height=533,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=textarea.yview)
            textarea.pack(fill=BOTH,expand=1)
            for i in x:
                billdata.append(table.item(i)['values']) 
            for i in os.listdir("../RMS/bills"):
                if int(i.split('.')[0]) == int(billdata[0][1]):
                    il = open(f"bills/{i}","r")
                    textarea.delete('1.0',END)
                    for d in il:
                        textarea.insert(INSERT,d)
                    il.close()
                    present = "yes"
            if present == "no":
                messagebox.showerror("Error","Invalid Bill No.")
    search_button=Button(f2,image=search,bd=0,bg="#FFFFFF",command=search_bill_func)
    search_button.place(x=220,y=58)
    Label(f2,bd=10,text="Bill Options",font=("Times New Roman",14,),bg="white").place(x=0,y=110)
    
    viewbill_button=Button(f2,image=viewbill,bd=0,bg="#FFFFFF",command=view_bill_func)
    viewbill_button.place(x=40,y=150)    
    
    showall_button=Button(f2,image=showallbills,bd=0,bg="#FFFFFF",command=showall)
    showall_button.place(x=40,y=220)

    deletebill_button=Button(f2,image=deletebill,bd=0,bg="#FFFFFF",command=delete_bill)
    deletebill_button.place(x=40,y=290)

    exit_button=Button(f2,image=Exita,bd=0,bg="#FFFFFF",command=Exit_to_admin)
    exit_button.place(x=115,y=500)

    f3 = Frame(f1,bg="white",pady=2)
    f3.place(x=380,y=100,width=1000,height=605)
    scroll_x = Scrollbar(f3,orient=HORIZONTAL)
    scroll_y = Scrollbar(f3,orient=VERTICAL)
    table = ttk.Treeview(f3,columns=("S.No","Bill Number","Customer Name","Customer Contact No."),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=table.xview)
    scroll_y.config(command=table.yview)
    table.heading("S.No",anchor=W,text="S.No")
    table.heading("Bill Number",anchor=W,text="Bill Number")
    table.heading("Customer Name",anchor=W,text="Customer Name")
    table.heading("Customer Contact No.",anchor=W,text="Customer Contact No.")
    table['show']='headings'
    table.column("S.No",width=50)
    table.column("Bill Number",width=100)
    table.column("Customer Name",width=100)
    table.column("Customer Contact No.",width=100)
    table.pack(fill=BOTH,expand=1)
    showall()
home()
root.mainloop() 