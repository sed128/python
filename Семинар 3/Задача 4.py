#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
#*Пример:*

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

number = 45
numberBin = ''

while number > 0:
    numberBin = str(number % 2) + numberBin
    number = number // 2

print(numberBin)