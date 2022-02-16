from tkinter import *
from tkinter import messagebox

def button1Click():
    messagebox.showinfo('Ответ', 'Это радует!')
def button2Click():
    messagebox.showinfo('Ответ', 'Это огорчает?')

Window = Tk()
Window.title('ПрЮвет!!!')
Window.config()
Display = Label(Window, text='ПрЮвет, как дела!')
Display.place(width=260, height=120)
Button1 = Button(Window, text='Хорошо', command=button1Click)
Button2 = Button(Window, text='Плохо', command=button2Click)
Button1.place(x=20, y=70, width=100, height=30)
Button2.place(x=140, y=70, width=100, height=30)

Window.mainloop()
