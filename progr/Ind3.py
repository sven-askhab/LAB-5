#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    
    number = 100
    digit_sum = 0
    
    while number < 1000:
        n = number
        if number % 7 == 0:
            while n > 0:
                digit_sum += n % 10
                n = n // 10
            if digit_sum % 7 == 0:
                print(number)
        number += 1
        digit_sum = 0