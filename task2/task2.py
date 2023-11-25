'''

Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки намаксимальные. 
Напишите программу, котораязаменяет оценки Василия,
но наоборот: все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1

'''
from random import randint

userNum = int(input("Введите число: "))

marks = list()

for i in range(userNum):
    marks.append(randint(1, 5))

print(marks)

minNum = marks[0]
maxNum = marks[0]

for i in marks:
    if i < minNum:
        minNum = i
    elif i > maxNum:
        maxNum = i

for i in range(len(marks)):
    if marks[i] == maxNum:
        marks[i] = minNum

print(marks)