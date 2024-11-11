from random import *

x = randint(0,100)
print('Угадайте число от 1 до 100')
while True:
    y = int(input('Введите число: '))
    if y < x:
        print('Ваше число меньше того, что загадано')
    elif y > x:
        print('Ваше число больше того, что загадано')
    else:
        print('Угадали')
        break