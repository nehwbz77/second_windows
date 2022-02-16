from tkinter import *

# Функция для событий - Создаем
def button1Click():
    Display.config(text='Это радует!!!')
def button2Click():
    Display.config(text='Это огорчает???')

# Основная программа
Window = Tk()
Display = Label(Window, text='ПрЮвет, как дела?!?!?')
Display.pack()
Button1 = Button(Window, text='Хорошо', command=button1Click)
Button2 = Button(Window, text='Плохо', command=button2Click)
Button1.pack(side='left')
Button2.pack(side='right')

Window.mainloop()

