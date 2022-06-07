from tkPDFViewer import tkPDFViewer as pdf
from tkinter import*

class pdfClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Term and Condition")
        self.root.config(bg="white")
        self.root.focus_force()

        variable1 = pdf.ShowPdf()
        variable2 = variable1.pdf_view(root,pdf_location=r"images\term.pdf",width=100,height=100)
        variable2.pack()

if __name__=="__main__":
    root=Tk()
    obj=pdfClass(root)
    root.mainloop()