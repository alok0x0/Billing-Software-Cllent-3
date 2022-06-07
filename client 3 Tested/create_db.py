import sqlite3

def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice text,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,dis text,sgst text,cgst text,igst text, qty text,status text,hsn text,expiry text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS generatebill(InvoiceNo text,CustomerName text,Date text,Qty text,Amt text, dis text,sgst text,cgst text,igst text,licenseno text,paymenttype text,Netamount text,debitamount text,creditamount text,address text,phno text,status text,duedate text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS creditdetails(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,date text,duedate text,paymentamt text,dueamt text,contact text,status text, address text)")
    con.commit()

create_db()