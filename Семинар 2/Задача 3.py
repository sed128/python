# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.

str1 = input("Введите строку 1")
str2 = input("Введите строку 2")

str1List = list(str1)
str2List = list(str2)

findCount = 0
flag = False

for i in range(len(str1)):
    flag = True
    for j in range(len(str2)):
        if (str1List[i+j] != str2List[j]):
            flag = False
            break

    if flag:
        findCount += 1

print(findCount)
