from tkinter import *

def button1Click():
    Display.config(text='Это радует!')
def button2Click():
    Display.config(text='Это огорчает')

Window = Tk()
Display = Label(Window, text='ПрЮвет, как дела!')
Display.grid(row=0, column=1)
Button1 = Button(Window, text='Хорошо', command=button1Click)
Button2 = Button(Window, text='Плохо', command=button2Click)
Button1.grid(row=2, column=0, padx=10, pady=10,)
Button2.grid(row=2, column=2, padx=10, pady=10)

Window.mainloop()