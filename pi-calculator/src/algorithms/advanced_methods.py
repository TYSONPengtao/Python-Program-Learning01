"""
高级π值计算算法模块
包含多种计算π值的方法：
1. Nilakantha级数
2. Gauss-Legendre算法
3. Chudnovsky算法
"""
import numpy as np
from decimal import Decimal, getcontext
from typing import Union, Tuple

def calculate_nilakantha(terms: int = 1000) -> float:
    """
    使用Nilakantha级数计算π值
    π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    
    Args:
        terms: 计算项数
    
    Returns:
        float: 计算得到的π值
    """
    result = Decimal(3.0)
    sign = 1
    
    for i in range(2, 2*terms + 1, 2):
        term = Decimal(4) / (Decimal(i) * Decimal(i+1) * Decimal(i+2))
        result += sign * term
        sign = -sign
    
    return float(result)

def calculate_gauss_legendre(iterations: int = 10) -> float:
    """
    使用Gauss-Legendre算法计算π值
    
    Args:
        iterations: 迭代次数
    
    Returns:
        float: 计算得到的π值
    """
    a = 1.0
    b = 1.0 / np.sqrt(2)
    t = 0.25
    p = 1.0
    
    for _ in range(iterations):
        a_next = (a + b) / 2
        b = np.sqrt(a * b)
        t = t - p * (a - a_next) ** 2
        a = a_next
        p *= 2
    
    return (a + b) ** 2 / (4 * t)

def calculate_chudnovsky(precision: int = 50) -> Decimal:
    """
    使用Chudnovsky算法计算π值
    该算法用于计算高精度的π值
    
    Args:
        precision: 所需的小数位数
    
    Returns:
        Decimal: 计算得到的π值
    """
    getcontext().prec = precision
    C = 426880 * Decimal(10005).sqrt()
    L = 13591409
    X = 1
    M = 1
    K = 6
    S = L
    for i in range(1, precision):
        M = M * (K ** 3 - 16 * K) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    return pi

def estimate_error(computed_pi: Union[float, Decimal], method: str) -> float:
    """
    估算计算结果的误差
    
    Args:
        computed_pi: 计算得到的π值
        method: 计算方法名称
    
    Returns:
        float: 相对误差
    """
    if isinstance(computed_pi, Decimal):
        computed_pi = float(computed_pi)
    return abs(computed_pi - np.pi) / np.pi
