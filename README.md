# Python_study

# a = [i**2 for i in range(10)]
# print(a)

#b = {i:i*2 for i in range(10)}
#print(b)


print('Введите а');
a = input()
print('Введите b');
b = input()
print(a, b)
print('{} -- {}'.fotmat(a, b))

print('Введите а');
a = int(input())
print('Введите b');
b = int(input())
c = 30
print(a, ' + ', b, ' = ', c)
print('{} + {} = {}'.format(a, b, c))

a = int(input('Введите а: ')) # 11
b = int(input('Введите b: ')) # 22
c = 33
print('{} + {} = {}'.format(a, b, c))

a, b, c = 1, 2, 3
# a: 1 b: 2 c: 3
print('a: {} b: {} c: {}'.format(a, b, c))
range(*(1,5,2)))

for i in 1, -2, 3, 14, 5:
print(i)

print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

 