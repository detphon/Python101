from tkinter import *
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกอะไร')
GUI.geometry('300x150')

def Button1():
    text = text_enter.get()
    messagebox.showinfo("Message", f"{text}")


label = Label(GUI, text="อยากพิมพ์อะไร")
label.pack(padx=10, pady=10)

text_enter = Entry(GUI)
text_enter.pack(padx=10, pady=10)

B1 = Button(GUI,text='show',command=Button1)
B1.pack(ipadx=20,ipady=5)

GUI.mainloop()


