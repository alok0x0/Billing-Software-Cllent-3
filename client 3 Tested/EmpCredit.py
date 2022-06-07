from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import time
# from billing import BillClass
class empcredit:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #==========================================
        # All Variables=====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cust_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_date=StringVar()
        self.var_duedate=StringVar()
        self.var_paymentamt=StringVar()
        self.var_dueamt=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_address=StringVar()
        self.var_debitamt=StringVar()
        self.var_credit=StringVar()
        self.date_ = time.strftime("%d-%m-%Y")
        print(self.date_)

        #====searchFrame===
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)


        #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","CustomerName","phno","InvoiceNo"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        # ===title===
        title = Label(self.root, text="Credit Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(
            x=50, y=100, width=1000)

        #===Content===
        #==row1==
        lbl_customerid=Label(self.root,text="Cust ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_date=Label(self.root,text="Date",font=("goudy old style",15),bg="white").place(x=380,y=150)
        lbl_duedate=Label(self.root,text="Due Date",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_customerid = Entry(self.root,textvariable=self.var_cust_id, font=("goudy old style", 15),
                          bg="lightyellow").place(x=150, y=150, width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        # cmb_gender = ttk.Combobox(self.root, values=("Select", "Male", "Female", "Other"),
        #                           state='readonly', justify=CENTER, font=("goudy old style", 15))
        # cmb_gender.place(x=500, y=150, width=180)
        # cmb_gender.current(0)
        txt_date = Entry(self.root,textvariable=self.var_date, font=("goudy old style", 15),
                            bg="lightyellow").place(x=500, y=150, width=180)
        txt_duedate = Entry(self.root,textvariable=self.var_duedate, font=("goudy old style", 15),
                            bg="lightyellow").place(x=850, y=150, width=180)

        # ==row2==
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=210)
        lbl_paymentamt = Label(self.root, text="Total Amt", font=("goudy old style", 15), bg="white").place(x=380, y=190)
        lbl_dueamt = Label(self.root, text="Credit Amt", font=("goudy old style", 15), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root,textvariable=self.var_name,  font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=210, width=180)
        txt_paymentamt = Entry(self.root,textvariable=self.var_paymentamt,font=("goudy old style", 15), bg="lightyellow",state='readonly').place(
            x=500, y=190, width=180)
        txt_dueamt = Entry(self.root,textvariable=self.var_dueamt, font=("goudy old style", 15), bg="lightyellow",state='readonly').place(
            x=850, y=190, width=180)

        # ==row3==
        # lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="white").place(x=50, y=230)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=380, y=230)
        lbl_status = Label(self.root, text="Status", font=("goudy old style", 15), bg="white").place(x=750, y=230)

        # txt_email = Entry(self.root,textvariable=self.var_email,  font=("goudy old style", 15), bg="lightyellow").place(
        #     x=150, y=230, width=180)
        txt_contact = Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(
            x=500, y=230, width=180)
        # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        cmb_status = ttk.Combobox(self.root,textvariable=self.var_status, values=("Paid", "Unpaid"), state='readonly',
                                 justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=850, y=230, width=180)
        cmb_status.current(0)

        # ==row4==
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=50, y=270)
        # lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="white").place(x=500, y=270)

        self.txt_address = Text(self.root,font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        # txt_salary = Entry(self.root,  font=("goudy old style", 15),
        #                    bg="lightyellow").place(x=600, y=270, width=180)

        lbl_debitamt = Label(self.root, text="Debit Amt", font=("goudy old style", 15), bg="white").place(x=470, y=270)
        txt_debit = Entry(self.root, textvariable=self.var_debitamt, font=("goudy old style", 15),
                           bg="lightyellow",state='readonly').place(
            x=570, y=270, width=150)

        lbl_credit = Label(self.root, text="New Debit Amt", font=("goudy old style", 15), bg="white").place(x=715, y=270)
        txt_credit = Entry(self.root, textvariable=self.var_credit, font=("goudy old style", 15),
                           bg="lightyellow").place(
            x=850, y=270, width=180)


        # # ===buttons===
        # btn_add = Button(self.root, text="Save",command=self.add, font=("goudy old style", 15), bg="#2196f3",
        #                  fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root,command=self.update, text="Update",  font=("goudy old style", 15), bg="#4caf50",
                            fg="white", cursor="hand2").place(x=680, y=315, width=110, height=28)
        btn_delete = Button(self.root,command=self.delete, text="Delete",  font=("goudy old style", 15), bg="#f44336",
                            fg="white", cursor="hand2").place(x=830, y=315, width=110, height=28)
        btn_clear = Button(self.root,command=self.clear, text="Clear",  font=("goudy old style", 15), bg="#607d8b",
                           fg="white", cursor="hand2").place(x=950, y=315, width=110, height=28)
        btn_show_all = Button(self.root, text="Show All", command=self.show, font=("goudy old style", 15),
                              bg="#083531", fg="white",
                              cursor="hand2").place(x=20, y=325, width=80, height=25)

        #===Employee Details===
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)


        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx= Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
        "invoice", "name","date", "duedate", "paymentamt", "dueamt", "contact", "status", "address","debitamt"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("invoice", text="invoice")
        self.EmployeeTable.heading("name", text="Name")
        # self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("date", text="Date")
        self.EmployeeTable.heading("duedate", text="Due Date")
        self.EmployeeTable.heading("paymentamt", text="Total Amt")
        self.EmployeeTable.heading("dueamt", text="Credit Amt")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("status", text="Status")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("debitamt", text="Debit Amt")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("invoice", width=90)
        self.EmployeeTable.column("name", width=100)
        # self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("date", width=100)
        self.EmployeeTable.column("duedate", width=100)
        self.EmployeeTable.column("paymentamt", width=100)
        self.EmployeeTable.column("dueamt", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("status", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("debitamt", width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

#==============================================================================================================
    # def add(self):
    #     con=sqlite3.connect(database=r'ims.db')
    #     cur=con.cursor()
    #     try:
    #         if self.var_cust_id.get()=="":
    #             messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)
    #         else:
    #             cur.execute("select * from creditdetails where cid=?",(self.var_cust_id.get(),))
    #             row=cur.fetchone()
    #             if row!=None:
    #                 messagebox.showerror("Error","This Employee Id already assigned,try different",parent=self.root)
    #             else:
    #                 cur.execute("insert into creditdetails(cid,name,email,date,duedate,paymentamt,dueamt,contact,status,address) values(?,?,?,?,?,?,?,?,?,?)",(
    #                                     self.var_cust_id.get(),
    #                                     self.var_name.get(),
    #                                     self.var_email.get(),
    #                                     self.var_date.get(),
    #                                     self.var_duedate.get(),
    #
    #                                     self.var_paymentamt.get(),
    #                                     self.var_dueamt.get(),
    #
    #                                     self.var_contact.get(),
    #                                     self.var_status.get(),
    #                                     self.txt_address.get('1.0',END),
    #
    #                 ))
    #                 con.commit()
    #                 messagebox.showinfo("Success","Customer credit Addedd Successfully",parent=self.root)
    #                 self.show()
    #     except Exception as ex:
    #         messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select InvoiceNo,CustomerName,Date,duedate,Netamount,creditamount,phno,status,address,debitamount from generatebill where status = 'Unpaid'")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        # print(row)
        self.var_cust_id.set(row[0]),
        self.var_name.set(row[1]),
        # self.var_email.set(row[2]),
        self.var_date.set(row[2]),
        self.var_duedate.set(row[3]),

        self.var_paymentamt.set(row[4]),
        self.var_dueamt.set(row[5]),

        self.var_contact.set(row[6]),
        self.var_status.set(row[7]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END,row[8])
        self.var_debitamt.set(row[9])

    # def getdata(self):


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cust_id.get()=="":
                messagebox.showerror("Error","customer invoice no Must Be Required",parent=self.root)
            else:
                cur.execute("select * from generatebill where InvoiceNo=?",(self.var_cust_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid customer invoice no",parent=self.root)
                else:
                    self.dueamt=(float(self.var_dueamt.get()) - int(self.var_credit.get()))
                    self.debit=(float(self.var_debitamt.get())) + int(self.var_credit.get())
                    cur.execute("update generatebill set CustomerName=?,Date=?,duedate=?,Netamount=?,creditamount=?,phno=?,status=?,address=?,debitamount=? where InvoiceNo=?",(

                                        self.var_name.get(),
                                        # self.var_email.get(),
                                        self.var_date.get(),
                                        self.var_duedate.get(),

                                        self.var_paymentamt.get(),
                                        self.dueamt,

                                        self.var_contact.get(),
                                        self.var_status.get(),
                                        self.txt_address.get('1.0',END),
                                        self.debit,

                                        self.var_cust_id.get(),
                    ))
                    con.commit()

                    messagebox.showinfo("Success","credit details  Updated Successfully",parent=self.root)
                    self.show()

                    self.var_dueamt.set(self.dueamt)
                    self.var_debitamt.set(self.debit)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cust_id.get() == "":
                messagebox.showerror("Error", "customer invoice no Must Be Required", parent=self.root)
            else:
                cur.execute("select * from generatebill where InvoiceNo=?", (self.var_cust_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Customer Invoice  ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from generatebill where InvoiceNo=?", (self.var_cust_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Customer credit Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)



    def clear(self):
        self.var_cust_id.set(""),
        self.var_name.set(""),
        # self.var_email.set(""),
        self.var_date.set(""),
        self.var_duedate.set(""),

        self.var_paymentamt.set(""),
        self.var_dueamt.set(""),

        self.var_contact.set(""),
        self.var_status.set(""),
        self.txt_address.delete('1.0', END),
        self.var_debitamt.set("")
        self.var_credit.set("")
        self.var_debitamt.set("")
        self.var_searchtxt.set(""),
        self.var_searchby.set("Select")
        self.show()


    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input should be required",parent=self.root)
            else:
                cur.execute("select InvoiceNo,CustomerName,Date,duedate,Netamount,creditamount,phno,status,address,debitamount from generatebill where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")

                rows = cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=empcredit(root)
    root.mainloop()