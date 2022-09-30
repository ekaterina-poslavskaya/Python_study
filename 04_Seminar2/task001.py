# a = [i**2 for i in range(10)]
# print(a)

#b = {i:i*2 for i in range(10)}
#print(b)

#b.update({200:4000})
#print(b)
# 1. Напишите программу, которая принимает на вход число N и 
# выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число N='))
lst = []
if n >= 1:
    lst.append(1)
    for i in range(1,n):
        lst.append(lst[i-1]*(-3))
    print(lst)    
else:
    print('Количество элементов должно быть больше 0')

lst1 = [(-3)**i for i in range(n)]   
print(lst1)