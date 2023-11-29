'''

(пользовательский ввод можно заменить на рандомный)
Пользователь вводит размер массива – N
и элементы массива (целые числа).
нужно из этого массива вывести количество элементов, у которых ближайшие соседние элементы меньше самого элемента.

Ввод:       Ввод:
    5            5
1 2 3 4 5    1 5 1 5 1

Вывод: Вывод:
     0       2

'''
from random import randint

def getArray(size):
    return [randint(0, 5) for _ in range(size)]

def getCount(array):
    count = 0
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            count += 1
    return count

arrSize = int(input("Введите размер массива: "))

userArray = getArray(arrSize)
print(userArray)

print(getCount(userArray))


# 2

print(sum([1 for i in range(1, len(userArray) - 1) if userArray[i - 1] < userArray[i] > userArray[i + 1]]))