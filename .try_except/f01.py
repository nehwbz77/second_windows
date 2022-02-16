import random

def initGame () :
    # global Input, Attempt

    Secret = 'Я задумал число от 1 до 1000'
    print(Secret)
    # Attempt = 0
    # Input = 0


def playGame(Input, Attempt):
    # global Input, Attempt
    Case = random.randint(1, 1000)

    while Input != Case:
        print('Угадай число: ', end=' ')
        Input = int(input())
        Attempt += 1

        if Input < Case:
            print('Слишком маленькое ! ')
        if Input > Case:
            print('Слишком большое ! ')
        if Input == Case:
            print('Угадал !!! *** ')
    return Attempt

# playGame(0, 0)


def endGame(Attempt):
    print('Ты попробовал ' + str(Attempt) + ' раз. ')

initGame()
Game = playGame(0, 0)
endGame(Game)

