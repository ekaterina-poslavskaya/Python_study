# Реализуйте алгоритм перемешивания списка
import random

n = int(input('Введите число элементов списка...'))
lst = [random.randint(0,10) for i in range(n)]
print(lst)

random.shuffle(lst)
print(lst)