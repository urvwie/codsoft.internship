import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    options = []
    
    if include_uppercase.get():
        options.extend(string.ascii_uppercase)
    if include_lowercase.get():
        options.extend(string.ascii_lowercase)
    if include_numbers.get():
        options.extend(string.digits)
    if include_symbols.get():
        options.extend(string.punctuation)
        
    if not options:
        messagebox.showerror("Error", "Please select at least one character set")
        return
    
    password = ''.join(random.choice(options) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")

# Password length
tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var).grid(row=0, column=1, pady=5)


include_uppercase = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase", variable=include_uppercase).grid(row=1, column=0, columnspan=2)
include_lowercase = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Lowercase", variable=include_lowercase).grid(row=2, column=0, columnspan=2)
include_numbers = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=include_numbers).grid(row=3, column=0, columnspan=2)
include_symbols = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Include Symbols", variable=include_symbols).grid(row=4, column=0, columnspan=2)


tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=6, column=0, columnspan=2, pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
