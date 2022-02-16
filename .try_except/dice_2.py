# Игральные кубики
import random, time
print('Давай бросим кубики!')
YoNum = 0
MyNum = 0

for Nr in range(6):
    print(str(Nr + 1) + ' Раунд')

    print('Твой бросок: ', end='')
    Shoot_1 = random.randint(1, 6) #Твой бросок
    time.sleep(0.5) #Ожидание в полсекунды
    print(Shoot_1)

    print('Мой бросок: ', end='')
    Shoot_2 = random.randint(1, 6) #Мой бросок
    time.sleep(0.5) #Ожидание в полсекунды
    print(Shoot_2)

    if Shoot_2 > Shoot_1:
        MyNum = MyNum + 1
    if Shoot_1 > Shoot_2:
        YoNum = YoNum + 1
    if Shoot_2 == Shoot_1:
        MyNum = MyNum + 1 
        YoNum = YoNum + 1
    print(str(YoNum) + ' и ' + str(MyNum))
    # print(str(MyNum) + ' и ' + str(YoNum))
    time.sleep(1) #Ожидание в секунду
    print()

#ВЫчисления победителя
if YoNum > MyNum:
    print('Ты победил *** ')
if YoNum < MyNum:
    print('Я победил !!! ')
else:
    print('Ничья%%%%')
