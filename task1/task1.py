'''

Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: 7 6

Вывод:

3 1 3 4 2 4 12

4 15 43 1 15 1 

'''

from random import randint

def getArray(size):
    #result = []
    #for _ in range(size):
    #    result.append(randint(0, 5))

    return [randint(0, 5) for _ in range(size)]

def arrDiff(array1, array2):
    #result = []
    #for i in array1:
    #    if i not in array2:
    #        result.append(i)

    return [i for i in array1 if i not in array2]

size_1 = int(input("Введите число первого массива: "))
size_2 = int(input("Введите число второго массива: "))

arr_1 = getArray(size_1)
arr_2 = getArray(size_2)

print(arr_1)
print(arr_2)
print(arrDiff(arr_1, arr_2))