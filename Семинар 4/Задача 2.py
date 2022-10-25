# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

source = [1,3,4,2,5,6,7,9,2,3,6,9,7,2]

ret = []

for i in source:
    flag = False
    for j in ret:
        if j == i:
            flag = True
    if flag == False:
        ret.append(i)

print(ret)