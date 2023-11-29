'''

Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.

Ввод:       Вывод:
1 2 3 2 3       2

'''

from random import randint

def getArray(size):
    return [randint(0, 5) for _ in range(size)]

def checkRepeat(array):
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
    return count

arrSize = int(input("Введите размер массива: "))

userArray = getArray(arrSize)
print(userArray)

print(checkRepeat(userArray))