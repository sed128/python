#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
#Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('source.txt','r') as sourceFile:
    sourceText = sourceFile.read()
with open('encode.txt','r') as encodeFile:
    encodeText = encodeFile.read()

def encode(ss):
    prevChar = ''
    ret = ''
    count = 1
    for c in ss:
        if prevChar == '':
            prevChar = c
            count = 1
        elif c == prevChar:
            count += 1
        else:
            ret += str(count)
            ret += prevChar
            count = 1
            prevChar = c

    ret += str(count)
    ret += prevChar
    return ret

def decode(ss):
    count = ''
    ret = ''
    for c in ss:
        if c.isdigit():
            count += c
        else:
            ret += c*int(count)
            count = ''
    return ret

print(sourceText)
print(encode(sourceText))
print(encodeText)
print(decode(encodeText))
