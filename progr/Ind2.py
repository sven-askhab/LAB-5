#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a1 = float(input("Введите коэффициент a1: "))
    b1 = float(input("Введите коэффициент b1: "))
    c1 = float(input("Введите коэффициент c1: "))

    a2 = float(input("Введите коэффициент a2: "))
    b2 = float(input("Введите коэффициент b2: "))
    c2 = float(input("Введите коэффициент c2: "))

    d = a1 * b2 - a2 * b1
    Dx = -c1 * b2 + c2 * b1
    Dy = -a1 * c2 + a2 * c1

    if d != 0:
        x = Dx / d
        y = Dy / d
        print(f"Прямые пересекаются в точке с координатами ({x}, {y})")
    elif Dx == Dy == 0:
        print("Прямые совпадают")
    else:
        print("Прямые параллельны")