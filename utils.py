#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль с вспомогательными функциями.
"""

import math


def is_close_to_zero(value, epsilon=1e-10):
    """
    Проверяет, является ли значение близким к нулю.
    
    Args:
        value (float): Проверяемое значение.
        epsilon (float, optional): Допустимое отклонение. По умолчанию 1e-10.
        
    Returns:
        bool: True, если значение можно считать равным нулю, иначе False.
    """
    return abs(value) < epsilon


def round_if_close_to_int(value, epsilon=1e-10):
    """
    Округляет значение до целого числа, если оно близко к целому.
    
    Args:
        value (float): Проверяемое значение.
        epsilon (float, optional): Допустимое отклонение. По умолчанию 1e-10.
        
    Returns:
        float: Округленное значение, если оно близко к целому, или исходное значение.
    """
    rounded = round(value)
    if abs(value - rounded) < epsilon:
        return rounded
    return value 