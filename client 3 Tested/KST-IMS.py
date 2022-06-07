from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from billing import BillClass
from product import productClass
from sales import salesClass
from msg import pdfClass
from EmpCredit import empcredit
import sqlite3
from tkinter import messagebox
import os
import time
import webbrowser
#auto-py-to-exe



class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("  Inventory Management System |  Developed by KST")
        self.root.config(bg="white")
        # ====Title===
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="KST Inventory Management System", image=self.icon_title, compound=LEFT,
        font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1,height=70)

        # ===btn_logout===
        #self.logbtn = Image.open("images/logout.png")
        #self.logbtn = self.logbtn.resize((150, 50), Image.ANTIALIAS)
        #self.logbtn = ImageTk.PhotoImage(self.logbtn)

        self.trmbtn = Image.open("images/term.png")
        self.trmbtn = self.trmbtn.resize((50, 50), Image.ANTIALIAS)
        self.trmbtn = ImageTk.PhotoImage(self.trmbtn)

        self.webbtn = Image.open("images/web.png")
        self.webbtn = self.webbtn.resize((50, 50), Image.ANTIALIAS)
        self.webbtn = ImageTk.PhotoImage(self.webbtn)
        
        #btn_logout = Button(self.root,text="Logout",image=self.logbtn, command=self.logout, border=0, bg="#010c48",font=("times new roman", 15, "bold")
                            #,cursor="hand2").place(x=1150, y=10)
        btn_term = Button(self.root, text="T&C",image=self.trmbtn,command=self.msg ,font=("times new roman", 15, "bold"),border=0,bg="#010c48"
                            ,cursor="hand2").place(x=1270, y=10, height=50, width=50)
        btn_web = Button(self.root, text="Website",image=self.webbtn,command=self.web ,font=("times new roman", 15, "bold"),border=0,bg="#010c48"
                            ,cursor="hand2").place(x=1200, y=10, height=50, width=50)
        # ====Clock=====
        self.lbl_clock = Label(self.root,text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",
                               font=("times new roman", 15,), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ===Left_Menu====
        self.MenuLogo = Image.open("images/logo3.png")
        self.MenuLogo = self.MenuLogo.resize((200, 130), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        self.wallLogo = Image.open("images/logo5.jpg")
        self.wallLogo = self.wallLogo.resize((1150, 550), Image.ANTIALIAS)
        self.wallLogo = ImageTk.PhotoImage(self.wallLogo)

        self.menutitle = Image.open("images/menu.png")
        self.menutitle = self.menutitle.resize((195, 50), Image.ANTIALIAS)
        self.menutitle= ImageTk.PhotoImage(self.menutitle)

                
        CenterMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        CenterMenu.place(x=200, y=100, width=1150, height=600)

        lbl_wallLogo = Label(CenterMenu, image=self.wallLogo)
        lbl_wallLogo.pack(side=TOP, fill=X)
        
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)
        

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file="images/side.png")

        lbl_menu = Label(LeftMenu, text="MENU", image=self.menutitle, font=("times new roman", 20)).pack(side=TOP, fill=X)
        
        btn_employee = Button(LeftMenu, text="Billing Area", command=self.billing, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier", command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category",command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Products",command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales",command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit",command=self.Exit_menu, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
        font=("times new roman", 20, "bold"), bg="DodgerBlue2", bd=3).pack(side=TOP, fill=X)

        # ===Containt Image====
        self.box = Image.open("images/button2.png")
        self.box = self.box.resize((300, 150), Image.ANTIALIAS)
        self.box = ImageTk.PhotoImage(self.box)

        self.box1 = Image.open("images/button3.png")
        self.box1 = self.box1.resize((300, 150), Image.ANTIALIAS)
        self.box1 = ImageTk.PhotoImage(self.box1)

        self.box2 = Image.open("images/button4.png")
        self.box2 = self.box2.resize((300, 150), Image.ANTIALIAS)
        self.box2 = ImageTk.PhotoImage(self.box2)

        self.box3 = Image.open("images/button5.png")
        self.box3 = self.box3.resize((300, 150), Image.ANTIALIAS)
        self.box3 = ImageTk.PhotoImage(self.box3)

        self.box4 = Image.open("images/button6.png")
        self.box4 = self.box4.resize((300, 150), Image.ANTIALIAS)
        self.box4 = ImageTk.PhotoImage(self.box4)

        self.box5 = Image.open("images/button7.png")
        self.box5 = self.box5.resize((300, 150), Image.ANTIALIAS)
        self.box5 = ImageTk.PhotoImage(self.box5)
        # ===Containt====
        self.lbl_employee=Label(self.root,text="[ 0]",compound=TOP,border=0,image=self.box,relief=RIDGE,font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=200,width=290)

        self.lbl_supplier=Label(self.root,text="[ 0]",compound=TOP,border=0,image=self.box1,relief=RIDGE,font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=200,width=290)

        self.lbl_category=Label(self.root,text="[ 0]",compound=TOP,border=0,image=self.box2,relief=RIDGE,font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=200,width=290)

        self.lbl_product=Label(self.root,text="[ 0]",compound=TOP,border=0,image=self.box3,relief=RIDGE,font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=340,height=200,width=290)

        self.lbl_sales=Label(self.root,text="[]",compound=TOP,border=0,image=self.box4,relief=RIDGE,font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=340,height=200,width=290)

        self.lbl_dueamt = Label(self.root, text="[ 0]", compound=TOP, border=0, image=self.box5, relief=RIDGE,
                                 font=("goudy old style", 20, "bold"))
        self.lbl_dueamt.place(x=1000, y=340, height=200, width=290)

        # ====Footer=====
        lbl_footer = Label(self.root,
                           text="KST Inventory Management System  |  Devloped By Kodeo Software Technology\n For any technical issue Contact : KST",
                           font=("times new roman", 12,), bg="#4d636d", fg="white").pack(side=BOTTOM,fill=X)
        

        self.update_contant()
        #=====Button Employees======#
    def msg(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=pdfClass(self.new_win)

    def web(self):
        webbrowser.open('https://kodeosoftwaretechnology.com/')
        

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)        
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def EmpCredit(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = empcredit(self.new_win)
    
    def Exit_menu(self):
        exitbtn=messagebox.askyesno("EXIT","Do you want to Exit")
        if exitbtn>0:
            self.root.destroy()

    def update_contant(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'[ {str(len(product))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'[ {str(len(supplier))}]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'[ {str(len(category))}]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'[ {str(len(employee))}]')

            cur.execute("select Sum(Netamount) from generatebill")
            generatebill = cur.fetchall()
            self.lbl_sales.config(text=f' {str(generatebill)}RS')

            cur.execute("select Sum(creditamount) from generatebill")
            generatebill = cur.fetchall()

            self.lbl_dueamt.config(text=f' {str(generatebill)}RS')

            # bill=len(os.listdir('bill'))
            # self.lbl_sales.config(text=f'[ {str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_contant)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
