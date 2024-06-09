from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Calculator ")
root.geometry("500x500")
root.resizable(FALSE,FALSE)

num1 = IntVar()
num2 = IntVar()
operation = StringVar()

label1 = Label(root,text = "A").place(x = 75,y = 50)
label2 = Label(root,text = "B").place(x = 75,y = 100)

entry1 = Entry(root,textvariable= num1).place(x = 150,y =50)
entry2 = Entry(root,textvariable= num2).place(x = 150,y =100)

combobox = ttk.Combobox(root,textvariable=operation,
                        values = ['+','-','*','/'],state = 'readonly',width = 8).place (x = 150,y=150)
def submit():
    label3 = Label(root, text=operation.get()).place(x=100, y=400)

button = Button(root,text = "Submit",command=submit).place(x = 400, y= 150)

root.mainloop()
