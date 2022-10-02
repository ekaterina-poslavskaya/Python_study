# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

list = ['ffff','3rfhg','4h']
for i in list:
    print(type(i))
    try:
        int(i)
        float(i)
        print('YES')
        break
    except:
        pass
