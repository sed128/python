#Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
#*Пример:*

#- 6782 -> 23
#- 0,56 -> 11

num = float(input("Введите число"))
sum = 0
try:
    mantisLen = len(str(num).split(".")[1])
    num *= pow(10,mantisLen+1)
    num = int(num)
    num //= 10
    while num > 0:
        sum += num % 10
        num //= 10

    print(sum)

except:
    print("Повторите ввод")
