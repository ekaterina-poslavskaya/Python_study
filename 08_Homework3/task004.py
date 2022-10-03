# 4. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

#*Пример:*

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

num = int(input('Введит десятичное число..'))
num_abs = abs(num)
s = ''
while num_abs != 0 and num_abs != 1:
    #s = str(num_abs % 2) + s
    #num_abs = num_abs // 2
    num_abs,b = divmod(num_abs, 2) #вместо предыдущих двух строк можно еще и так
    s = str(b) + s
s = str(num_abs) + s
if num < 0:
    s = '-' + s
print(s)