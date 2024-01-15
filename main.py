import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title('Demo')
window.geometry('300x250')

# Create a label for the title
title_label = ttk.Label(master=window, text='Miles to kilometers', font='Calibri 24 bold')

# Create a frame for organizing input elements
input_frame = ttk.Frame(master=window)

# Create an entry widget for user input
entry = ttk.Entry(master=input_frame)

# Create a button for the conversion action
button = ttk.Button(master=input_frame, text='Convert')

# Pack the widgets to organize them within the window
title_label.pack()

# Pack the entry and button widgets into the input frame
entry.pack()
button.pack()

# Pack the input frame to organize it within the window
input_frame.pack()

# Run the Tkinter event loop
window.mainloop()
