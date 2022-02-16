import random


Case = random.randint(1, 6)
Secret = 'Я задумал число от 1 до 1000'

print(Case)
print(Secret)

Input = 0
Attemp = 0

while Input != Case:
    print('Угадай число ', end='')
    Input = int(input())
    Attemp = Attemp + 1
    if Input < Case:
        print('Слишком маленькое!!!')
    if Input > Case:
        print('Слишком большое ???')
    if Input == Case:
        print('Угадал****!!!')
    if Input == 0:
        print('Правильное число ' + str(Case))
        break
        # exit()
        # continue

print('Ты попробовал ' + str(Attemp) + ' раз.')

