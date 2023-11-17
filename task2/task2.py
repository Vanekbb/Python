'''

Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность(сдвиг - циклический) 
на K элементов вправо, K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3

Output: [4, 5, 1, 2, 3]


'''
from random import randint

k = int(input("Введите число: "))
listLenght = randint(5, 10)

numList = [randint(0, 5) for _ in range(listLenght)]
print(numList)
print(numList[-k:])
print(numList[:-k])
print(numList[-k:] + numList[:-k])

#2

for shift in range(k):
    shifterNum = numList.pop()
    numList.insert(0, shifterNum)

print(numList)