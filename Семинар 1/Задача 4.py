# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

a = float(input("Введите первый операнд "))
b = float(input("Введите второй операнд "))
c = input("Введите операцию (+, -, /, *, mod, pow, div) ")

if c == "+":
    print(f'{a} {c} {b} = {a+b}')
elif c == "-":
    print(f'{a} {c} {b} = {a - b}')
elif c == "/" and b == 0:
    print("Ошибка деления на 0!")
elif c == "/" and b != 0:
    print(f'{a} {c} {b} = {a / b}')
elif c == '*':
    print(f'{a} {c} {b} = {a * b}')
elif c == 'mod':
    print(f'{a} {c} {b} = {a % b}')
elif c == 'pow':
    print(f'{a} {c} {b} = {pow(a,b)}')
elif c == 'div':
    print(f'{a} {c} {b} = {a // b}')
else:
    print("Неизвестная операция!")

