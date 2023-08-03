"""
Напишите программу, которая  создает массив из чисел от -5 до 5 включительно и выводит его на консоль.

Результат работы программы:
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

"""
out_list = []
for i in range(-5, 6):
    out_list.append(i)

print(out_list)

"""
Напишите программу, которая  создает массив из всех ЧЕТНЫХ чисел от 0 до 100 включительно и выводит его на консоль.
Результат работы программы:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 
76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

"""
out_list = []
for i in range(0, 101, 2):
    out_list.append(i)

print(out_list)


"""
Напишите программу, которая  создает массив из 100 СЛУЧАЙНЫХ  чисел (каждое - в диапазоне от 0 до 100 включительно) и выводит массив на консоль.
Примечание: Как получить случайное число от 1 до 10?

import random
rnd = random.randint(1, 10)


"""
import random


numbers = []
for i in range(100):
    rnd = random.randint(1, 100)
    numbers.append(rnd)

print(numbers)


"""
Модифицируем программу, чтобы она дополнительно вывела все чётные числа из массива, разделяя их символом “;”.

"""
import random


numbers = []
for i in range(100):
    rnd = random.randint(1, 100)
    numbers.append(rnd)

print(numbers)
print(len(numbers))

for i in range(100):
    if numbers[i] % 2 == 0:
        print(numbers[i], end = "; ")


"""
Напишите программу, которая выводит каждый элемент массива X в отдельной строке.
Массив X вводится пользователем в одну строку (1 пробел между элементами).
"""
elements = input().split()

for i in range(len(elements)):
    print(elements[i])


"""
Напишите программу, которая выводит каждый элемент массива X в одну строку без пробелов. 
Массив X вводится пользователем в одну строку (1 пробел между элементами).
"""
elements = input().split()

for i in range(len(elements)):
    print(elements[i], end = "")


"""
Пользователь вводит строку - числа, разделенные пробелом.
Программа должна вывести на консоль все положительные числа.
Выводится числа должны в одну строку, через 1 пробел.
"""
elements = input().split()

for i in range(len(elements)):
    number = int(elements[i])
    if int(number) > 0:
        print(number, end = " ")


"""
Реализация пузырьковой сортировки
"""
array = [3,  7,  4,  4,  6,  5,  8]
array_length = len(array)

for i in range(array_length - 1):
    for j in range(array_length - i - 1):
        if array[j] > array[j + 1]: # если порядок в паре неверный
            array[j], array[j + 1] = array[j + 1], array[j] # меняем местами элементы

print(array)
