# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# nubmer = int(input('Input three-digit number '))
# if (nubmer < 999) and (nubmer >99):
#   hundreds = nubmer//100
#   tens = nubmer//10
#   print((nubmer % 10) + hundreds + (tens % 10))
# else :print('It is not three-digit number')


# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#  Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и 
# Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# Total_birds = int(input('Input an even number of birds '))
# if Total_birds % 2 == 0:
#   Katyas_work = int(Total_birds/3)*2
#   Peter=Sergay= int(Katyas_work/4)
#   print(f'Катя сделала {Katyas_work} журавликов, Петя {Peter} журавликов, и Сережа {Sergay} журавликов" ')
# else: print('The number is not even')


# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
#  и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
#  где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 
# – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.
# 385916 -> yes
# 123456 -> no

# tikets_num = int(input('Input positive six-digit number '))
# if tikets_num >99999 and tikets_num < 10000000:
#   first_num = tikets_num // 1000
#   second_num = tikets_num % 1000
#   first_sum = ((first_num // 100) + (first_num % 10) + ((first_num // 10) % 10))
#   second_sum = ((second_num // 100) + (second_num % 10) + ((second_num // 10) % 10))
#   if first_sum == second_sum:
#     print('yes')
#   else :print('no')
# else: print('Conditions not met')


# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на
#  два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('Input first positive number '))
n = int(input('Input second another positive number '))
k = int(input('Input third positive number '))
if m !=n:
  size_of_chokolate = m*n
  balance = size_of_chokolate - k
if (m == k or n == k) or (k % m ==0 or k % n ==0 ):
    print('yes')
else: print('no')
