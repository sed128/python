#Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

source = [1.1, 1.2, 3.1, 5, 10.01]
flag = True
minElement = maxElement = 0

for element in source:
    if '.' not in str(element):
        continue
    if flag:
        minElement = maxElement = element % 1
        flag = False
    else:
        if minElement > element % 1:
            minElement = element % 1
        if maxElement < element % 1:
            maxElement = element % 1

if flag:
    print("Некорректный список")
else:
    print(maxElement - minElement)