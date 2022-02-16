from tkinter import *

# Константы текста
Answer = ['Супер', 'Хорошо', 'Так себе', 'Плохо', 'Ужасно', 'Не скажу']
Diagnose = ['Это здорово!', 'Раз ты так думаешь....' ,'Это плохо??','Это радует!!', 'Все возможно..', 'Это огорчате ?', ]

# Функция события
def buttonClick(Nr):
    Display.config(text=Diagnose[Nr])

# Основная программа 
Window = Tk()
Window.title('ПрЮвет!*?')
Window.config(width=300, height=190)
Display = Label(Window, text='Как это сделать????')
Display.place(x=80, y=10, width=160, height=30)

# Кнопки через список
Knopka = []
for Nr in range(0, 6):
    Knopka.append(Button(Window, text=Answer[Nr]))
for pos in range(0, 3):
    Knopka[pos].place(x=20, y=60+pos*40, width=120, height=30)
    Knopka[pos+3].place(x=160, y=60+pos*40, width=120, height=30)

# Индивидуальные настройки событий
Knopka[0].config(command=lambda: buttonClick(0))
Knopka[1].config(command=lambda: buttonClick(1))
Knopka[2].config(command=lambda: buttonClick(2))
Knopka[3].config(command=lambda: buttonClick(3))
Knopka[4].config(command=lambda: buttonClick(4))
Knopka[5].config(command=lambda: buttonClick(5))

# Цикл событий - Вызов
Window.mainloop()