# import random

# Capital = random.randint(2, 10)*10000
# print('Ты выиграл в лотерею ' + str(Capital) +\
#     ' рублей!')
# print('Ты можешь не забирать выигрыш сразу, ', end=' ')
# print('а вложить деньги и заработать на этом !')
# print('Какой суммой ты распологаешь ? ', end=' ')
# Capital = float(input())

# print('Процентная ставка: ', end=' ')

# Percent = float(input())
# Term = 0

# while Capital < 1000000:
#     Fee = Capital * Percent / 100
#     Capital = Capital + Fee
#     Term += 1
#     if Percent <= 0:
#         break

# if Term > 0:
#     print('Чтобы тебе превратиться в миллионера, твои деньги в течение : ',  end= ' ')
#     print(str(Term) + ' лет должны быть в банке .')
# else:
#     print('Добро пожаловать в клуб миллионеров!!! ')
# print('Чтобы стать миллионером, тебе понадобиться ', end=' ')
# print(str(Term) + ' лет.')

print('Какую сумму ты хочешь инвестировать: ')
Capital = float(input())
print('Процентная ставка : ')
Percent = int(input())
print('На какой срок ты вкладываешь деньги :')
Term = int(input())

for Value in range(Term):
    Fee = Capital * Percent / 365
    Capital = Capital + Fee
    Term -= 1
print('Так ты получешь ' + str(Capital) + ' за это время')

if Capital < 1000000:
    print('Но так ты не станешь миллионером!!!')
else:
    print('Добро пожаловать в Клуб дохуярда!!!!')