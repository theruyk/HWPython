# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# import random

# n = int(input('Input current of coins '))
# current_of_coins = list()
# for i in range (n):
#   current_of_coins.append(random.randint(0,1))
# print(current_of_coins)

# count1 = 0
# count0 = 0

# for i in range((len(current_of_coins))):
#   if current_of_coins[i] ==1:
#     count1+=1
#   else: count0 +=1
# if count1 > count0: 
#   print (count0)
# else: print (count1)

# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел
# S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2


# s = int(input('Input sum of numbers  '))
# p = int(input('Input product of numbers  '))


# if(s == p):
#     print(s//2, p//2)
# for x in range(s-1):
#     y = s-x
#     if(p==x*y):          
#         print(f'x = {x}, y = {y}')
#         break



# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

import math
import math

list1 = [num for num in range(int(input('Input number '))+1)]


list2=list()
for i, num in enumerate(list1):
    if (2**(list1 [i])) < list1[-1]:
      list2.append(2**(list1 [i]))
print (*list2)
