import string
import random
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Password Generator")
frame = tk.Frame(window, width=300)
frame.grid()
def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    # pass_len = int(input("Enter the password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # shuffle the list s
    random.shuffle(s)
    password = "".join(s[:int(pass_len.get())+1])

    my_pass = tk.Label(window, text=password)
    my_pass.grid()





# create input field
the_label = tk.Label(window, text="Please enter the password length", fg="black")
the_label.grid(row=1)
pass_len = tk.Entry(window, width=30)
pass_len.grid(row=2)

gen_button = tk.Button(window, text="Generate", command=gen)
gen_button.grid()
window.mainloop()