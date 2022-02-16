# 
# class Monster:
#     # Инициализация Атрибутов
#     def init(self, name, character):
#     # def __init__(self, name, character):
#         self.Name = name
#         self.Character = character
    
#     # Метод
#     def show(self):
#         print('Имя: ' + self.Name)
#         print('особенность: ' + self.Character)

# # Основная программа - Вызов
# # Frank = Monster('Альберт', 'задумчивый')
# Frank = Monster()
# Frank. init('Альберт', 'задумчивый')
# Frank.show()


# class Monster:
#     # Инициализация Атрибутов
#     def __init__(self, name, character):
#         self.Name = name
#         self.Character = character

#     # Метод
#     def show(self):
#         print('Имя: ' + self.Name)
#         print('Особенность: ' + self. Character)

# # Дочерние Классы
# class GMonster(Monster):
#     pass
# class AMonster(Monster):
#     pass

# # Вызов программы
# Frank = Monster('Фрэнк', 'необычный')
# Frank.show()
# Albert = GMonster('Альберт', 'задумчивый')
# Albert.show()
# Sigmund = AMonster('Зигмунд', 'веселый')
# Sigmund.show()

# import mosterlab
from mosterlab import*

# Основная программа - Вызов
# Frank = mosterlab.Monster('Фрэнк', 'необычный')
Frank = Monster('Фрэнк', 'необычный')
Frank.show()
# Albert = mosterlab.GMonster('Альберт', 'задумчивый')
Albert = GMonster('Альберт', 'задумчивый')
Albert.show()
# Sigmund = mosterlab.SMonster('Зигмунд', 'веселый')
Sigmund = SMonster('Зигмунд', 'веселый')
Sigmund.show()

