# Importing necessary libraries
import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip

# Function to generate a password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: You must select at least one character type."

    return ''.join(random.choice(characters) for _ in range(length))

# Function to handle generate button click event
def generate_button_clicked():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    result_label.config(text=password)
    copied_label.config(text="")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        pyperclip.copy(password)
        copied_label.config(text="Password copied to clipboard", foreground="green")
    else:
        copied_label.config(text="No password generated", foreground="red")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(background="#ADD8E6")  # Light Blue background color

# Create and apply style
style = ttk.Style()

# Set style for the labels
style.configure("Medium.TCheckbutton", font=("Arial", 12))
style.configure("Large.TLabel", font=("Arial", 14))

# Set style for the button
style.configure("Medium.TButton", font=("Arial", 12), padding=6, relief="flat", background="#4CAF50", foreground="white")

# Create and pack widgets
length_label = ttk.Label(root, text="Password Length:", style="Large.TLabel")
length_label.pack()

length_entry = ttk.Entry(root, font=("Arial", 12))
length_entry.pack()

letters_var = tk.BooleanVar()
letters_checkbox = ttk.Checkbutton(root, text="Include Letters", variable=letters_var, onvalue=True, offvalue=False, style="Medium.TCheckbutton")
letters_checkbox.pack(pady=5)

numbers_var = tk.BooleanVar()
numbers_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var, onvalue=True, offvalue=False, style="Medium.TCheckbutton")
numbers_checkbox.pack(pady=5)

symbols_var = tk.BooleanVar()
symbols_checkbox = ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var, onvalue=True, offvalue=False, style="Medium.TCheckbutton")
symbols_checkbox.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked, style="Medium.TButton")
generate_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, style="Medium.TButton")
copy_button.pack(pady=5)

copied_label = ttk.Label(root, text="")
copied_label.pack()

# Run the main event loop
root.mainloop()

# Code Attribution:

# Author.   Python
# Title.    string — Common string operations¶
# Url.      https://docs.python.org/3/library/string.html
# Year.     2023

# Author.   Python
# Title.    Tkinter documentation
# Url.      https://docs.python.org/3/library/tkinter.html 
# Year.     2023

# Author.   Pyperclip
# Title.    Welcome to Pyperclip’s documentation! 
# Url.      https://pyperclip.readthedocs.io/en/latest/ 
# Year.     2024

