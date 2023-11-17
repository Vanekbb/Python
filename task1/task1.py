'''

Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6


'''

from random import randint

listLenght = randint(5, 10)

numList = []

for _ in range(listLenght):
    numList.append(randint(0, 5))

print(numList)