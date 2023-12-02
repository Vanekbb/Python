'''

Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод:                   Вывод:
values = [0, 2, 10, 6]      same

if same_by(lambda x: x % 2, values):
    print(‘same’)
else:
    print(‘different’)

'''

def same_by_1(characteristic, objects):
    if len(objects) == 0:
        return True
    
    for i in range(len(objects)):
        if characteristic(objects[i]) == 0:
            objects[i] = True
        else:
            objects[i] = False

    objects = set(objects)

    if False in objects and True in objects:
        return False
    else:
        return True


values = [0, 2, 10, 6]

if same_by_1(lambda x: x % 2, values):
    print("same_1")
else:
    print("different_1")

# 2

def same_by_2(characteristic, objects):
    if len(objects) == 0:
        return True

    check_0 = characteristic(objects[0])

    for i in objects[1:]:
        if check_0 != characteristic(i):
            return False
    return True

if same_by_2(lambda x: x % 2, values):
    print("same_2")
else:
    print("different_2")

# 3

def same_by_3(characteristic, objects):
    res_set = {characteristic(i) for i in objects}

    if len(res_set) <= 1:
        return True
    return False

if same_by_3(lambda x: x % 2, values):
    print("same_3")
else:
    print("different_3")

# 4

def same_by_4(characteristic, objects):
    if len(objects) == 0:
        return True
    
    result = list(filter(characteristic, objects))

    if len(objects) == len(result) or len(result) == 0:
        return True
    return False

if same_by_4(lambda x: x % 2, values):
    print("same_4")
else:
    print("different_4")

# 5

def same_by_5(characteristic, objects):
    if len(objects) == 0:
        return True
    
    result = list(map(characteristic, objects))

    if all(result) == any(result):
        return True
    return False

if same_by_5(lambda x: x % 2, values):
    print("same_5")
else:
    print("different_5")
