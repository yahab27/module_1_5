tuple_ = 1, 's' , 3.745, 'name' # формирование кортежа
print ('immutable_var: ', tuple_ ) # вывод на экран кортежа
# tuple_[1] = 7 кортеж – это неизменяемая упорядоченная коллекция,
# print (tuple_) которая не поддерживает обращение по элементам
mutable_list = [3 ,5, 'a', 'apple'] # формирование списка
print (mutable_list) # вывод списка на экран
mutable_list[2]='27' # замена третьего элемента списка
print (mutable_list) # вывод на экран измененного списка

