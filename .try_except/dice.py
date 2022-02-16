import random, time
print('Давай бросим кубики!!!')
Att = 0
YoNum = 0
MyNum = 0

#Игральные кубики
while Att < 6:
    Att = Att + 1
    print(str(Att) + ' Раунд')
    print('Твой бросок: ', end='')
    Shoot_1 = random.randint(1, 6) #Твой бросок
    time.sleep(0.5) #Ожидание в полсекунды
    print(Shoot_1)

    print('Мой бросок: ', end='')
    Shoot_2 = random.randint(1, 6) #Мой бросок
    time.sleep(0.5) #Ожидание в полсекунды
    print(Shoot_2)

    if Shoot_1 > Shoot_2:
        YoNum = YoNum + 1
    if Shoot_2 > Shoot_1:
        MyNum = MyNum + 1

    print(str(YoNum ) + ' и ' + str( MyNum) + '\n')
    time.sleep(0.3) #Ожидание в одну секунду
    # print()

#Вычисления
if YoNum > MyNum:
    print('Ты выиграл!!!')
if YoNum < MyNum:
    print('Я выиграл***')
else:
    print('Ничья"""')
        