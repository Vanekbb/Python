'''

Пользователь вводит одно число N. Далее идут N чисел, записанных на новой строчке каждое.
Вывести максимальное и минимальное (циклы)

Input: 5 -> 5 1 6 5 9

Output: 1 9

'''

n = input("Введите положительное целое число: ")

while not n.isdigit() or n == "0":
    print("Некорректный ввод")
    n = input("Введите положительное целое число: ")

n = int(n)

userWeight = int(input("Введите число: "))

minNum = userWeight
maxNum = userWeight

for i in range(n - 1):
    weight = int(input("Введите число: "))
    if weight > maxNum:
        maxNum = weight
    elif weight < minNum:
        minNum = weight

print()
print(f"Минимальное значение = {minNum}, максимальное значение = {maxNum}")