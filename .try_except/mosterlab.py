

class Monster:
    # Инициализация Атрибутов
    def __init__(self, name, chatacter):
        self.Name = name
        self.Character = chatacter

    # Метод
    def Type(self):
        return 'Монстер'
    def show(self):
        print('Имя: ' + self.Name)
        print('особенность: ' + self.Character)
        print('Тип: ' + self.Type())

# Дочерние классы
class GMonster(Monster):
    # Метод
    def Type(self):
        return ' Дух монстра '
class SMonster(Monster):
    # Метод
    def Type(self):
        return 'Душа монстра'