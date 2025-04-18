#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для обработки пользовательского ввода.
"""


def get_equation_coefficients():
    """
    Получает от пользователя коэффициенты квадратного уравнения.
    
    Returns:
        tuple: Кортеж из трех float значений (a, b, c).
        
    Raises:
        ValueError: Если пользователь ввел некорректные данные.
    """
    print("Введите коэффициенты квадратного уравнения ax² + bx + c = 0:")
    
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        return a, b, c
    except ValueError:
        raise ValueError("Коэффициенты должны быть числами")


def get_coefficients_from_string(equation_str):
    """
    Извлекает коэффициенты из строкового представления уравнения.
    Поддерживает форматы вида: "ax² + bx + c = 0" или "a*x^2 + b*x + c = 0"
    
    Args:
        equation_str (str): Строковое представление уравнения.
        
    Returns:
        tuple: Кортеж из трех float значений (a, b, c).
        
    Raises:
        ValueError: Если строка имеет неправильный формат.
    """
    # Эта функция реализована частично и может быть расширена в будущем
    # для поддержки различных форматов ввода уравнения
    try:
        # Простой вариант: предполагаем, что пользователь ввел три числа через пробел
        parts = equation_str.strip().split()
        if len(parts) == 3:
            return float(parts[0]), float(parts[1]), float(parts[2])
        else:
            raise ValueError("Неправильный формат уравнения")
    except:
        raise ValueError("Не удалось разобрать уравнение. Введите коэффициенты отдельно.") 