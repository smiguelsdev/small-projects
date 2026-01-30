#!/usr/bin/python3

# This project is mainly to learn tkinter and making GUI's in Python.
import tkinter as tk
import random
import pyperclip


def generate_password(length):
    password = ""
    characters = [
        list("0123456789"),                    # numbers
        list("abcdefghijklmnopqrstuvwxyz"),    # lowercase letters
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),    # uppercase letters
        list("!@#$%&*()-_=+,.?")      # special characters
    ]
    selected_characters = []

    if sel_numbers.get() == 1:
        selected_characters += characters[0]
    if sel_lowerletters.get() == 1:
        selected_characters += characters[1]
    if sel_upperletters.get() == 1:
        selected_characters += characters[2]
    if sel_spcharacters.get() == 1:
        selected_characters += characters[3]

    for i in range(length):
        password += random.choice(selected_characters)

    return password
    

def on_generate():
    password_length = int(length_spinbox.get())

    password = generate_password(password_length)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", password)
    output_text.config(state="disabled")


def on_copy():
    pyperclip.copy(output_text.get("1.0", tk.END))


def main():
    global length_spinbox, output_text, sel_numbers, sel_lowerletters, sel_upperletters, sel_spcharacters
    root = tk.Tk(screenName=None, baseName="py_passwd_gen", className='Tk', useTk=1)
    copy_icon = tk.PhotoImage(file = "images/copy.png")
    copy_icon = copy_icon.subsample(5,5)

    root.geometry("400x400")

    tk.Label(root, text="Password Length").grid(row=1, column=0, sticky="w")

    length_spinbox = tk.Spinbox(root, from_=0, to=10)
    length_spinbox.grid(row=2, column=0, sticky="w")
    
    sel_numbers = tk.IntVar()
    sel_lowerletters = tk.IntVar()
    sel_upperletters = tk.IntVar()
    sel_spcharacters = tk.IntVar()

    tk.Checkbutton(root, text="Numbers", variable=sel_numbers).grid(row=3, column=0, sticky="w")
    tk.Checkbutton(root, text="Lowercase Letters", variable=sel_lowerletters).grid(row=4, column=0, sticky="w")
    tk.Checkbutton(root, text="Uppercase Letters", variable=sel_upperletters).grid(row=5, column=0, sticky="w")
    tk.Checkbutton(root, text="Special Characters", variable=sel_spcharacters).grid(row=6, column=0, sticky="w")

    button = tk.Button(root, text="Generate password", command=on_generate)
    button.grid(row=7, column=0, sticky="w")

    output_text = tk.Text(root, width=30, height=5)
    output_text.grid(row=8, column=0, sticky="w")
    output_text.config(state="disabled")
         
    button = tk.Button(root, image=copy_icon, command=on_copy)
    button.grid(row=9, column=0, sticky="w")

    root.mainloop()


if __name__ == '__main__':
    main()