# Найти длину высоты треугольника, проведённой из наименьшего угла
# Степнов Сергей
# Группа ИУ7-16Б

from math import sqrt

a_x, a_y = map(float, input("Введите координаты точки A в формате 'x y': ").split())
b_x, b_y = map(float, input("Введите координаты точки B в формате 'x y': ").split())
c_x, c_y = map(float, input("Введите координаты точки C в формате 'x y': ").split())

length_ab = sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)
length_bc = sqrt((b_x - c_x) ** 2 + (b_y - c_y) ** 2)
length_ac = sqrt((a_x - c_x) ** 2 + (a_y - c_y) ** 2)

semi_perimeter = (length_ab + length_bc + length_ac) / 2
area_abc = sqrt(semi_perimeter * (semi_perimeter - length_ab) * (semi_perimeter - length_bc) *
                (semi_perimeter - length_ac))

if area_abc == 0:
    print("\nФигура не является треугольником")
else:
    print(f"\nДлина высоты, проведённой из наименьшего угла: "
          f"{format(2 * area_abc / min(length_ab, length_bc, length_ac), '.5g')}")
