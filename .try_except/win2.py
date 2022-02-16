from tkinter import*

Window = Tk()
Display = Label(Window, text='ПрЮвет, как дела!')
Display.pack()

Button1 = Button(Window, text='Хорошо!')
Button2 = Button(Window, text='Плохо?')
Button1.pack()
Button2.pack()

Window.mainloop()
