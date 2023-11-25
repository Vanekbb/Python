'''

Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)

Input: 5

Output: yes

'''

def checkNum(n):
    if n == 2:
        return "yes"
    if n % 2 == 1:
        return "yes"
    else:
        return "no"
    
userNum = int(input("Введите число: "))
print(checkNum(userNum))