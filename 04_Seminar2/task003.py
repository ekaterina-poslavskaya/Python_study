# 3. Напишите программу, в которой пользователь 
# будет задавать две строки, а
# программа - определять количество вхождений 
# одной строки в другой.

str1 = input()
str2 = input()
print(f'Строка "{str1}" входит в строку "{str2}" {str2.count(str1)} раз')
print(f'Строка "{str2}" входит в строку "{str1}" {str1.count(str2)} раз')