'''

На вход программе подаются натуральные числа,как только пользователь введёт 0 ввод прекращается. 
Вывести наибольший элемент получившейся последовательности».

Есть два кода с ошибками, нужно определить где ошибок меньше.

'''

#Ваня:
n = int(input())

max_number = n #1 max_number = 1000

while n != 0:
    n = int(input())
    if max_number < n: #2 max_number > n
        max_number = n
print(max_number)

#Петя:
n = int(input())

max_number = -1

while n > 0: #1 n < 0
    n = int(input())
    if max_number < n:
        max_number = n #3 n = max_number
    n = int(input()) #2 перенесли строку нижу if
print(max_number) #4 print(n)