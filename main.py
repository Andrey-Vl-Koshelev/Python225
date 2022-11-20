# import main
from car import electrocar

# def main():
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()

# from math import pi
#
#
# class Rectangle:
#     def __init__(self, l, h):
#         self.l = l
#         self.h = h
#
#     def get_rect_perimetr(self):
#         res = self.l * 2 + self.h * 2
#         print(f"Периметр прямоугольника: {res}")
#         return res
#
#     def get_rect_area(self):
#         res = self.l * self.h
#         print(f"Площадь прямоугольника: {res}")
#         return res
#
#     def print_rect(self):
#         print(f"Стороны прямоугольника: {self.l}, {self.h}")
#         return {self.l, self.h}
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_circle_circumference(self):
#         res = 2 * pi * self.r
#         print(f"Длина окружности: {round(res, 2)}")
#         return res
#
#     def get_circle_area(self):
#         res = round(pi * self.r ** 2, 2)
#         print(f"Площадь круга: {res}")
#         return res
#
#     def print_circle(self):
#         print(f"Радиус круга: {self.r}")
#         return self.r
#
#
# class Cylinder(Rectangle, Circle):
#     def __init__(self, r, h):
#         Circle.__init__(self, r)
#         Rectangle.__init__(self, self.get_circle_circumference(), h)
#
#     def get_volume(self):
#         res = self.get_circle_area() * self.h
#         print(f"Объем: {res}")
#         return res
#
#     def print_cylinder(self):
#         print(f"Радиус основания: {self.r}, высота: {self.h}")
#
#
# circles = [Circle(4), Circle(2), Circle(6), Circle(8), Circle(1)]
# rects = [Rectangle(3, 7), Rectangle(2, 7), Rectangle(19, 12)]
# cylinders = [Cylinder(4, 7), Cylinder(2, 5), Cylinder(9, 3), Cylinder(5, 5)]
#
# circle_max_s = max(circles, key=lambda c: c.get_circle_area())
# rect_min_p = min(rects, key=lambda r: r.get_rect_perimetr())
# cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
# cylinder_v_avr = sum(cylinders_v) / len(cylinders_v)
# print(f"Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {circle_max_s.get_circle_area()}")
# print(f'Прямоугольник с наименьшим периметром: {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimetr()}')
# print(f"Средний объем цилиндров: {round(cylinder_v_avr, 2)}")

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Robot:
# #     k = 0
# #
# #     def __init__(self, name):
# #         self.name = name
# #         print('Инициализация робота: ', self.name)
# #         Robot.k += 1
# #
# #     def __del__(self):
# #         print(self.name, 'выключается')
# #         Robot.k -= 1
# #         if Robot.k == 0:
# #             print(self.name, 'был последним')
# #         else:
# #             print('Работающих роботов осталось:', Robot.k)
# #
# #     def say_hi(self):
# #         print('Приветствую! Меня зовут:', self.name)
# #
# # droid1 = Robot('R2_D2')
# # droid1.say_hi()
# # print('Численность роботов:', Robot.k)
# #
# # droid2 = Robot('C-3PO')
# # droid2.say_hi()
# # print('Численность роботов:', Robot.k)
# # print('\nЗдесь роботы делают работу\n')
# # print('Роботы закончили работу')
# # del droid1
# # del droid2
# # print('Численность роботов:', Robot.k)


# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = 'Некоректные данные'
#         self.__year = self.__power = self.__price = 0
#         if Car.__check_value_str(name):
#             self.__name = name
#         if Car.__check_value_int(year):
#             self.__year = year
#         if Car.__check_value_str(model):
#             self.__model =model
#         if Car.__check_value_int(power):
#             self.__power = power
#         if Car.__check_value_str(color):
#             self.__color = color
#         if Car.__check_value_int(price):
#             self.__price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print('Данные должны быть числом')
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print('Данные должны быть строкой')
#             return False
#         return True
#
#     def set_name(self, name):
#         if Car.__check_value_str(name):
#             self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#
#     def print_info(self):
#         print('Данные автомобиля'.center(40,'*'))
#         print(f"""Название модели: {self.__name}
# Год выпуска: {self.__year}
# Производитель: {self.__model}
# Мощность двигателя: {self.__power}
# Цвет машины: {self.__color}
# Цена: {self.__price}
# """)
#         print('='*40)
#
#
#
# c1 = Car('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
# c1.print_info()
# c1.set_name('X2')
# print(c1.get_name())
# c1.print_info()


# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, m):
#         self.__age = m
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
#
#
# p1 = Person('Irina', 26)
# print(p1.name)
# p1.name = 'Igor'
# del p1.name
# p1.age = 20
# print(p1.age)
# del p1.age
# print(p1.__dict__)


# class Numbers:
#
#     @staticmethod
#     def min_nums(a, b, d, c):
#         min_num = min(a, b, d, c)
#         return min_num
#
#     @staticmethod
#     def max_nums(a, b, d, c):
#         max_num = max(a, b, d, c)
#         return max_num
#
#     @staticmethod
#     def sr_arif(a, b, d, c):
#         arif = (a + b + d + c) / 4
#         return arif
#
#     @staticmethod
#     def factor(a):
#         n = 1
#         for i in range(1, (a + 1)):
#             n = n * i
#         return n
#
#
#
# print('Минимальное число:', Numbers.min_nums(4, 5, 9, 2))
# print('Максимальное число:', Numbers.max_nums(4, 5, 9, 2))
# print('Среднее арифметическое:', Numbers.sr_arif(4, 5, 9, 2))
# print('Факториал числа:', Numbers.factor(9))


# class Weight:
#
#     def __init__(self, k=0):
#         self.__k = k
#
#     @property
#     def kg_k(self):
#         return self.__k
#
#     @kg_k.setter
#     def kg_k(self, k):
#         if isinstance(k, int | float):
#             self.__k = k
#         else:
#             print('Килограммы задаются числами')
#
#     def to_pounds(self):
#         return round(self.__k * 2.205, 2)
#
# w1 = Weight(12)
# print(w1.kg_k, 'кг =>', end='')
# print(w1.to_pounds(), 'фунтов')
# w1.kg_k = 41.5
# print(w1.kg_k, 'кг =>', end='')
# print(w1.to_pounds(), 'фунтов')


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежит {self.surname} был открыт. ')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт. ')
#
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd )
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur )
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете.')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено')
#         self.print_balance()
#
#
#
#
# ass = Account('12345', 'Долгих', 0.03, 1000)
# ass.print_info()
# ass.convert_to_usd()
# ass.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# ass.convert_to_usd()
# Account.set_eur_rate(3)
# ass.convert_to_eur()
# print()
# ass.edit_owner('Дюма')
# ass.print_info()
# print()
# ass.add_percents()
# print()
# ass.withdraw_money(3000)
# print()
# ass.withdraw_money(100)
# print()
# ass.add_money(5000)
# print()
# ass.withdraw_money(3000)
# print()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         print(f'Площадь {self.color} прямоугольника: ', end='')
#         return self.__width * self.__height
#
# rect = Rectangle(10, 20, 'green')
# # rect.width = 5
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect.color)
# print(rect.area())


# import math
# #
# #
# # class Table:
# #     def __init__(self, width=None, length=None, radius=None):
# #         if radius is None:
# #             self._width = width
# #             self._length = length
# #         else:
# #             self._radius = radius
# #
# #     def calc_area(self):
# #         raise NotImplementedError('В дочернем классе должен быть определен метод calc_area')
# #
# #
# # class SqTable(Table):
# #     def calc_area(self):
# #         return self._width * self._length
# #
# #
# # class RoundTable(Table):
# #     def calc_area(self):
# #         return round(math.pi * self._radius ** 2, 2)
# #
# #
# # t = SqTable(20, 10)
# # print(t.__dict__)
# # print(t.calc_area())
# # t2 = RoundTable(radius=20)
# # print(t2.__dict__)
# # print(t2.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print('*' * 30)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print('*' * 30)


