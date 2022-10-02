#colors = ['red','green','blue']
#data = open('file.txt','a')
#data.writelines(colors)
#data.write('\nLINE2\n')
#data.write('LINE3\n')
#data.close()

#with open('file.txt','a') as data:
#    data.write('line 4\n')
#    data.write('line 5\n')


#path = 'file.txt'
#data = open(path,'r')
#for line in data:
#    print(line)
#data.close()    

import task002
print(task002.f(1))
print(task002.new_string('!',5))
print(task002.new_string('!'))
print(task002.concatenatio('a','d','g','t','i'))
print(task002.int_concatenatio(1,2,3,4,5))

list = []
for e in range(1,10):
    list.append(task002.fib(e))
print(list)    

a = (3, 4, 41, 5)
print(a)
print(a[-2])
b = (3,)
print(b[0])

for item in a:
    print(item)

a1, a2, a3, a4 = a

dic = {}
dic = \
    { 'up':'.',
      'left':'<-',
      'right':'->',
      'down':'|'
    }
for i in dic.keys():
    print(i)  
    print(dic[i])  

for i in dic.values():
    print(i)

for i in dic:
    print(i)        

colors = {'red','green','blue'}
print(colors)
colors.add('grey')
#colors.remove('black')
colors.discard('black')

a ={1,2,3,4,5,8}
b = {2,7,9,0}
c = a.copy()
d = a.union(b)

s = frozenset(a)


list1 = [1,2,3,4,5]
list2 = list1

print(list1)
print(list2)

list1[0] = 123
list2[1] = 456

print(list1)
print(list2)
list1.pop(1)
print(list1)
list1.pop()
print(list1)
list1.pop()
print(list1)

list1.insert(2,11)
print(list1)

list1.append(222)
print(list1)
