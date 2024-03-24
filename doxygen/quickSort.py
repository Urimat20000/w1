"""! @brief Определяет функцию быстрой сортировки"""
##
# @file quicksort.py
#
# @brief Файл с функцией быстрой сортировки.
#
# @section description_sensors Описание
# Данный алгоритм сортировки имеет среднее время сортировки O(n log n)
print(aa)
# Functions
def quickSort(array):
    """! Сама функция сортировки."""
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)
    else:
        return array

