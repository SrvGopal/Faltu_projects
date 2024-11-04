from tkinter import *
from random import *

root = Tk()

root.geometry("500x500")
root.title("Password Generator ")

main_frame = Frame(root)
main_frame.pack(pady=20, fill='x')

label_frame = Frame(main_frame)
label_frame.pack(padx=10, pady=5)

length_l = Label(label_frame, text="Password Length:", font=('Arial', 12))
length_l.pack(side='left')

length = IntVar()
length_entry = Entry(label_frame, textvariable=length, width=5, font=('Arial', 12))
length_entry.pack(side='left', padx=5)

button_frame = Frame(main_frame)
button_frame.pack(pady=10)

submit_button = Button(button_frame, text="Generate Password",
                       command=lambda: generate_password(),
                       font=('Arial', 12))

submit_button.pack(padx=10)

password_frame = Frame(main_frame)
password_frame.pack(pady=10, padx=10)

password_label = Label(password_frame, text="Generated Password:", font=('Arial', 12))
password_label.pack(side='left')

password_output = Label(password_frame, text="", wraplength=400, font=('Arial', 12))
password_output.pack(side='left', padx=5)

def generate_password():
    
      size = length.get()
      if size < 1:
          password_output.config(text="Length must be at least 1")
          return
      word = "1234567890~!@#$%^&*()_+-`={}|[QWERTYUIOPASDFGHJKLZXCVBNM]:;,/<>?.qwertyuiopasdfghjklzxcvbnm"
      lst = list(word)
      passwd = "".join(choice(lst) for i in range(size))
      password_output.config(text=passwd)
    

root.mainloop()
