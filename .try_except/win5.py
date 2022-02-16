from tkinter import *

def button1Click():
    Display.config(text='Это радует!!!')
def button2Click():
    Display.config(text='Это огорчает???')

Window = Tk()
Window.config(width=260, height=120)
Display = Label(Window, text='ПрЮвет, как дела*')
Display.place(x=50, y=20, width=160, height=30)
Button1 = Button(Window, text='Хорошо', command=button1Click)
Button2 = Button(Window, text='Плохо', command=button2Click)
Button1.place(x=20, y=70, width=100, height=30)
Button2.place(x=140, y=70, width=100, height=30)
Window.mainloop()