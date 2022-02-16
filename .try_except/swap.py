def exchange(x1, x2):
    Swap = x1
    x1 = x2
    x2 = Swap
    # print('Меняем : ' + str(x1) + ' и ' + str(x2))
    # return x1, x2

#Основная программа
print('Введи число : ', end='')
Num_1 = int(input())
print('И еще одно : ', end='')
Num_2 = int(input())
print('До обмена : ' + str(Num_1) + ' и ' + str(Num_2))
# exchange(Num_1, Num_2)
(Num_1, Num_2) = exchange(Num_1, Num_2)
print('После обмена : ' + str(Num_1) + ' и ' + str(Num_2))
