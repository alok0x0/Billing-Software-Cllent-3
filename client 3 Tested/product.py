from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        # self.var_emp_id = None
        self.root = root
        # self.Product=Product
        product_Frame = root
        product_Frame.geometry("1100x500+220+130")
        product_Frame.title("Inventory Management System")
        product_Frame.config(bg="white")
        product_Frame.focus_force()
        # ==========================================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_dis=IntVar()
        self.var_hsn=IntVar()
        self.var_sgst=IntVar()
        self.var_expiry=StringVar()
        self.var_cgst=IntVar()
        self.var_igst=IntVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        product_Frame = Frame(product_Frame, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=450, height=480)

        # ====title====
        title = Label(product_Frame, text="Manage products Details", font=("goudy old style", 18), bg="#0f4d7d",
                      fg="white").pack(side=TOP, fill=X)
        # column 1
        lbl_caterory = Label(product_Frame, text="Category", font=("goudy old style", 18), bg="white").place(x=30, y=35)
        lbl_supplier = Label(product_Frame, text="Supplier", font=("goudy old style", 18), bg="white").place(x=30,
                                                                                                             y=75)
        lbl_product_name = Label(product_Frame, text="Name", font=("goudy old style", 18), bg="white").place(x=30,
                                                                                                             y=115)
        lbl_price = Label(product_Frame, text="Price", font=("goudy old style", 18), bg="white").place(x=30, y=155)
        lbl_dis = Label(product_Frame, text="DIS", font=("goudy old style", 18), bg="white").place(x=30, y=195)
        lbl_hsn = Label(product_Frame, text="HSN", font=("goudy old style", 18), bg="white").place(x=240, y=195)
        lbl_sgst = Label(product_Frame, text="SGST", font=("goudy old style", 18), bg="white").place(x=30, y=235)
        lbl_expiry = Label(product_Frame, text="Expiry", font=("goudy old style", 18), bg="white").place(x=240, y=235)
        lbl_cgst = Label(product_Frame, text="CGST", font=("goudy old style", 18), bg="white").place(x=30, y=275)
        lbl_igst = Label(product_Frame, text="IGST", font=("goudy old style", 18), bg="white").place(x=30, y=315)
        lbl_quantity = Label(product_Frame, text="Quantity", font=("goudy old style", 18), bg="white").place(x=30,
                                                                                                             y=355)
        lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 18), bg="white").place(x=30, y=395)

        # ===column2
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly',
                               justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=150, y=40, height=25,width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly',
                               justify=CENTER, font=("goudy old style", 15))
        cmb_sup.place(x=150, y=80,height=25, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 15),
                         bg="lightyellow").place(x=150, y=120,height=25, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 15),
                          bg="lightyellow").place(x=150, y=160,height=25, width=200)
        txt_dis = Entry(product_Frame, textvariable=self.var_dis, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=200,height=25, width=70)
        txt_hsn = Entry(product_Frame, textvariable=self.var_hsn, font=("goudy old style", 15), bg="lightyellow").place(
            x=320, y=200, height=25, width=110)
        txt_sgst = Entry(product_Frame, textvariable=self.var_sgst, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=240,height=25, width=70)
        txt_expiry = Entry(product_Frame, textvariable=self.var_expiry, font=("goudy old style", 15),
                         bg="lightyellow").place(
            x=320, y=240, height=25, width=110)

        txt_cgst = Entry(product_Frame, textvariable=self.var_cgst, font=("goudy old style", 15),
                         bg="lightyellow").place(
            x=150, y=280, height=25, width=70)

        txt_igst = Entry(product_Frame, textvariable=self.var_igst, font=("goudy old style", 15),
                         bg="lightyellow").place(
            x=150, y=320, height=25, width=70)

        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=360,height=25, width=70)



        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=400,height=25, width=200)
        cmb_status.current(0)
        # ===buttons===
        btn_add = Button(product_Frame, text="Save",command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white",
                         cursor="hand2").place(x=10, y=440, width=100, height=35)
        btn_update = Button(product_Frame, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white",
                            cursor="hand2").place(x=120, y=440, width=100, height=35)
        btn_delete = Button(product_Frame, text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white",
                            cursor="hand2").place(x=230, y=440, width=100, height=35)
        btn_clear = Button(product_Frame, text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white",
                           cursor="hand2").place(x=340, y=440, width=100, height=35)
        # ====searchFrame===
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12, "bold"), bd=2,
                                 relief=RIDGE, bg="white")
        SearchFrame.place(x=480, y=10, width=600, height=80)

        # ===options===
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15),
                           bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="search", command=self.search, font=("goudy old style", 15), bg="#4caf50",
                            fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        # ===Products Details===
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(p_frame,
                                         columns=("pid", "Supplier", "Category", "name", "price","DIS","SGST","CGST","IGST", "qty", "status","hsn","expiry"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("pid", text="P ID")
        self.productTable.heading("Category", text="Category")
        self.productTable.heading("Supplier", text="Supplier")
        self.productTable.heading("name", text="Name")
        self.productTable.heading("price", text="Price")
        self.productTable.heading("DIS", text="DIS")
        self.productTable.heading("SGST", text="SGST")
        self.productTable.heading("CGST", text="CGST")
        self.productTable.heading("IGST", text="IGST")
        self.productTable.heading("qty", text="Qty")
        self.productTable.heading("status", text="Status")
        self.productTable.heading("hsn", text="hsn")
        self.productTable.heading("expiry", text="expiry")

        self.productTable["show"] = "headings"

        self.productTable.column("pid", width=90)
        self.productTable.column("Category", width=100)
        self.productTable.column("Supplier", width=100)
        self.productTable.column("name", width=100)
        self.productTable.column("price", width=100)
        self.productTable.column("DIS", width=100)
        self.productTable.column("SGST", width=100)
        self.productTable.column("CGST", width=100)
        self.productTable.column("IGST", width=100)
        self.productTable.column("qty", width=100)
        self.productTable.column("status", width=100)
        self.productTable.column("hsn", width=100)
        self.productTable.column("expiry", width=100)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()
        self.fetch_cat_sup()
    # ==============================================================================================================

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are Required", parent=self.root)
            else:
                cur.execute("select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Product already present, try different", parent=self.root)
                else:
                    cur.execute("insert into product(Category, Supplier, name, price,dis,sgst,cgst,igst, qty, status,hsn,expiry) values(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_dis.get(),
                            self.var_sgst.get(),
                            self.var_cgst.get(),
                            self.var_igst.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_hsn.get(),
                            self.var_expiry.get(),
                        ))
                con.commit()
                messagebox.showinfo("Success", "Employee Addedd Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_sup.set(row[1])
        self.var_cat.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_dis.set(row[5])
        self.var_sgst.set(row[6])
        self.var_cgst.set(row[7])
        self.var_igst.set(row[8])
        self.var_qty.set(row[9])
        self.var_status.set(row[10])
        self.var_hsn.set(row[11])
        self.var_expiry.set(row[12])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product form list", parent=self.root)
            else:
                cur.execute("select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    cur.execute(
                        "Update product set Category=?,Supplier=?,name=?,price=?,dis=?,sgst=?,cgst=?,igst=?,qty=?,status=?,hsn=?,expiry=? where pid=?",
                        (
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_dis.get(),
                            self.var_sgst.get(),
                            self.var_cgst.get(),
                            self.var_igst.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_hsn.get(),
                            self.var_expiry.get(),
                            self.var_pid.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select product from the list", parent=self.root)
            else:
                cur.execute("select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid product ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from product where pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("0")
        self.var_dis.set("0")
        self.var_sgst.set("0")
        self.var_cgst.set("0")
        self.var_igst.set("0")
        self.var_qty.set("0")
        self.var_status.set("Active")
        self.var_hsn.set("0")
        self.var_expiry.set("0")
        self.var_pid.set("0")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Select input should be required", parent=self.root)
            else:
                cur.execute("select * from product where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
