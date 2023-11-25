'''

Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)

Input: 5

Output: yes

'''

def checkNum(n):
    for div in range(2, n):
        if n % div == 0:
            return False
    return True
    
userNum = int(input("Введите число: "))
print(checkNum(userNum))