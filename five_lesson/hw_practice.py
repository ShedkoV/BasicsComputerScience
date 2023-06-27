"""
1. Дополните приведенный код, используя индексатор, так чтобы он вывел 17-ый элемент списка primes.
"""
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])


"""
2. Дополните приведенный код, используя индексатор, так чтобы он вывел последний элемент списка primes.
"""
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])


"""
3. Дополните приведенный код, используя срезы, так чтобы он вывел первые 6 элементов списка primes.

Примечание. Результатом вывода должна быть строка [2, 3, 5, 7, 11, 13].
"""
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])


"""
4. Дополните приведенный код так, чтобы он вывел "перевёрнутый" список languages (т.е. элементы будут идти в обратном порядке).
"""
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])


""""
5. На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Пример: Владимир Семенович Высоцкий

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи. Пример: В.С.В.
"""
full_name = input('Введите ФИО: ').split()
print(
    full_name[0][0] + '. ' + full_name[1][0] + '. ' + full_name[2][0] + '.'
)



"""
6. Пользователь вводит строку - числа, разделенные пробелом.
Программа должна вывести на консоль все числа из массива, меньшие 0, но большие -2022. Выводится числа должны в одну строку, через 1 пробел.

"""
elements = input().split()

for i in range(len(elements)):
    number = int(elements[i])
    if number < 0 and number > -2022:
        print(number, end = " ")



"""
7. Пользователь вводит строку - числа, разделенные пробелом.
Программа должна вывести на консоль сумму всех введенных чисел.

"""
elements = input().split()

summa = 0
for i in range(len(elements)):
    number = int(elements[i])
    summa = summa + number

print(summa)


"""
8. Пользователь вводит строку - числа, разделенные пробелом.
Программа должна вывести на консоль произведение всех чисел.

"""
elements = input().split()

summa = 1
for i in range(len(elements)):
    number = int(elements[i])
    summa = summa * number

print(summa)


"""
9. Пользователь вводит строку - числа, разделенные пробелом.
Программа должна вывести на консоль квадраты всех чисел. Выводится числа должны в одну строку, через 1 пробел.

"""
elements = input().split()

for i in range(len(elements)):
    number = int(elements[i])
    print(number ** 2, end = " ")


"""
10. Вывести из приложенного списка восклицательный знак
"""
some_list = [
    [12, 2, 4],
    [True, None, -12],
    ['Hello, World!', 'true', False],
    [34, 1],
]
print(
    some_list[2][0][-1]
)
