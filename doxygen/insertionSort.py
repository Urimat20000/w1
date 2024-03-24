"""! @brief Определяет функцию сортировки вставками"""
##
# @file insertionSort.py
#
# @brief Файл с функцией сортировки вставками.
#
# @section description_sensors Описание
# Данный алгоритм сортировки имеет среднее время сортировки O(n^2)
print(aa)
# Functions
def insertionSort(arr):
    """! Сама функция сортировки вставками."""
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i
        while j>0 and arr[j-1]>x:
            arr[j] = arr[j-1]
            j-=1

        arr[j] = x

    return arr





