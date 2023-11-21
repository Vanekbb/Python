'''

Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)

Input: [0, -1, 5, 2, 3]

Output: 2 (-1 < 5, 2 < 3)

'''

from random import randint

listLenght = randint(5, 10)

numList = []

for _ in range(listLenght):
    numList.append(randint(-1, 5))

print(numList)

count = 0

for i in range(len(numList) - 1):
    if (i < len(numList) - 1):
        if (numList[i] < numList[i + 1]):
            count += 1

print(count)

# 2

new_list = [1 for i in range(len(numList)-1) if numList[i] < numList[i+1]]
print(sum(new_list))

new_list = [1 if numList[i] < numList[i+1] else 0 for i in range(len(numList)-1)]
print(sum(new_list))