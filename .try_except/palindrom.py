print('Напиши короткий текст (небольшой, без пробелов): ')
Text_1 = input()
Text_2 = ' '
Chain = len(Text_1)
for Number in range(0, Chain):
    Text_2 += Text_1[Chain - Number - 1]
print(Text_2)
if Text_1 == Text_2:
    print('Палиндром!!**')