#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#*Пример:*
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 10
koef = [randint(0,100) for i in range (k+1)]
res = ""

for i in range (k):
    if koef[i] > 0:
        if len(res) > 0:
            res += ' + '
        res += str(koef[i]) + '*x^' + str(k-i)

if koef[k] > 0:
    if len(res) > 0:
        res += ' + '
    res += str(koef[k])

if len(res) > 0:
    res += ' = 0'
    print(res)
    with open('result.txt', 'w') as data:
        data.write(res)
else:
    print("WTF???")
