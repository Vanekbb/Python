'''

Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50.
Нужно вывести наибольшее количество идущих подряд положительных чисел.


Input: 6 -> -20 30 -40 50 10 -10

Output: 2

'''
import random

n = input("Введите положительное целое число: ")

while not n.isdigit() or n == "0":
    print("Некорректный ввод")
    n = input("Введите положительное целое число: ")

n = int(n)

max_thaw_days = 0
thaw_days = 0

for i in range(n):
    temprature = random.randint(-50, 50)
    print(temprature, end = " ")
    if temprature > 0:
        thaw_days += 1
    else:
        if thaw_days > max_thaw_days:
            max_thaw_days = thaw_days
        thaw_days = 0

if thaw_days > max_thaw_days:
    max_thaw_days = thaw_days

print()
print(max_thaw_days)