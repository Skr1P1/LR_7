#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Используя замыкания функций, объявите внутреннюю функцию, которая принимает в
#качестве аргумента коллекцию (список или кортеж) и возвращает или минимальное
#значение, или максимальное, в зависимости от значения параметра type внешней
#функции. Если type равен «max», то возвращается максимальное значение, иначе –
#минимальное. По умолчанию type должно принимать значение «max». Вызовите
#внутреннюю функцию замыкания и отобразите на экране результат ее работы.


def func_1(type_='max'):
    def func_2(lst):
        return eval(f'{type_}(lst)')

    return func_2
 
 
a = [1, 2, 3, 4, 5, 65, 6,]
 
max_func = func_1()
min_func = func_1('min')


if __name__ == "__main__":
    print(max_func(a))
    print(min_func(a))
    