# class Liguid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density
#
#     def edit_density(self, val):
#         self.density = val
#
#     def calc_v(self, m):
#         v = m / self.density
#         print(f'Объем {m} кг {self.name} равен {v} m^3')
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f'Вес {v} m^3 of {self.name} составляет {m} кг.')
#
#     def print_info(self):
#         print(f'Жидкость "{self.name}" (плотность = {self.density}kg/m^3).')
#
#
# class Alcohol(Liguid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
# a.edit_density(1000)
# a.print_info()
# a.calc_v(300)
# a.calc_m(0.5)
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def set_name_notebook(self):
#         print(f'{self.name} => ', end=' ')
#         self.note.set_notebook_all()
#
#     class Notebook:
#         def __init__(self):
#             self.model = 'HP'
#             self.processor = 'i7'
#             self.memory = 16
#
#         def set_notebook_all(self):
#             print(f'{self.model}, {self.processor}, {self.memory}')
#
#
# s1 = Student('Roman')
# s2 = Student('Vova')
# s1.set_name_notebook()
# s2.set_name_notebook()


# class Point3D:
#     CH = 'Координата должна быть числом'
#     RIGHT = 'Правый операнд должен быть типом Point3D'
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'{self.__x}, {self.__y}, {self.__z}'
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int | float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     @staticmethod
#     def __check0(v):
#         if v.x == 0 or v.y == 0 or v.z == 0:
#             raise ZeroDivisionError('Ни одна из координат не должна быть нулем')
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print('Неверно задан ключ')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('Ключ должен быть строкой')
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print('Координаты должны быть числами')
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print('Координаты первой точки: ', pt1)
# print('Координаты второй точки: ', pt2)
#
# pt3 = pt1 + pt2
# print(f'Сложение координат: ({pt3})')
#
# pt4 = pt1 - pt2
# print(f'Разность координат: ({pt4})')
#
# pt5 = pt1 * pt2
# print(f'Умножение: ({pt5})')
#
# pt6 = pt1 / pt2
# print(f'Деление: ({pt6})')
#
# pt7 = pt1 == pt2
# print(f'Равенство координат: {pt7}')
#
# print('x=', pt1['x'], 'x1=', pt2['x'])
# print('y=', pt1['y'], 'y1=', pt2['y'])
# print('z=', pt1['z'], 'z1=', pt2['z'])
#
# pt1['x'] = 20
# print('Запись значения в координату x: ', pt1['x'])

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age} года.'
#
#     def make_sound(self):
#         return f'{self.name} мяукает.'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст {self.age} года.'
#
#     def make_sound(self):
#         return f'{self.name} гавкает.'
#
#
# c = Cat('Пушок', 2.5)
# # print(c.info())
# d = Dog('Мухтар', 4)
# # print(d.info())
# # shape = [c, d]
# for g in [c, d]:
#     print(g.info(),'\n',g.make_sound())


# class Human:
#     def __init__(self, lastname, name, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.lastname} {self.name} {self.age}', end=' ')
#
#
# class Student(Human):
#     def __init__(self, lastname, name, age, direction, group, rating):
#         super().__init__(lastname, name, age)
#         self.direction = direction
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.direction} {self.group} {self.rating}', end=' ')
#
#
# class Teacher(Human):
#     def __init__(self, lastname, name, age, spec, exp):
#         super().__init__(lastname, name, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#         super().info()
#         print(f'{self.spec} {self.exp}', end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, lastname, name, age, direction, group, rating, theme):
#         super().__init__(lastname, name, age, direction, group, rating)
#         self.theme = theme
#
#     def info(self):
#         super().info()
#         print(f'{self.theme}', end=' ')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#         return res ** 2
#
#
# @Power
# def func1(a, b):
#     return a * b
#
#
# n = func1(2, 3)
# print(n)


# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.name
#         return wrap
#
#
# @Power(2)
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 3))
# import json
#
# data = {
#     "first_name": "Jane",
#     "last_name": "Doe",
#     "hobbies": ("running", "sky diving", "singing"),
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Alice",
#             "age": 6
#         },
#         {
#             "first_name": "Bob",
#             "age": 8
#         },
#     ]
# }
# with open("data_file.json", "w") as fw:
#     json.dump(data, fw,indent=4)
#
# with open("data_file.json", "r") as fw:
#     data = json.load(fw)
#     print(data)
# json_string = json.dumps(data, sort_keys=False)
# print(json_string )
#
# data = json.loads(json_string )
# print(data)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#     key = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     while len(key) != 10:
#         key += choice(nums)
#     # print(key)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, key
#
#
# def write_json(person_dict, key):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#     data[key] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for _ in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ', '
#         return f'Студент: {self.name} {a[:-2]}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + '\n'
#         return f'Группа: {self.group}\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_group(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bond', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikola', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]

# Student.load_from_file('student.json')
# Student.dump_to_json(st1, 'student.json')
# Student.dump_to_json(st3, 'student.json')

# my_group = Group(sts, 'ГК Python')
# print(my_group)
# Group.dump_group('group.json', my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st3]
# my_group2 = Group(group22, 'ГК Web')
# print(my_group2)
# Group.dump_group('group.json', my_group2)
# Group.upload_group(('group.json'))
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)


# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.edit_mark(2, 4)
# print(st1)
# print(st1.average_mark())

# import json
#
#
# class Country:
#
#     def __init__(self, num):
#         self.data = {}
#         self.num = num
#
#     def __str__(self):
#         return f'{self.num}'
#
#     def pin_country(self):
#         if self.num == 5:
#             with open('country.json', 'r') as f:
#                 return json.load(f)
#
#
#     def add_country(self):
#         if self.num == 1:
#             try:
#                 self.data = json.load(open('country.json'))
#             except FileNotFoundError:
#                 self.data = {}
#             country = input('Введите название страны: ')
#             capital = input('Введите название столицы страны: ')
#             self.data[country] = capital
#             with open('country.json', 'w') as f:
#                 json.dump(self.data, f, indent=2)
#                 print('Файл сохранен')
#
#     def removal_country(self):
#         if self.num == 2:
#             try:
#                 self.data = json.load(open('country.json'))
#             except FileNotFoundError:
#                 self.data = {}
#             country = input('Введите название страны для удаления: ')
#             self.data.pop(country)
#             with open('country.json', 'w') as f:
#                 json.dump(self.data, f, indent=2)
#                 print('Файл сохранен')
#
#     def scan_country(self):
#         if self.num == 3:
#             self.data = json.load(open('country.json'))
#             country = input('Введите название страны для поиска столицы: ')
#             n = self.data[country]
#             return f'Столица - {n}'
#
#     def changes_country(self):
#         if self.num == 4:
#             try:
#                 self.data = json.load(open('country.json'))
#             except FileNotFoundError:
#                 self.data = {}
#             country = input('Введите название страны столицу которой хотите изменить: ')
#             capital = input('Введите новое название столицы: ')
#             self.data[country] = capital
#
#             with open('country.json', 'w') as f:
#                 json.dump(self.data, f, indent=2)
#                 m = self.data.get(country)
#                 return f'Уточненное название столицы - {m}'
#
#     def end_of(self):
#         if self.num == 6:
#             return f'Завершение работы.'
#
#     @classmethod
#     def main(cls):
#
#         while True:
#             print('*' * 40)
#             print(
#                 f'Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                 f'3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                 f'6 - завершение работы'
#             )
#             num = int(input('Ввод: '))
#             if num == 5:
#                 print(Country(5).pin_country())
#             elif num == 1:
#                 print(Country(1).add_country())
#
#             elif num == 2:
#                 print(Country(2).removal_country())
#
#             elif num == 3:
#                 print(Country(3).scan_country())
#
#             elif num == 4:
#                 print(Country(4).changes_country())
#             else:
#                 print(Country(6).end_of())
#                 print('*' * 40)
#                 break
#
#
# Country.main()

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
#
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# month = int(input('Введите номер месяца: '))
# if 1 <= month <= 2 or month == 12:
#     print('Зима')
# elif 3 <= month <= 5:
#     print('Весна')
# elif 6 <= month <= 8:
#     print('Лето')
# elif 9 <= month <= 11:
#     print('Осень')
# else:
#     print('Нет такого месяца')

