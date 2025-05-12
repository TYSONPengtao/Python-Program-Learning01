import pytest
import math
import numpy as np
from decimal import Decimal
from algorithms.leibniz import calculate_leibniz
from algorithms.monte_carlo import calculate_monte_carlo
from algorithms.advanced_methods import (
    calculate_nilakantha,
    calculate_gauss_legendre,
    calculate_chudnovsky,
    estimate_error
)
from algorithms.visualization import create_monte_carlo_animation

def test_leibniz_accuracy():
    """测试莱布尼茨方法的精度"""
    pi = calculate_leibniz(1_000_000)
    assert abs(pi - np.pi) < 0.001

def test_monte_carlo_accuracy():
    """测试蒙特卡罗方法的精度"""
    # 使用固定的随机种子以保证可重复性
    np.random.seed(42)
    pi = calculate_monte_carlo(1_000_000)
    assert abs(pi - np.pi) < 0.01

def test_monte_carlo_convergence():
    """测试蒙特卡罗方法的收敛性"""
    np.random.seed(42)
    results = []
    for _ in range(5):
        pi = calculate_monte_carlo(100_000)
        results.append(pi)
    # 检查结果的标准差是否在合理范围内
    assert np.std(results) < 0.01

def test_visualization_creation():
    """测试可视化创建功能"""
    ani = create_monte_carlo_animation(num_points=100, frames=10)
    assert ani is not None

@pytest.mark.parametrize("n_terms", [100, 1000, 10000])
def test_leibniz_convergence(n_terms):
    """测试莱布尼茨方法在不同项数下的收敛性"""
    pi = calculate_leibniz(n_terms)
    # 误差应该随着项数增加而减小
    expected_error = 1.0 / n_terms
    actual_error = abs(pi - np.pi)
    assert actual_error < expected_error, f"误差 {actual_error} 大于预期 {expected_error}"

@pytest.mark.parametrize("method,func,threshold", [
    ("Nilakantha", calculate_nilakantha, 1e-8),
    ("Gauss-Legendre", calculate_gauss_legendre, 1e-12),
    ("Chudnovsky", lambda: float(calculate_chudnovsky(20)), 1e-15)
])
def test_advanced_methods_accuracy(method, func, threshold):
    """测试高级计算方法的精度"""
    pi = func()
    error = estimate_error(pi, method)
    assert error < threshold, f"{method}方法的误差 {error} 超过阈值 {threshold}"

def test_nilakantha_convergence():
    """测试Nilakantha级数的收敛性"""
    results = [calculate_nilakantha(n) for n in [10, 100, 1000]]
    errors = [abs(x - np.pi) for x in results]
    # 验证误差是否随项数增加而减小
    assert all(errors[i] > errors[i+1] for i in range(len(errors)-1))

def test_gauss_legendre_rapid_convergence():
    """测试Gauss-Legendre算法的快速收敛性"""
    # 即使很少的迭代次数也应该得到较高的精度
    pi = calculate_gauss_legendre(5)
    assert abs(pi - np.pi) < 1e-10

def test_chudnovsky_high_precision():
    """测试Chudnovsky算法的高精度"""
    pi = calculate_chudnovsky(50)
    # 转换为字符串进行前30位比较
    pi_str = str(pi)
    np_pi_str = str(Decimal(np.pi))
    assert pi_str[:30] == np_pi_str[:30]

def test_error_estimation():
    """测试误差估算函数"""
    # 使用一个已知误差的值
    test_pi = 3.14
    error = estimate_error(test_pi, "test")
    expected_error = abs(test_pi - np.pi) / np.pi
    assert abs(error - expected_error) < 1e-10
