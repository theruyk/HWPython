# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# n = int(input( 'Введите количество элементов 1 множества: '))
# num_set = set()
# for i in range(n):
#   num = int(input( 'Введите число:'))
#   num_set.add(num)

# m = int(input( 'Введите количество элементов 2 множества: '))
# num_set2 = set()
# for i in range(m):
#   num = int(input( 'Введите число:'))
#   num_set2.add(num)

# result_set = num_set.intersection(num_set2)

# print(*num_set)
# print(*num_set2)
# print(*result_set)


# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

n = int(input( 'Введите количество кустов черники: '))
num_list = []
for i in range(n):
  num = int(input( 'Введите количество ягод на i кусте:'))
  num_list.append(num)
print(*num_list)
sum1=0
for i in range(len(num_list)-1):
  k = num_list[i] + num_list[i+1] + num_list[i-1]
  if k > sum1:
    sum1=k
num_list2 = [num_list[0], num_list[-1], num_list[-2]]
sum(num_list2)
if sum(num_list2) > sum1:
  print(sum(num_list2))
else:print(sum1)
