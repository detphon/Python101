from tkinter import *
from tkinter import messagebox
from datetime import datetime
import csv

# Create the main window
GUI = Tk()
GUI.title('GUI-BISIC_CSV')
#GUI.geometry('300x150')

# Create the text entry widget
entry = Entry(GUI, width=50)
entry.pack()
#entry.pack(padx=10, pady=10)

def save_csv():
    time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    text = entry.get()
    with open('BASIC_GUI-DATA.csv', 'a') as file:
        file.write(time + "  " + text + '\n')
        entry.delete(0, END)
    #messagebox.showinfo('Success', 'Text saved successfully')

def show_csv():
    try:
        with open('BASIC_GUI-DATA.csv') as file:
            text = file.read()
            messagebox.showinfo('Text Data', text)
    except FileNotFoundError:
        messagebox.showerror('Error', 'File not found')

def clear_csv():
    text = entry.get() 
    with open('BASIC_GUI-DATA.csv', 'w') as file:
        file.write('')
        entry.delete(0, END)
    messagebox.showinfo('Success', 'data is clear')


# Create the "Save" button
save_button = Button(GUI, text='Save', command=save_csv, width=25)
save_button.pack()
#save_button.pack()

# Create the "Show" button
show_button = Button(GUI, text='Show', command=show_csv, width=25)
show_button.pack()
#show_button.pack()

# Create the "Show" button
clear_button = Button(GUI, text='clear', command=clear_csv, width=25)
clear_button.pack()
#show_button.pack()

# Run the main event loop
GUI.mainloop()
