#!/usr/bin/python3

# This file is just me learning how to utilize the tkinter library
#   Tutorial followed: https://www.geeksforgeeks.org/python/python-gui-tkinter/
import tkinter as tk

# The Label widget is used to display text or images in a Tkinter window. It is commonly used for showing messages, titles, or instructions.
root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

testLabel = tk.Label(root, text="Oyono es mi padre")
testLabel.pack()

root.mainloop()