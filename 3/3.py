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

# Ввод данных
a_x, a_y = map(int, input("Введите координаты точки A в формате 'x y': ").split())
b_x, b_y = map(int, input("Введите координаты точки B в формате 'x y': ").split())
c_x, c_y = map(int, input("Введите координаты точки C в формате 'x y': ").split())

# Основной блок программы
# Нахождение длин сторон треугольника
len_ab = sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)  # Длина отрезка AB
len_bc = sqrt((b_x - c_x) ** 2 + (b_y - c_y) ** 2)  # Длина отрезка BC
len_ac = sqrt((a_x - c_x) ** 2 + (a_y - c_y) ** 2)  # Длина отрезка AC

# Нахождение длины биссектрисы большего угла
a, b, c = sorted([len_ab, len_bc, len_ac])
p = (a + b + c) / 2  # Полупериметр
len_bisector = 2 * sqrt(a * b * p * (p - c)) / (a + b)  # Длина биссектрисы большего угла

# Определение треугольника на равнобедренность
is_isosceles = False
if a == b or b == c:
    is_isosceles = True

# Вывод ответа на пункты 1-3
print(f"AB: {format(len_ab, '.5g')}\n"
      f"BC: {format(len_bc, '.5g')}\n"
      f"AC: {format(len_ac, '.5g')}\n"
      f"Длина биссектрисы из большего угла: {format(len_bisector, '.5g')}\n"
      f"Треугольник равнобедренный?: {is_isosceles}\n")

# Ввод данных
m_x, m_y = map(int, input("Введите координаты точки M в формате 'x y': ").split())

# Векторное произведение
vec_ab = (a_x - m_x) * (b_y - a_y) - (a_y - m_y) * (b_x - a_x)
vec_bc = (b_x - m_x) * (c_y - b_y) - (b_y - m_y) * (c_x - b_x)
vec_ac = (c_x - m_x) * (a_y - c_y) - (c_y - m_y) * (a_x - c_x)

# Проверка на знаки
if (vec_ab < 0) == (vec_bc < 0) == (vec_ac < 0):
    # Нахождение длин отрезков AM, BM и CM
    len_am = sqrt((a_x - m_x) ** 2 + (a_y - m_y) ** 2)  # Длина отрезка AM
    len_bm = sqrt((b_x - m_x) ** 2 + (b_y - m_y) ** 2)  # Длина отрезка BM
    len_cm = sqrt((c_x - m_x) ** 2 + (c_y - m_y) ** 2)  # Длина отрезка CM

    # Нахождение длин перпендикуляров из точки M на AB, BC и AC
    m_ab_p = (len_am + len_bm + len_ab) / 2  # Полупериметр треугольника ABM
    len_m_ab = 2 / len_ab * sqrt(m_ab_p * (m_ab_p - len_am) * (m_ab_p - len_bm) * (m_ab_p - len_ab))
    m_bc_p = (len_bm + len_cm + len_bc) / 2  # Полупериметр треугольника BCM
    len_m_bc = 2 / len_bc * sqrt(m_bc_p * (m_bc_p - len_bm) * (m_bc_p - len_cm) * (m_bc_p - len_bc))
    m_ac_p = (len_am + len_cm + len_ac) / 2  # Полупериметр треугольника ACM
    len_m_ac = 2 / len_ac * sqrt(m_ac_p * (m_ac_p - len_am) * (m_ac_p - len_cm) * (m_ac_p - len_ac))

    # Вывод ответа на 4 пункт
    print("Точка M лежит внутри треугольника\n"
          f"Расстояние до ближайшей стороны треугольника: {format(min(len_m_ab, len_m_bc, len_m_ac), '.5g')}")
else:
    # Вывод ответа на 4 пункт
    print("Точка M не лежит внутри треугольника")
