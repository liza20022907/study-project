#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Главный модуль программы для решения квадратных уравнений.
"""

from input_handler import get_equation_coefficients
from equation_solver import solve_quadratic_equation
from output_formatter import format_result


def main():
    """
    Основная функция программы.
    """
    print("Программа для решения квадратных уравнений ax² + bx + c = 0")
    
    try:
        a, b, c = get_equation_coefficients()
        roots = solve_quadratic_equation(a, b, c)
        formatted_result = format_result(a, b, c, roots)
        print(formatted_result)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main() 