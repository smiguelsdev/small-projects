#!/usr/bin/python3

# This file is just me learning how to utilize the tkinter library
#   Tutorial followed: https://www.geeksforgeeks.org/python/python-gui-tkinter/
import tkinter as tk

# The Label widget is used to display text or images in a Tkinter window. It is commonly used for showing messages, titles, or instructions.
root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

testLabel = tk.Label(root, text="Oyono es mi padre").grid(row=0, column=0)
#testLabel.pack() # Only use if the object is not in a grid

# This example creates a window with a Stop button. When the button is clicked, the application closes.
testButton = tk.Button(root, text="Exit", width=25, command=root.destroy).grid(row=1, column=0)
# testButton.pack() # Only use if the object is not in a grid

# The Entry widget is used to accept single-line text input from the user. For multi-line text input, the Text widget is used instead.
tk.Label(root, text="First name:").grid(row=2, column=0)
tk.Label(root, text="Last name: ").grid(row=3, column=0)

firstEntry = tk.Entry(root)
lastEntry = tk.Entry(root)

firstEntry.grid(row=2, column=1)
lastEntry.grid(row=3, column=1)

root.mainloop()