# Программа для:
# 1) нахождения длин сторон треугольника
# 2) нахождения длины биссектриссы большего угла треугольника
# 3) определения типа треугольника (равнобедренный или нет)
# 4) определения расположения точки относительно треугольника,
#    если лежит внутри, вывести расстояние до ближайшей стороны
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from math import sqrt


# Вычисление площади по трём сторонам
def area(side_1, side_2, side_3):
    semi_perimeter = (side_1 + side_2 + side_3) / 2
    return sqrt(semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3))


# Ввод данных
a_x, a_y = map(int, input("Введите координаты точки A в формате 'x y': ").split())
b_x, b_y = map(int, input("Введите координаты точки B в формате 'x y': ").split())
c_x, c_y = map(int, input("Введите координаты точки C в формате 'x y': ").split())

# Нахождение длин сторон треугольника
length_ab = sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)  # Длина отрезка AB
length_bc = sqrt((b_x - c_x) ** 2 + (b_y - c_y) ** 2)  # Длина отрезка BC
length_ac = sqrt((a_x - c_x) ** 2 + (a_y - c_y) ** 2)  # Длина отрезка AC

if area(length_ab, length_bc, length_ac) == 0:
    print("Фигура не является треугольником")
    exit()

# Нахождение длины биссектрисы большего угла
a, b, c = sorted([length_ab, length_bc, length_ac])
s_p = (a + b + c) / 2  # Полупериметр
len_bisector = 2 * sqrt(a * b * s_p * (s_p - c)) / (a + b)  # Длина биссектрисы большего угла

# Определение треугольника на равнобедренность
is_isosceles = False
if a == b or b == c:
    is_isosceles = True

# Вывод ответа на пункты 1-3
print(f"AB: {format(length_ab, '.5g')}\n"
      f"BC: {format(length_bc, '.5g')}\n"
      f"AC: {format(length_ac, '.5g')}\n"
      f"Длина биссектрисы из большего угла: {format(len_bisector, '.5g')}\n"
      f"Треугольник равнобедренный?: {is_isosceles}\n")

# Ввод данных
m_x, m_y = map(int, input("Введите координаты точки M в формате 'x y': ").split())

# Векторное произведение
vec_ab = (a_x - m_x) * (b_y - a_y) - (a_y - m_y) * (b_x - a_x)
vec_bc = (b_x - m_x) * (c_y - b_y) - (b_y - m_y) * (c_x - b_x)
vec_ac = (c_x - m_x) * (a_y - c_y) - (c_y - m_y) * (a_x - c_x)

# Определение расположения точки относительно треугольника
if (vec_ab <= 0) == (vec_bc <= 0) == (vec_ac <= 0):
    # Нахождение длин отрезков AM, BM и CM
    am = sqrt((a_x - m_x) ** 2 + (a_y - m_y) ** 2)  # Длина отрезка AM
    bm = sqrt((b_x - m_x) ** 2 + (b_y - m_y) ** 2)  # Длина отрезка BM
    cm = sqrt((c_x - m_x) ** 2 + (c_y - m_y) ** 2)  # Длина отрезка CM

    # Нахождение длин перпендикуляров из точки M на AB, BC и AC
    distance_m_ab = 2 / length_ab * area(am, bm, length_ab)  # Длина перпендикуляра из точкм M на AB
    distance_m_bc = 2 / length_bc * area(bm, cm, length_bc)  # Длина перпендикуляра из точкм M на BC
    distance_m_ac = 2 / length_ac * area(am, cm, length_ac)  # Длина перпендикуляра из точкм M на AC

    # Вывод ответа на 4 пункт
    print("Точка M лежит внутри треугольника\n"
          f"Расстояние до ближайшей стороны треугольника: "
          f"{format(min(distance_m_ab, distance_m_bc, distance_m_ac), '.5g')}")
else:
    # Вывод ответа на 4 пункт
    print("Точка M не лежит внутри треугольника")
