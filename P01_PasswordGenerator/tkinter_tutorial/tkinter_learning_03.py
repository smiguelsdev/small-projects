#!/usr/bin/python3

# This file is just me learning how to utilize the tkinter library
#   Tutorial followed: https://www.geeksforgeeks.org/python/python-gui-tkinter/
import tkinter as tk

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

# The Entry widget is used to accept single-line text input from the user. For multi-line text input, the Text widget is used instead.
tk.Label(root, text="First name:").grid(row=2, column=0)
tk.Label(root, text="Last name: ").grid(row=3, column=0)

firstEntry = tk.Entry(root)
lastEntry = tk.Entry(root)

firstEntry.grid(row=2, column=1)
lastEntry.grid(row=3, column=1)

print(firstEntry.get)

root.mainloop()