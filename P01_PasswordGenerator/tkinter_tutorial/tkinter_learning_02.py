#!/usr/bin/python3

# This file is just me learning how to utilize the tkinter library
#   Tutorial followed: https://www.geeksforgeeks.org/python/python-gui-tkinter/
import tkinter as tk

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

# This example creates a window with a Stop button. When the button is clicked, the application closes.
testButton = tk.Button(root, text="Exit", width=25, command=root.destroy)
testButton.pack() # Only use if the object is not in a grid

root.mainloop()