#2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

#*Пример:*

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
lst = list(map(int, input('Введите элементы списка через ",": ').split(',')))
print(lst)
s = 0
for i in range(len(lst)//2):
    print(f'lst[{i}] * lst[{len(lst)-1-i}] = {lst[i] * lst[len(lst)-1-i]}') 
if len(lst)%2 == 1:
    print(f'lst[{len(lst)//2+1}] = {lst[len(lst)//2+1]**2}') 