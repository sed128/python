#Создайте программу для игры с конфетами человек против бота.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#Делаем игру против бота
#а) Подумайте как наделить бота ""интеллектом""

from random import randint

candy = 2021
candyStepLimit = 28
currentPlayer = 0
count = 0

print("Игра с конфетами")
print(f'Перед нами кучка из {candy} конфет. Разрешается брать не более {candyStepLimit} конфет за раз')

if randint(0,1) == 0:
    currentPlayer = 0
else:
    currentPlayer = 1

while 1:
    if candy == 0:
        print(f'Выйграл игрок {currentPlayer}')
        break
    else:
        currentPlayer += 1
        if currentPlayer > 1:
            currentPlayer = 0
        print(f'Остаток конфет {candy}, ходит игрок {currentPlayer}')

    if currentPlayer:
        while 1:
            count = int(input("Сколько конфет вы берете?"))
            if count > 0 and count <= candyStepLimit and count <= candy:
                break
    else:
        if candy >= 28+28+1:
            count = 28
        elif candy >= 28 + 1:
            count = candy - 28 - 1
        else:
            count = candy

    candy -= count
    print(f'Игрок {currentPlayer} взял {count} конфет')


