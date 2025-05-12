import pytest
import math
from algorithms.leibniz import calculate_leibniz
from algorithms.monte_carlo import calculate_monte_carlo

def test_leibniz():
    """测试莱布尼茨方法的精确度"""
    pi = calculate_leibniz(terms=1000000)
    assert abs(pi - math.pi) < 0.001

def test_monte_carlo():
    """测试蒙特卡罗方法的精确度"""
    pi = calculate_monte_carlo(num_samples=1000000)
    assert abs(pi - math.pi) < 0.01

def test_leibniz_convergence():
    """测试莱布尼茨方法的收敛性"""
    pi1 = calculate_leibniz(terms=1000)
    pi2 = calculate_leibniz(terms=10000)
    assert abs(pi2 - math.pi) < abs(pi1 - math.pi)

def test_monte_carlo_consistency():
    """测试蒙特卡罗方法的一致性"""
    results = [calculate_monte_carlo(num_samples=100000) for _ in range(5)]
    max_diff = max(abs(x - y) for x in results for y in results)
    assert max_diff < 0.1