# n = int(input('Введите число от 1 до 99: '))
# if 0 <= n <= 99:
#     if 11 <= n <= 14:
#         print(f'{n} копеек')
#     elif n % 10 == 1:
#         print(f'{n} копейка')
#     elif 2 <= n % 10 <= 4:
#         print(f'{n} копейки')
#     else:
#         print(f'{n} копеек')
# else:
#     print('Не верный диапазон')

# n = input('Ведите число цифрой или прописью: ')
# m = input('Ведите число цифрой или прописью: ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# print('*' * 7)

# n = int(input('Ведите начало диапазона: '))
# m = int(input('Ведите конец диапазона: '))
#
# i = n
# res = 0
# while i <= m:
#     if i % 2:
#         res += i
#     i += 1
# print(f'Сумма целых нечетных чисел: {res}')

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print('Результат: ', res)

# res = ''
# while True:
#
#     print('Выберете операцию:')
#     print(f'1 - "g" - выход\n2 - "+" - сложение\n3 - "-" - вычитание\n'
#           f'4 - "/" - деление\n5 - "*" - умножение\n6 - "%" - деление по модулю')
#     n = int(input('Введите цифру: '))
#
#     if n == 1:
#         break
#     m = int(input('Введите первое число: '))
#     s = int(input('Введите второе число: '))
#     if s == 0:
#         print('На 0 делить нельзя')
#     elif n == 2:
#         res = m + s
#         print(res)
#     elif n == 3:
#         res = m - s
#         print(res)
#     elif n == 4:
#         res = m / s
#         print(res)
#     elif n == 5:
#         res = m * s
#         print(res)
#     elif n == 6:
#         res = m % s
#         print(res)

# n = int(input('Количество символов: '))
# m = input('Тип символа: ')
# print(f'0 - горизонтальная\n1 - вертикальная')
# s = int(input('Ориентация линии:'))
# i = 0
# while i < n:
#     if s == 0:
#         print(m, end=' ')
#     elif s == 1:
#         print(m )
#     else:
#         print('Такой ориентации не предусмотрено.')
#         break
#     i += 1

# n = int(input('Введите количество чисел последовательности: '))
# i = 1
# num = float(input('Введите число: '))
# res = 0
# minim = num
# maxim = num
# while i < n:
#     num = float(input('Введите число: '))
#     res += num / n
#     if maxim < n:
#         maxim = n
#     if minim > n:
#         minim = n
#     i += 1
# print('Количество чисел', n)
# print('Среднее арифметическое:', res)
# print('Минимальное число равно:', minim)
# print('Максимальное число равно:', maxim)

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 15:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# n = int(input('Введите целое число: '))
# for i in range(1, n):
#     if n % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=' ')

# n = int(input('Введите длину прямоугольника: '))
# m = int(input('Введите высоту прямоугольника: '))
# for i in range(m + 1):
#     for j in range(n + 1):
#         print('*', end=' ')
#     print()

# n = int(input('Введите длину прямоугольника: '))
# m = int(input('Введите высоту прямоугольника: '))
# for i in range(m):
#     for j in range(n):
#         if i == 0 or i == m - 1 or j == 0 or j == n - 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# n = 5
# for i in range(1, n + 1):
#     print(i ** 2, end=' ')

# генератор ввода кода
# print([int(input('-> ')) for i in range(int(input('n = ')))])

# n = 4
# sum = 0
# for i in range(4):
#     a = int(input('-> '))
#     if a < 0:
#         sum += a
# print(sum)

# sum = 0
# cal = 0
# for i in range(20):
#     if i % 2 == 0:
#         cal += 1
#     else:
#         sum += i
# print('Количество четных элементов: ', cal)
# print('Сумма  нечетных: ', sum)

