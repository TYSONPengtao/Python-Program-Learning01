import pytest
import math
import numpy as np
from algorithms.leibniz import calculate_leibniz
from algorithms.monte_carlo import calculate_monte_carlo
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
