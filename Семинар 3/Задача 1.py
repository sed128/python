#Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

source = [2,3,5,9,3]
sum = 0
index = 1

while index <= len(source)-1:
    sum += source[index]
    index += 2

print(sum)
