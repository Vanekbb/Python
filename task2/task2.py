'''

Дан список размеров(длина, ширина) эллипсов:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
- Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.


Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

Вывод:
2.5 10

'''

'''
def find_farthest_orbit(list_of_orbits):
    max_orbit = 0
    for a, b in list_of_orbits:
        if a == b:
            continue
        s = 3.14 * a * b
        if max_orbit < s:
            max_orbit = s
            result = a, b
    return result
'''

def find_farthest_orbit(list_of_orbits):
    list_of_orbits = list(filter(lambda sizes: sizes[0] != sizes[1],list_of_orbits))
    list_max_areas = [3.14 * a * b for a, b in list_of_orbits]
    max_area = max(list_max_areas)
    index_max_area = list_max_areas.index(max_area)
    return list_of_orbits[index_max_area]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
