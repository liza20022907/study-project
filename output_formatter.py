#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для форматирования вывода результатов.
"""


def format_result(a, b, c, solution):
    """
    Форматирует результат решения уравнения.
    
    Args:
        a (float): Коэффициент при x².
        b (float): Коэффициент при x.
        c (float): Свободный член.
        solution (dict): Словарь с информацией о решении.
        
    Returns:
        str: Отформатированный результат.
    """
    equation_str = format_equation(a, b, c)
    result_str = f"Решение уравнения {equation_str}:\n"
    
    solution_type = solution['type']
    roots = solution['roots']
    discriminant = solution.get('discriminant')
    
    if discriminant is not None:
        result_str += f"Дискриминант: {discriminant}\n"
    
    if solution_type == 'two_real':
        result_str += f"Два действительных корня:\n"
        result_str += f"x₁ = {roots[0]}\n"
        result_str += f"x₂ = {roots[1]}"
    elif solution_type == 'one_real':
        result_str += f"Один действительный корень:\n"
        result_str += f"x = {roots[0]}"
    elif solution_type == 'two_complex':
        result_str += f"Два комплексных корня:\n"
        result_str += f"x₁ = {format_complex(roots[0])}\n"
        result_str += f"x₂ = {format_complex(roots[1])}"
    elif solution_type == 'linear':
        result_str += f"Уравнение линейное:\n"
        result_str += f"x = {roots[0]}"
    elif solution_type == 'identity':
        result_str += f"Любое значение x является решением"
    elif solution_type == 'no_roots':
        result_str += f"Нет решений"
    
    return result_str


def format_complex(complex_number):
    """
    Форматирует комплексное число в удобочитаемый вид.
    
    Args:
        complex_number (complex): Комплексное число.
        
    Returns:
        str: Отформатированное комплексное число.
    """
    real = complex_number.real
    imag = complex_number.imag
    
    if imag >= 0:
        return f"{real} + {imag}i"
    else:
        return f"{real} - {abs(imag)}i"


def format_equation(a, b, c):
    """
    Форматирует уравнение в стандартном виде.
    
    Args:
        a (float): Коэффициент при x².
        b (float): Коэффициент при x.
        c (float): Свободный член.
        
    Returns:
        str: Отформатированное уравнение.
    """
    terms = []
    
    # Добавление члена с x²
    if a != 0:
        if a == 1:
            terms.append("x²")
        elif a == -1:
            terms.append("-x²")
        else:
            terms.append(f"{a}x²")
    
    # Добавление члена с x
    if b != 0:
        if b > 0:
            if terms:  # Если уже есть первый член, добавляем знак "+"
                if b == 1:
                    terms.append("+ x")
                else:
                    terms.append(f"+ {b}x")
            else:  # Если это первый член, не добавляем знак "+"
                if b == 1:
                    terms.append("x")
                else:
                    terms.append(f"{b}x")
        else:  # b < 0
            if b == -1:
                terms.append("- x")
            else:
                terms.append(f"- {abs(b)}x")
    
    # Добавление свободного члена
    if c != 0:
        if c > 0:
            if terms:  # Если уже есть члены, добавляем знак "+"
                terms.append(f"+ {c}")
            else:  # Если это первый член, не добавляем знак "+"
                terms.append(f"{c}")
        else:  # c < 0
            terms.append(f"- {abs(c)}")
    
    # Если нет членов, значит все коэффициенты равны 0
    if not terms:
        return "0 = 0"
    
    # Возвращаем собранное уравнение
    return " ".join(terms) + " = 0" 