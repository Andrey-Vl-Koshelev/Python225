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
