from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile
import webbrowser
from reportlab.pdfgen import canvas
from EmpCredit import empcredit
from reportlab.lib.colors import magenta,red
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

class BillClass:
    def __init__(self, root):
        self.root = root

        self.root.geometry("1350x700+0+0")
        self.root.title("  Inventory Management System |  Developed by KST")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0
        # ========All Variables===============



        # ====Title===
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,
                                                                                                                 y=0,
                                                                                                                 relwidth=1,
                                                                                                                 height=70)

        # ===btn_logout===
        self.wbtn = Image.open("images/share.png")
        self.wbtn = self.wbtn.resize((150, 50), Image.ANTIALIAS)
        self.wbtn = ImageTk.PhotoImage(self.wbtn)

        btn_logout = Button(self.root,text="whatsapp",image=self.wbtn, command=self.Bill_send, border=0, bg="#010c48",font=("times new roman", 15, "bold")
                            ,cursor="hand2").place(x=1150, y=10)
        #btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",
                            #cursor="hand2").place(x=1150, y=10, height=50, width=150)

        # ====Clock=====
        self.lbl_clock = Label(self.root,
                               text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",
                               font=("times new roman", 15,), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # =====Product Frame=====#


        ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame1.place(x=10, y=110, width=410, height=550)

        pTitle = Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg='#262626',
                       fg="white").pack(side=TOP, fill=X)

        # ===Product Search Frame=====
        self.var_search = StringVar()
        ProductFrame2 = Frame(ProductFrame1, bd=4, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search = Label(ProductFrame2, text="Search Product | By Name ", font=("time new roman", 15, "bold"),
                           bg="white", fg="green").place(x=2, y=5)



        lbl_search = Label(ProductFrame2, text="Product Name", font=("time new roman", 15, "bold"), bg="white").place(
            x=2, y=45)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=("time new roman", 15),
                           bg="lightyellow").place(x=145, y=47, width=150, height=22)
        btn_search = Button(ProductFrame2, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white",
                            cursor="hand2").place(x=300, y=45, width=80, height=25)
        btn_show_all = Button(ProductFrame2, text="Show All", command=self.show, font=("goudy old style", 15), bg="#083531", fg="white",
                              cursor="hand2").place(x=300, y=10, width=80, height=25)

        # ===Product detail Details===
        ProductFrame3 = Frame(self.root, bd=3, relief=RIDGE)
        ProductFrame3.place(x=15, y=250, width=398, height=380)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price","dis","sgst","cgst","igst", "qty", "status","hsn","expiry"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("pid", text="P.Id")
        self.productTable.heading("name", text="Name")
        self.productTable.heading("price", text="Price")
        self.productTable.heading("dis", text="DIS")
        self.productTable.heading("sgst", text="SGST")
        self.productTable.heading("cgst", text="CGST")
        self.productTable.heading("igst", text="IGST")
        self.productTable.heading("qty", text="QTY")
        self.productTable.heading("status", text="Status")
        self.productTable.heading("hsn", text="hsn")
        self.productTable.heading("expiry", text="expiry")
        self.productTable["show"] = "headings"
        self.productTable.column("pid", width=40)
        self.productTable.column("name", width=100)
        self.productTable.column("price", width=100)
        self.productTable.column("dis", width=40)
        self.productTable.column("sgst", width=40)
        self.productTable.column("cgst", width=40)
        self.productTable.column("igst", width=40)
        self.productTable.column("qty", width=40)
        self.productTable.column("status", width=90)
        self.productTable.column("hsn", width=40)
        self.productTable.column("expiry", width=40)
        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        lbl_note = Label(ProductFrame1, text="Note: Enter 0 Qunatity to remove product from the cart",
                         font=("goudy old style", 12), anchor='w', bg="white", fg="red").pack(side=BOTTOM, fill=X)

        # ========Customer Frame=======#
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)
        cTitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15,), bg="lightgray").pack(
            side=TOP, fill=X)

        lbl_name = Label(CustomerFrame, text="Name", font=("time new roman", 15), bg="white").place(x=5, y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("time new roman", 13),
                         bg="lightyellow").place(x=80, y=35, width=180)

        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("time new roman", 15), bg="white").place(x=270,
                                                                                                              y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("time new roman", 13),
                            bg="lightyellow").place(x=380, y=35, width=140)

        # ===Cal_Cart Frame=====
        Cal_Cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420, y=190, width=530, height=360)

        # ===Calculator Frame=====
        self.var_cal_input = StringVar()

        Cal_Frame = Frame(Cal_Cart_Frame, bd=9, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)

        self.txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=('arial', 15, 'bold'), width=21,
                                   bd=10,
                                   relief=GROOVE, state='readonly', justify=RIGHT)
        self.txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(Cal_Frame, text='7', font=('arial', 15, 'bold'), command=lambda: self.get_input(7), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=1, column=0)
        btn_8 = Button(Cal_Frame, text='8', font=('arial', 15, 'bold'), command=lambda: self.get_input(8), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9', font=('arial', 15, 'bold'), command=lambda: self.get_input(9), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=1, column=2)
        btn_sum = Button(Cal_Frame, text='+', font=('arial', 15, 'bold'), command=lambda: self.get_input('+'), bd=5,
                         width=4, pady=10, cursor="hand2").grid(
            row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4', font=('arial', 15, 'bold'), command=lambda: self.get_input(4), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=('arial', 15, 'bold'), command=lambda: self.get_input(5), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=('arial', 15, 'bold'), command=lambda: self.get_input(6), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=2, column=2)
        btn_sub = Button(Cal_Frame, text='-', font=('arial', 15, 'bold'), command=lambda: self.get_input('-'), bd=5,
                         width=4, pady=10, cursor="hand2").grid(
            row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=('arial', 15, 'bold'), command=lambda: self.get_input(1), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=('arial', 15, 'bold'), command=lambda: self.get_input(2), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=('arial', 15, 'bold'), command=lambda: self.get_input(3), bd=5,
                       width=4, pady=10, cursor="hand2").grid(
            row=3, column=2)
        btn_mul = Button(Cal_Frame, text='*', font=('arial', 15, 'bold'), command=lambda: self.get_input('*'), bd=5,
                         width=4, pady=10, cursor="hand2").grid(
            row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0', font=('arial', 15, 'bold'), command=lambda: self.get_input(0), bd=5,
                       width=4, pady=15, cursor="hand2").grid(
            row=4, column=0)
        btn_c = Button(Cal_Frame, text='c', font=('arial', 15, 'bold'), command=self.clear_cal, bd=5, width=4, pady=15,
                       cursor="hand2").grid(
            row=4, column=1)
        btn_eq = Button(Cal_Frame, text='=', font=('arial', 15, 'bold'), command=self.perform_cal, bd=5, width=4,
                        pady=15, cursor="hand2").grid(
            row=4, column=2)
        btn_div = Button(Cal_Frame, text='/', font=('arial', 15, 'bold'), command=lambda: self.get_input('/'), bd=5,
                         width=4, pady=15, cursor="hand2").grid(
            row=4, column=3)

        # ===Cart Table Details===
        cart_Frame = Frame(Cal_Cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=280, y=8, width=245, height=342)
        self.cartTitle = Label(cart_Frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15,),
                          bg="lightgray")
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_Frame, columns=("pid", "name", "price","dis","sgst","cgst","igst", "qty"),
                                      yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="P.Id")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("dis", text="DIS")
        self.CartTable.heading("sgst", text="SGST")
        self.CartTable.heading("cgst", text="CGST")
        self.CartTable.heading("igst", text="IGST")
        self.CartTable.heading("qty", text="QTY")




        self.CartTable["show"] = "headings"
        self.CartTable.column("pid", width=40)
        self.CartTable.column("name", width=90)
        self.CartTable.column("price", width=90)
        self.CartTable.column("dis", width=90)
        self.CartTable.column("sgst", width=90)
        self.CartTable.column("cgst", width=90)
        self.CartTable.column("igst", width=90)
        self.CartTable.column("qty", width=40)

        # self.CartTable.column("qty", width=40)


        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        # ===Add Cart WidgetsFrame=====

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_dis = StringVar()
        self.var_sgst=StringVar()
        self.var_cgst=StringVar()
        self.var_igst=StringVar()
        self.var_qty = StringVar()
        self.var_stock= StringVar()
        self.var_hsn=StringVar()
        self.var_expiry=StringVar()
        self.var_license=StringVar()
        self.var_payment=StringVar()
        self.var_address=StringVar()
        self.var_debit=DoubleVar()
        self.var_status=StringVar()
        self.var_duedate=StringVar()
        self.var_date=StringVar()


        Add_CartWidgetsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=420, y=550, width=530, height=110)

        lbl_p_name = Label(Add_CartWidgetsFrame, text="Product Name", font=("times new roman", 15), bg="white").place(
            x=5, y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("times new roman", 15),
                           bg="lightyellow3", state='readonly').place(x=5, y=35, width=115, height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame, text="Price/Qty", font=("times new roman", 15),
                            bg="white").place(
            x=140, y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("times new roman", 15),
                            bg="lightyellow3").place(x=140, y=35, width=90, height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text="Qty", font=("times new roman", 15),
                          bg="white").place(
            x=240, y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15),
                          bg="lightyellow3").place(x=240, y=35, width=50, height=22)

        lbl_p_dis = Label(Add_CartWidgetsFrame, text="Dis", font=("times new roman", 15),
                          bg="white").place(
            x=300, y=5)
        self.txt_p_dis = Entry(Add_CartWidgetsFrame, textvariable=self.var_dis, font=("times new roman", 15),
                          bg="lightyellow3").place(x=300, y=35, width=50, height=22)

        lbl_p_sgst = Label(Add_CartWidgetsFrame, text="SGST", font=("times new roman", 15),
                          bg="white").place(
            x=360, y=5)
        self.txt_p_sgst = Entry(Add_CartWidgetsFrame, textvariable=self.var_sgst, font=("times new roman", 15),
                          bg="lightyellow3").place(x=360, y=35, width=50, height=22)

        lbl_p_cgst = Label(Add_CartWidgetsFrame, text="CGST", font=("times new roman", 15),
                           bg="white").place(
            x=420, y=5)
        self.txt_p_cgst = Entry(Add_CartWidgetsFrame, textvariable=self.var_cgst, font=("times new roman", 15),
                           bg="lightyellow3").place(x=420, y=35, width=50, height=22)

        lbl_p_igst = Label(Add_CartWidgetsFrame, text="IGST", font=("times new roman", 15),
                           bg="white").place(
            x=480, y=5)
        self.txt_p_igst = Entry(Add_CartWidgetsFrame, textvariable=self.var_igst, font=("times new roman", 15),
                           bg="lightyellow3").place(x=480, y=35, width=50, height=22)

        self.lbl_inStock = Label(Add_CartWidgetsFrame, text="In Stock", font=("times new roman", 15),
                                 bg="white")
        self.lbl_inStock.place(x=5, y=70)

        btn_clear_cart = Button(Add_CartWidgetsFrame, text="Clear",command=self.clear_cart, font=("times new roman", 15, "bold"),
                                bg="lightgray", cursor="hand2").place(x=180, y=70, width=150, height=30)

        btn_add_cart = Button(Add_CartWidgetsFrame, text="Add | Update Cart", command=self.add_update_cart, font=("times new roman", 15, "bold"),
                              bg="orange", cursor="hand2").place(x=340, y=70, width=180, height=30)

        # =======Billing Area======
        self.billFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        self.billFrame.place(x=953,y=110,width=390,height=480)

        self.lbl_amnt=Label(self.billFrame,text='Bill Amount \n[0]',font=("gaudy old style",15,'bold'),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=200,height=70)

        self.lbl_net_pay = Label(self.billFrame, text='Net Pay \n[0]',font=("gaudy old style", 15, 'bold'),bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=200, y=5, width=200, height=70)

        self.lbl_total = Label(self.billFrame, text='Total Amount       [0]', font=("times new roman", 15), bg="white")
        self.lbl_total.place(x=0, y=90, width=220, height=40)
        # self.lbl_total = Label(billFrame, text='Total Amount \n[0]', font=("times new roman", 15), bg="white").place(x=10, y=100)
        # self.txt_total = Entry(billFrame,font=("time new roman", 13),bg="lightyellow").place(x=150, y=100, width=120)

        lbl_debit = Label(self.billFrame, text="Debit Amount", font=("times new roman", 15), bg="white").place(x=15, y=140)
        txt_debit = Entry(self.billFrame, textvariable=self.var_debit, font=("time new roman", 13),bg="lightyellow").place(x=150, y=140, width=120)

        # lbl_Debit = Label(billFrame, text="Credit Amount", font=("times new roman", 15), bg="white").place(x=10, y=180)
        # txt_Debit = Entry(billFrame, textvariable=self.var_cname, font=("time new roman", 13),bg="lightyellow").place(x=150, y=180, width=120)
        self.lbl_credit = Label(self.billFrame, text='Credit Amount        [0]', font=("times new roman", 15), bg="white")
        self.lbl_credit.place(x=0, y=180, width=220, height=40)
       
        # ibl_combo =Label(billFrame ,text="Payment",font="time 15 bold" ).place(x=20,y=240,width=120)
        # lists =["Cash Payment","Online Payment","Card Payment"]
        # listcombo =StringVar(billFrame)
        # listcombo.set("Payment")
        # menu =OptionMenu(billFrame,listcombo,*lists)
        # menu.place(x=20,y=240,width=120)
        cmb_payment = ttk.Combobox(self.billFrame, textvariable=self.var_payment,
                                   values=("Payment Mode", "Cash Payment", "Online Payment", "Card Payment"),
                                   state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_payment.place(x=20, y=240, width=150)
        cmb_payment.current(0)


        # self.ibl_combo =Label(billFrame ,text="License Type",font="time 15 bold" ).place(x=200,y=240,width=120)
        # lists =["License no 1","License no 2","License no 3"]
        # self.listcombo =StringVar(billFrame)
        # self.listcombo.set("License Type")
        # menu =OptionMenu(billFrame,listcombo,*lists)
        # menu.place(x=200,y=240,width=120)
        #cmb_license = ttk.Combobox(self.billFrame, textvariable=self.var_license, values=("License Type", "LAFD 17030233", "LAID 17030209", "LASD 17030227"),
                                  #state='readonly', justify=CENTER, font=("goudy old style", 13))
        #cmb_license.place(x=200, y=240, width=150)
        #cmb_license.current(0)

        lbl_date = Label(self.billFrame, text="Date", font=("goudy old style", 15), bg="white").place(x=20, y=280)
        txt_date = Entry(self.billFrame, textvariable=self.var_date, font=("goudy old style", 13),bg="lightyellow").place(x=100, y=280, width=100)

        lbl_address=Label(self.billFrame,text="Address",font=("goudy old style",15),bg="white").place(x=20,y=330)
        # txt_address = Text(billFrame, textvariable=self.var_address,font=("goudy old style", 15), bg="lightyellow")
        # txt_address.place(x=100, y=300, width=280, height=50)
        self.txt_address = Entry(self.billFrame, textvariable=self.var_address, font=("goudy old style", 15),
                                bg="lightyellow").place(x=100, y=320, width=280, height=50)

        lbl_status = Label(self.billFrame, text="Status", font=("goudy old style", 15), bg="white").place(x=20, y=380)
        cmb_status = ttk.Combobox(self.billFrame, textvariable=self.var_status, values=("Paid", "Unpaid"), state='readonly',
                                  justify=CENTER, font=("goudy old style", 13))
        cmb_status.place(x=100, y=380, width=90)
        cmb_status.current(0)

        lbl_duedate = Label(self.billFrame, text="Due Date", font=("goudy old style", 15), bg="white").place(x=200, y=380)
        txt_duedate = Entry(self.billFrame, textvariable=self.var_duedate, font=("goudy old style", 13),
                            bg="lightyellow").place(x=290, y=380, width=90)

        #billing Buttons
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        billMenuFrame.place(x=953, y=590, width=390, height=70)



        # self.lbl_discount = Label(billMenuFrame, text='GST AMT \n[0]', font=("gaudy old style", 15, 'bold'),
        #                       bg="#bbc34a", fg="white")
        # self.lbl_discount.place(x=124, y=5, width=120, height=70)
        btn_credit = Button(billMenuFrame, text='Credit A/C', cursor='hand2',command=self.EmpCredit,
                           font=("gaudy old style", 15, 'bold'),
                           bg="gray", fg="white")
        btn_credit.place(x=135, y=10, width=120, height=50)




        btn_clear = Button(billMenuFrame, text='Clear All', cursor='hand2', command=self.clear_all,
                           font=("gaudy old style", 15, 'bold'),
                           bg="gray", fg="white")
        btn_clear.place(x=5 , y=10, width=120, height=50)


        #btn_print = Button(billMenuFrame, text='Print',command=self.print_bill,cursor='hand2', font=("gaudy old style", 15, 'bold'),
                              #bg="lightgreen", fg="white")
        #btn_print.place(x=2, y=80, width=120, height=50)

        #btn_print = Button(billMenuFrame, text='PDF Bill',command=self.open,cursor='hand2', font=("gaudy old style", 15, 'bold'),
                              #bg="#009688", fg="white")
        #btn_print.place(x=124, y=80, width=120, height=50)

        # btn_clear = Button(billMenuFrame, text='Clear All',cursor='hand2',command=self.clear_all, font=("gaudy old style", 15, 'bold'),
        #                           bg="gray", fg="white")
        # btn_clear.place(x=124, y=80, width=120, height=50)

        btn_genrate = Button(billMenuFrame, text='GST Bill',command=self.generate_bill,cursor='hand2' ,font=("gaudy old style", 15, 'bold'),
                                 bg="#009688", fg="white")
        btn_genrate.place(x=265, y=10, width=120, height=50)

        #======FOOTER====
        footer=Label(self.root,text="IMS-Inventory Management System  |  Devloped By KST",font=("times new roman",11),bg='#4d636d',fg="White",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)

        self.show()
        # self.bill_top()
        self.update_date_time()

        # =======All Functions=======

    def get_input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select pid, name, price,dis,sgst,cgst,igst, qty, status, hsn, expiry from product where status = 'Active'")
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Select input should be required", parent=self.root)
            else:
                cur.execute("select pid, name, price,dis,sgst,cgst,igst, qty, status, hsn, expiry from product where name LIKE '%" + self.var_search.get() + "%' and status = 'Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_dis.set(row[3])
        self.var_sgst.set(row[4])
        self.var_cgst.set(row[5])
        self.var_igst.set(row[6])
        self.lbl_inStock.config(text=f"In Stock[{str(row[7])}]")
        self.var_stock.set(row[7])
        self.var_hsn.set(row[9])
        self.var_expiry.set(row[10])
        self.var_qty.set('1')


    def get_data_cart(self, ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_dis.set(row[3])
        self.var_sgst.set(row[4])
        self.var_cgst.set(row[5])
        self.var_igst.set(row[6])
        self.var_qty.set(row[7])
        self.lbl_inStock.config(text=f"In Stock[{str(row[8])}]")
        self.var_stock.set(row[8])
        self.var_hsn.set(row[9])
        self.var_expiry.set(row[10])

    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error', "Please select product from the list", parent = self.root)

        elif self.var_qty.get()=='':
            messagebox.showerror('Error', "Quantity is Required", parent = self.root)

        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error', "Invalid Quantity", parent = self.root)
        else:
            # price_cal = int(self.var_qty.get()) * float(self.var_price.get())
            # price_cal = float(price_cal)
            # print(price_cal)
            price_cal=self.var_price.get()

            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal,self.var_dis.get(),self.var_sgst.get(),self.var_cgst.get(),self.var_igst.get(), self.var_qty.get(),self.var_stock.get(),self.var_hsn.get(),self.var_expiry.get()]

            #==========Update_cart===============
            present = 'no'
            index_ = 0

            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirm', "Product already present\nDo you want to update| Remove from the Cart List", parent=self.root)
                if op == True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][7]=self.var_qty.get() #qty
            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.SGSTamt=0
        self.CGSTamt=0
        self.IGSTamt=0
        self.DISamt=0
        self.net_pay=0
        self.temp=0
        self.net_pay=0
        self.totalamt=0
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.total=0
        self.n=[]
        for row in self.cart_list:

            self.bill_amnt=0
            self.SGSTamt=0
            self.CGSTamt=0
            self.IGSTamt=0
            self.DISamt=0
            self.bill_amnt = self.bill_amnt +(float(row[2])*int(row[7]))
            self.a=self.a+self.bill_amnt
            self.SGSTamt =self.SGSTamt +((self.bill_amnt*int(row[4]))/100)
            self.b=self.b+self.SGSTamt
            self.CGSTamt=self.CGSTamt+((self.bill_amnt*int(row[5]))/100)
            self.c=self.c+self.CGSTamt
            self.IGSTamt=self.IGSTamt+((self.bill_amnt*int(row[6]))/100)
            self.d=self.d+self.IGSTamt
            self.DISamt=self.DISamt+((self.bill_amnt*int(row[3]))/100)
            self.e=self.e+self.DISamt

            self.totalamt=self.totalamt+((self.bill_amnt + self.SGSTamt + self.CGSTamt + self.IGSTamt)-(self.DISamt))
            self.total =((self.bill_amnt + self.SGSTamt + self.CGSTamt + self.IGSTamt) - (self.DISamt))
            self.n.append(self.total)
        self.net_pay=self.totalamt
        self.format_float="{:.2f}".format(self.net_pay)
        self.format_float1="{:.2f}".format(self.a)

        self.lbl_amnt.config(text=f"Bill Amount\n{str(self.format_float1)}")
        # self.lbl_discount.config(text=f"GST Amount\n{str(self.var_dis.get())}%")
        # self.txt_p_dis.config(text=f"Bill Amount\n{str(self.DISamt)}")
        self.lbl_net_pay.config(text=f"Net Pay\n{str(self.format_float)}")
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")
        self.lbl_total.config(text=f" Total Amt            {str(self.format_float)}")




    def credit(self):
        self.totalcredit = 0
        self.totalcredit = (float(self.format_float) - self.var_debit.get())
        self.format_float2="{:.2f}".format(self.totalcredit)
        self.lbl_credit.config(text=f" Credit Amount      {str(self.format_float2)}")

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def generate_bill1(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        if self.var_cname.get() == '' or self.var_contact.get() == '':
            messagebox.showerror("Error", f"Customer Details are required", parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", f"Please Add product to the Cart!!!", parent=self.root)
        else:
            # ==================bill top===============
            # self.bill_top()
            # ==================bill middle===============
            # self.bill_middle()
            # ==================bill Bottom===============
            # self.bill_bottom()
            self.credit()
            self.display()
            self.open()

            #fp = open(f'bill/{str(self.invoice)}.pdf', 'w')
            #fp.write(self.txt_bill_area.get('1.0', END))
            #fp.close()
            #messagebox.showinfo('Saved', "Bill has been generated/Save in Backend", parent=self.root)
            self.chk_print = 1

    def generate_bill(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error", f"Customer Details are required", parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error", f"Please Add product to the Cart!!!", parent=self.root)
        else:
# ==================bill top===============
#             self.bill_top()
# ==================bill middle===============
#             self.bill_middle()
# ==================bill Bottom===============
#             self.bill_bottom()
            self.credit()
            self.display()
            self.open()


            #fp=open(f'bill/{str(self.invoice)}.pdf','w')
            #fp.write(self.txt_bill_area.get('1.0',END))

            #fp.close()
            #messagebox.showinfo('Saved',"Bill has been generated/Save in Backend",parent=self.root)
            self.chk_print=1

            cur.execute("insert into generatebill(InvoiceNo,CustomerName,Date,Qty,Amt,dis,sgst,cgst,igst,licenseno,paymenttype,Netamount,debitamount,creditamount,address,phno,status,duedate) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                self.invoice,
                self.var_cname.get(),
                self.var_date.get(),
                self.var_qty.get(),
                self.bill_amnt,
                self.DISamt,
                self.SGSTamt,
                self.CGSTamt,
                self.IGSTamt,
                self.var_license.get(),
                self.var_payment.get(),
                self.net_pay,
                self.var_debit.get(),
                self.totalcredit,
                self.var_address.get(),
                self.var_contact.get(),
                self.var_status.get(),
                self.var_duedate.get()




            ))
            con.commit()

        con.close()



    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 98725***** , pune-413253
{str("="*48)}
 Customer Name: {self.var_cname.get()}
 Ph No. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\tDate: {str(time.strftime("%d/%m/%y"))}
{str("="*47)}
 Product  DIS  SGST  CGST  IGST  QTY  Price
{str("="*48)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)


    def bill_bottom(self):
        bill_bottom_temp =f'''
{str("="*48)}
 Bill Amount\t\t\t\t      Rs.{(self.a)}
 DIS Amount\t\t\t\t      Rs.{self.e}
 SGST Amount\t\t\t\t      Rs.{self.b}
 CGST Amount\t\t\t\t      Rs.{self.c}
 IGST Amount\t\t\t\t      Rs.{self.d}
 Net Pay\t\t\t\t      Rs.{self.net_pay}
{str("="*48)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)




    def bill_middle(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[8])-int(row[7])
                if int(row[3])==int(row[7]):
                    status='Inactive'
                if int(row[3])!=int(row[7]):
                    status='Active'

                price=float(row[2])*int(row[7])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t  "+self.var_dis.get()+"%\t"+self.var_sgst.get()+"%    "+self.var_cgst.get()+"%\t   "+self.var_igst.get()+"%\t  "+row[7]+"   Rs."+price)
                # =======update qty in product table=======
                cur.execute('Update product set qty=?,status=? where pid=?', (
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)


    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_dis.set('')
        self.var_sgst.set('')
        self.var_cgst.set('')
        self.var_igst.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        # self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.var_contact.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.var_address.set('')
        self.var_status.set('Paid')
        self.var_duedate.set('')
        self.var_date.set('')
        self.var_license.set('License Type')
        self.var_payment.set('Payment Mode')
        self.var_debit.set('0.0')
        self.lbl_credit = Label(self.billFrame, text='Credit Amount        [0]', font=("times new roman", 15),bg="white")
        self.lbl_credit.place(x=0, y=180, width=220, height=40)
        self.lbl_total = Label(self.billFrame, text='Total Amt             [0]', font=("times new roman", 15),bg="white")
        self.lbl_total.place(x=0, y=90, width=220, height=40)
        self.lbl_amnt = Label(self.billFrame, text='Bill Amount \n[0]', font=("gaudy old style", 15, 'bold'),bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=2, y=5, width=200, height=70)

        self.lbl_net_pay = Label(self.billFrame, text='Net Pay \n[0]', font=("gaudy old style", 15, 'bold'),bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=200, y=5, width=200, height=70)

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        self.date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {str(self.date_)}\t\t Time:{str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)


    #def print_bill(self):
        #if self.chk_print==1:
            #messagebox.showinfo('print',"Please wait while printing",parent=self.root)
            #new_file=tempfile.mktemp('.pdf')
            #open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            #os.startfile(new_file,'print')
        #else:
            #messagebox.showerror('print', "Please generate bill, to print the receipt", parent=self.root)

    def display(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))
        c = canvas.Canvas(f"{self.invoice}.pdf")
        c.setLineWidth(.1)
        # self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))

        c.line(200, 200, 200, 200)
        c.rect(0, 740, 593, 100)
        c.rect(0, 640, 270, 100)
        c.rect(0, 640, 440, 100)

        # c.rect(270,810,150,30)

        c.setFont("Times-Roman",20)
        c.setFillColor(red)
        c.drawString(220, 810,'AMBIKA TYRES & OIL TRADERS')
        c.setFont("Times-Roman", 13.5)
        c.setFillColor('#000000')
        c.drawString(306, 790, 'Oil Grease & Tyre Tube')
        c.drawString(230, 770, 'Sonai - Ghodegaon Road,Opp. Mate Hospital, Sonai,')
        # c.drawString(230, 763, 'e-mail : gnadhiseeds@gmail.com')
        c.drawString(230, 750, 'Tal. Newasa, Dist. Ahmednagar. Mob. 9921759336')



        c.rect(0, 170, 593, 800)
        c.rect(0, 170, 2, 800)

        c.rect(0, 170, 33, 470)
        c.rect(0, 170, 220, 470)
        c.rect(0, 170, 140, 470)
        #c.rect(0, 170, 235, 470)
        c.rect(0, 170, 270, 470)
        c.rect(0, 170, 315, 470)
        c.rect(0, 170, 360, 470)
        c.rect(400, 170, 40, 470)
        c.rect(0, 170, 510, 470)

        c.rect(0, 600, 600, 40)
        c.rect(0, 170, 600, 20)

        c.rect(0, 100, 600, 30)
        # c.rect(0, 80, 600, 10)

        c.rect(440, 0.5, 180, 70)


        # c.drawString(272, 710, 'GSTIN:27DELPK1692N1ZS')
        c.drawString(272, 680, 'State Code : 27 Maharastra')
        # c.drawString(272, 650, 'License No :')
        # c.drawString(340, 650, str(self.var_license.get()))


        c.drawString(445, 710, 'Invoice No:')
        c.drawString(510, 710,str(self.invoice))
        c.drawString(445, 680, 'Date :')
        # c.drawString(490, 680,str(time.strftime("%d/%m/%y")) )
        c.drawString(490,680,str(self.var_date.get()))
        # c.drawString(445,650,'Date :')

        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            x=580
            y=560
            z=554
            t=1
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                qty = int(row[8]) - int(row[7])
                if int(row[3]) == int(row[7]):
                    status = 'Inactive'
                if int(row[3]) != int(row[7]):
                    status = 'Active'

                price = float(row[2]) * int(row[7])
                price = str(price)
                c.drawString(10,x,str(t))
                c.setFont("Times-Roman", 10.5)
                c.setFillColor('#000000')
                c.drawString(40, x, str(name))
                c.setFont("Times-Roman", 12)
                c.setFillColor('#000000')
                c.drawString(225, x, str(price))
                c.setFont("Times-Roman", 10)
                c.setFillColor('#000000')
                c.drawString(145,x,(row[9]))
                c.setFont("Times-Roman", 13.5)
                c.setFillColor('#000000')
                #c.drawString(240, x,(row[3]))
                #c.drawString(255, x, '%')
                # c.drawString(230, y, str(self.j))
                c.drawString(280, x,(row[4]))
                c.drawString(295, x, '%')
                # c.drawString(280, y, str(i))
                c.drawString(330, x, (row[5]))
                c.drawString(345, x, '%')
                # c.drawString(330, y, str(self.c))
                c.drawString(365, x, (row[6]))
                c.drawString(380, x, '%')
                # c.drawString(395, y, str(self.d))
                c.drawString(410, x, (row[7]))
                c.drawString(445,x,(row[10]))
                k=580
                for j in self.n:
                    self.format_float6="{:.2f}".format(j)
                    c.drawString(530, k,str(self.format_float6))
                    k=k-40
                c.rect(0, z, 600, 0)
                x=x-40
                y=y-40
                z=z-40
                t=t+1

                # =======update qty in product table=======
                cur.execute('Update product set qty=?,status=? where pid=?', (
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

        c.drawString(5, 610, 'sr no')
        # c.drawString(10, 590,self.invoice)
        c.drawString(40, 610, 'Pruduct Name')
        # c.drawString(40,580,str(self.var_pname.get()))
        c.drawString(165, 610, 'HSN')
        c.drawString(230, 610, 'Price')
        c.setFont("Times-Roman", 12)
        c.setFillColor('#000000')
        c.drawString(220,175,str(self.a))
        #c.drawString(240, 610, 'DIS')
        # c.drawString(230,580,self.var_dis.get())
        # c.drawString(245, 580, '%')
        #c.drawString(237, 175,str(self.e))
        c.setFont("Times-Roman", 13.5)
        c.setFillColor('#000000')
        c.drawString(280, 610, 'SGST')
        # c.drawString(280, 580, self.var_sgst.get())
        # c.drawString(295, 580, '%')
        self.format_float3="{:.2f}".format(self.b)
        c.drawString(277, 175, str(self.format_float3))
        c.drawString(320, 610, 'CGST')
        # c.drawString(330, 580, self.var_cgst.get())
        # c.drawString(345, 580, '%')
        self.format_float4="{:.2f}".format(self.c)
        c.drawString(317, 175, str(self.format_float4))
        c.drawString(365, 610, 'IGST')
        # c.drawString(395, 580, self.var_igst.get())
        # c.drawString(410, 580, '%')
        self.format_float5="{:.2f}".format(self.d)
        c.drawString(362, 175, str(self.format_float5))
        c.drawString(410, 610, 'Qty')
        c.drawString(450, 610, 'Expiry')
        # c.drawString(450, 580, self.var_qty.get())
        c.drawString(530, 610, 'Amount')
        c.drawString(530, 175,str(self.format_float))




        # c.drawString(100, 175, 'Total')
        c.drawString(20, 140, 'Payment Made :')
        c.drawString(120, 140, str(self.var_payment.get()))

        c.drawString(250, 140, 'Status :')
        c.drawString(300,140,str(self.var_status.get()))

        c.drawString(370, 140, 'Due Date :')
        c.drawString(430, 140, str(self.var_duedate.get()))

        c.drawString(20,110,'Debit Amount : ')
        c.drawString(120,110,str(self.var_debit.get()))

        c.drawString(220, 110, 'Credit Amount : ')
        c.drawString(320,110,str(self.format_float2))
        # c.drawString(0, 155, 'Amount Chargable(in words)')
        # c.drawString(150, 120, 'HNS/SAC')
        # c.drawString(240, 120, 'Taxable Value')
        # c.drawString(370, 120, 'Intigrated tax')
        # c.drawString(350, 100, 'Rate')
        # c.drawString(420, 100, 'Amount')

        # c.drawString(480, 120, 'Total Tax Amount')
        # c.drawString(0.5, 70, 'Tax Amount(in words)')
        # c.drawString(0.5, 40, 'Invoice No')
        c.drawString(450, 10, 'Authorisad Signatory')
        c.drawString(5, 20, 'Software Developed by Kodeo Software Technology')
        c.drawString(5, 5, 'Mobile No.9356840782')


        c.drawString(5, 710, 'Customer Name :')
        c.setFont("Times-Roman", 11)
        c.setFillColor('#000000')
        c.drawString(105,710,self.var_cname.get())
        c.setFont("Times-Roman", 13.5)
        c.setFillColor('#000000')
        c.drawString(5, 680, 'Ph No :')
        c.drawString(55,680,self.var_contact.get())
        c.drawString(5, 650, 'Address :')
        c.setFont("Times-Roman", 11)
        c.setFillColor('#000000')
        c.drawString(65, 650, str(self.var_address.get()))
        c.setFont("Times-Roman", 13.5)
        c.setFillColor('#000000')

        c.drawImage("ambika.png",20,755,width=180,height=70)
        c.save()

    def open(self):
        os.startfile(f"{self.invoice}.pdf")
        # os.startfile("invoice.pdf")
        #os.rename('invoice.pdf','bill/{str(self.invoice)}.pdf')
        #os.rename('invoice.pdf','self.invoice.txt')

    #print("PDF Generated..")



    def EmpCredit(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = empcredit(self.new_win)
    
    def Bill_send(self):
        webbrowser.open('https://web.whatsapp.com/')


if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
