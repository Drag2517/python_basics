"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
import sys

A = 1
NUMBER_1 = 0


def number(list_data):
    """Функция для перевода списка в числовую последовательность и суммирования этих чисел"""
    list_data = list_data.split()
    result_1 = 0
    data_list_2 = list(map(int, list_data))
    result_1 = result_1 + sum(data_list_2)
    return result_1


while A > 0:
    data_list_1 = input("Введите числовую последовательность  ")
    for el in data_list_1:
        if 's' in data_list_1:
            i = data_list_1.rfind('s')
            if i != -1:
                data_list_1 = data_list_1[:i - 1]
            NUMBER_1 = NUMBER_1 + number(data_list_1)
            print(f"Результат: {NUMBER_1} ")
            sys.exit()
    NUMBER_1 = NUMBER_1 + number(data_list_1)
<<<<<<< HEAD
    print(f"Результат: {NUMBER_1} ")
=======
    print(f"Результат: {NUMBER_1} ")
>>>>>>> Amendments_Homework#1,2,3