# s = 0
# k = 0
# n = [6, 3, 0, 8, 2]
# for i in n:
#     if i > 0:
#         s += i
#         k += 1
# print('Среднее арифметическое:', s / k)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# n = int(input('Количество элементов списка: '))
# m = []
# for i in range(n):
#     s = int(input('Введите число кратное 3: '))
#     if s % 3 == 0:
#         m.append(s)
#     else:
#         print(f'{s} не делится на 3 без остатка.')
# print(m)

# n = [1, 2, 3]
# m = [11, 22, 33, 5, 6]
# c = []
# i = 0
# while i < len(m):
#     if i < len(n):
#         c.append(n[i])
#         c.append(m[i])
#     else:
#         c.append(m[i])
#     i += 1
# print(c)

# m = [11, 22, 33, 5, 6]
# del m[2]
# print(m)

# n = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m = []
# for i in n:
#     if n.count(i) == 1:
#         m.append(i)
# print(m)


# import requests
# import json

# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_users = ' and '.join(users)
# s = 's' if len(users) > 1 else ''
# print(f'user{s} {max_users} completed {max_complete} TODOs')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_file.json', 'w') as data_file:
#     filtered_todos = list(filter(keep, todos))
#     # print(filtered_todos)
#     json.dump(filtered_todos, data_file, indent=2)
# with open('filtered_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

import csv

# with open('data.csv') as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
# count = 0
# for row in file_reader:
#     print(row)
#     if count == 0:
#         print(f"Файл содержит столбцы: {', '.join(row)}")
#     else:
#         print(f'   {row[0]} - {row[2]}. Родился в {row[2]} году.')
#     count += 1
# print(f'Всего в файле {count} строки.')
# with open('data.csv') as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f'{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году')
#         # count += 1
# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '10'])
#     writer.writerow(['Петя', '8', '11'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=',', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
# with open('data_new.csv', 'r') as f:
#     print(f.read())

# with open('student1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow(({'Имя': 'Саша', 'Возраст': '7'}))

# data = [{
# #     'hostname': 'sw1',
# #     'location': 'London',
# #     'model': '3750',
# #     'vendor': 'Cisco'
# # }, {
# #     'hostname': 'sw2',
# #     'location': 'Liverpool',
# #     'model': '3850',
# #     'vendor': 'Cisco'
# # }, {
# #     'hostname': 'sw3',
# #     'location': 'Liverpool',
# #     'model': '3650',
# #     'vendor': 'Cisco'
# # }, {
# #     'hostname': 'sw4',
# #     'location': 'London',
# #     'model': '3650',
# #     'vendor': 'Cisco'
# # }]
# #
# # with open('dictwriter.csv', 'w') as f:
# #     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
# #     writer.writeheader()
# #     for d in data:
# #         writer.writerow(d)

# import requests
# import csv
#
# with open('DZ/data2.csv', 'r') as f:
#     print(f.read())

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find('div', class_='name').text
# row = soup.find_all('div', class_='name')
# row = soup.find_all('div', {'class':'name'})
# row = soup.find('div', {'data-set':'salary'})
# row = soup.find('div', text='Alena').parent
# row = soup.find('div', text='Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)
# import re
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_salary(i.text)

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv


# reg = requests.get('https://ru.wordpress.org/')
# # print(reg.headers['Content-Type'])
# # reg.encoding = 'utf-8'
# print(reg.text)


# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title')
#     return p1
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[1]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         # url = plugin.find('h3').find('a')['href']
#         url = plugin.find('h3').find('a').get('href')
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#         # print(data)
#
#         # print(rating)
#     # return len(plugins)
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def write_csv(name):
#     with open('DZ/built_in.csv', 'w', encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter=",", lineterminator='\r', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(name)
#
#
# name = []
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     s1 = soup.find_all('div', class_='page__content')[0]
#     plugins = s1.find_all('h3')
#     for plugin in plugins:
#         data = plugin.find('a').get('name')
#         name.append(data)
#         write_csv(name)
#
#
# def main():
#     url = 'https://letpy.com/handbook/builtins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
