# from car import electrocar
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
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






