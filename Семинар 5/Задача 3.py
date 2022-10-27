#Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

magicText = "абв"

source = "абв йцу кен гшщ фыв апр олд жэё ячс мит ьбю абвгд йцукен вабв"

def delMagic(ss,magic):
    ssList = ss.split()
    ret = ''
    for c in ssList:
        if magic not in c:
            ret += c
            ret += ' '

    return ret

print(delMagic(source,magicText))