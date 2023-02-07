# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# size_array = ((int(input('Input size array '))))
# list1=[0]*(size_array)
# for i in range(len(list1)):
#   list1.append(int(input('Input number ')))
# num_we_search = (int(input('Input searching number ')))
# count =0
# for i in range(len(list1)):
#   if num_we_search == list1[i]:
#     count+=1
# print(count)
    

# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

# while True:
#   import math
#   size_array = ((int(input('Input size array '))))
#   list1=[0]*(size_array)
#   for i in range(len(list1)):
#     list1.insert(i,(int(input('Input number '))))
#   for i in range(len(list1)-1,-1,-1):# избавляемся от нулей
#     if list1[i] == 0:
#         list1.pop(i)
#   num_we_search = (int(input('Input searching number ')))
#   if max(list1) < num_we_search:
#     print (max(list1))
#   elif num_we_search < min(list1):
#     print(min(list1))
#   else: 
#     array_bigger= list()
#     array_smaller=list()
#     for i in range(len(list1)):
#       if num_we_search == list1[i]:
#         print (list1[i])
#         break
#       if list1[i] > num_we_search:
#         array_bigger.append(list1[i])
#       elif list1[i] < num_we_search:
#         array_smaller.append(list1[i])
#     if ((max(array_smaller) + min(array_bigger))//2 == num_we_search): # не знаю как избавиться от ошибки в одном из сценариев
#         print(min(array_bigger),max(array_smaller))
#     elif num_we_search > array_smaller[i]:
#         print(max(array_smaller))
#     elif num_we_search < array_smaller[i]:
#        print(min(array_bigger))


# Задача 3.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом
#  очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка;B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;K – 5 очков;J, X – 8 очков;Q, Z – 10 очков.
# А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка;Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается
# только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример
# ноутбук
# 12