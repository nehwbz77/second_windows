import random
Capital = random.randint(2, 10)*10000
print('Ты выиграл в лотерею ' + str(Capital) + 'рублей!')
print('Ты можешь не звабирать выигрышь сразу, ', end='')
print('а вложить деньги и заработать на этом!')
print('Процентная ставка: ', end='')

Percent = float(input())
Term = 0

while Capital < 10000000:
    Fee = Capital * Percent / 100
    Capital = Capital + Fee
    Term += 1

print('Чтобы стать миллионером, тебе понадобится ', end='')
print(str(Term) + ' лет.')