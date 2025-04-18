#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для решения квадратных уравнений.
"""

import math
import cmath
from utils import is_close_to_zero


def solve_quadratic_equation(a, b, c):
    """
    Решает квадратное уравнение вида ax² + bx + c = 0.
    
    Args:
        a (float): Коэффициент при x².
        b (float): Коэффициент при x.
        c (float): Свободный член.
        
    Returns:
        dict: Словарь с информацией о решении:
            - 'type': Тип решения ('two_real', 'one_real', 'two_complex', 'linear', 'no_roots')
            - 'roots': Список корней уравнения
            - 'discriminant': Значение дискриминанта
    """
    if is_close_to_zero(a):
        # Если a ≈ 0, уравнение становится линейным
        return solve_linear_equation(b, c)
    
    # Вычисление дискриминанта
    discriminant = b**2 - 4*a*c
    
    # Определение типа решения на основе дискриминанта
    if discriminant > 0:
        # Два действительных корня
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return {
            'type': 'two_real',
            'roots': [root1, root2],
            'discriminant': discriminant
        }
    elif is_close_to_zero(discriminant):
        # Один действительный корень (дискриминант ≈ 0)
        root = -b / (2*a)
        return {
            'type': 'one_real',
            'roots': [root],
            'discriminant': discriminant
        }
    else:
        # Два комплексных корня
        sqrt_discriminant = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return {
            'type': 'two_complex',
            'roots': [root1, root2],
            'discriminant': discriminant
        }


def solve_linear_equation(b, c):
    """
    Решает линейное уравнение вида bx + c = 0.
    
    Args:
        b (float): Коэффициент при x.
        c (float): Свободный член.
        
    Returns:
        dict: Словарь с информацией о решении.
    """
    if is_close_to_zero(b):
        # Если b ≈ 0, то уравнение превращается в c = 0
        if is_close_to_zero(c):
            # c ≈ 0, то любое x - решение
            return {
                'type': 'identity',
                'roots': ['x ∈ ℝ'],  # Любое действительное число
                'discriminant': None
            }
        else:
            # c ≠ 0, нет решений
            return {
                'type': 'no_roots',
                'roots': [],
                'discriminant': None
            }
    else:
        # Обычное линейное уравнение
        root = -c / b
        return {
            'type': 'linear',
            'roots': [root],
            'discriminant': None
        } 