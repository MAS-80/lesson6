my_dict={'Petya': 1990,'Vasya': 1986,'Liza': 2000 }
print('словарь:', my_dict)
print('Значение:', my_dict.get('Liza'))
print('Значение:',my_dict.get('Lena'))
my_dict.update({'Fedya': 1999,'Sonya': 2002})
del_=my_dict.pop('Liza')
print('Удаленное значение',del_)
print('новый словарь', my_dict)

my_set={2, 0.25, 'apple', 'home', 2,'apple', 0.25, 'home', (2, 0.25, 5) }
print('множество:', my_set)
my_set.update({'tomato',8})#добавляем пару произвольных элемента
my_set.add(4)#добавляем первый произвольный элемент
my_set.add('cucumber')#добавляем второй произвольный элемент
my_set.discard(0.25)
print('измененное множество:',my_set)
