#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    m = int(input("Enter the month number: "))

    if 1 <= m <= 12:
        if m <= 6:
            print("First Half - year")
        else:
            print("Second Half - year")

        if m == 2:
            print("Number of days: 28")
        elif m == 4 or m == 6 or m == 9 or m == 11:
            print("Number of days: 30")
        else:
            print("Number of days: 31")

    else:
        print("Wrong month number.")