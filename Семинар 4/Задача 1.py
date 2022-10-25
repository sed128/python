#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = 456

numList = []
d = 2
while d * d <= N:
    if N % d == 0:
        numList.append(d)
        N //=d
    else:
        d += 1
if N > 1:
    numList.append(N)

print(numList)