import time
import math
import matplotlib.pyplot as plt
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
from algorithms.visualization import create_monte_carlo_animation, save_animation

def compare_methods(max_terms: int = 1_000_000, step: int = 100_000):
    """比较两种方法的性能和精度"""
    terms = np.arange(step, max_terms + step, step)
    leibniz_errors = []
    monte_carlo_errors = []
    leibniz_times = []
    monte_carlo_times = []
    
    for n in terms:
        # 莱布尼茨方法
        start_time = time.perf_counter()
        leibniz_pi = calculate_leibniz(n)
        leibniz_time = time.perf_counter() - start_time
        leibniz_errors.append(abs(leibniz_pi - math.pi))
        leibniz_times.append(leibniz_time)
        
        # 蒙特卡罗方法
        start_time = time.perf_counter()
        monte_carlo_pi = calculate_monte_carlo(n)
        monte_carlo_time = time.perf_counter() - start_time
        monte_carlo_errors.append(abs(monte_carlo_pi - math.pi))
        monte_carlo_times.append(monte_carlo_time)
    
    return terms, leibniz_errors, monte_carlo_errors, leibniz_times, monte_carlo_times

def plot_results(terms, leibniz_errors, monte_carlo_errors, leibniz_times, monte_carlo_times):
    """绘制性能和精度对比图"""
    plt.figure(figsize=(12, 6))
    
    # 精度对比
    plt.subplot(1, 2, 1)
    plt.plot(terms, leibniz_errors, label='莱布尼茨方法')
    plt.plot(terms, monte_carlo_errors, label='蒙特卡罗方法')
    plt.xlabel('项数/采样点数')
    plt.ylabel('误差')
    plt.title('精度对比')
    plt.legend()
    plt.grid(True)
    
    # 性能对比
    plt.subplot(1, 2, 2)
    plt.plot(terms, leibniz_times, label='莱布尼茨方法')
    plt.plot(terms, monte_carlo_times, label='蒙特卡罗方法')
    plt.xlabel('项数/采样点数')
    plt.ylabel('计算时间 (秒)')
    plt.title('性能对比')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def visualize_monte_carlo(save_gif: bool = True):
    """创建蒙特卡罗方法的动态可视化"""
    print("\n创建蒙特卡罗方法的动态可视化...")
    animation = create_monte_carlo_animation(num_points=1000, frames=100)
    
    if save_gif:
        print("正在保存动画...")
        save_animation(animation, 'pi_calculation.gif')
        print("动画已保存为 'pi_calculation.gif'")
    else:
        plt.show()

def compare_all_methods(max_terms: int = 1_000_000):
    """比较所有方法的性能和精度"""
    methods = {
        '莱布尼茨级数': lambda n: calculate_leibniz(n),
        '蒙特卡罗方法': lambda n: calculate_monte_carlo(n),
        'Nilakantha级数': lambda n: calculate_nilakantha(n//100),  # 使用较少的项数因为收敛更快
        'Gauss-Legendre': lambda n: calculate_gauss_legendre(int(np.log2(n))),  # 迭代次数随项数对数增长
        'Chudnovsky': lambda n: float(calculate_chudnovsky(int(np.log10(n)) + 10))  # 精度随项数对数增长
    }
    
    results = {}
    for method_name, method_func in methods.items():
        start_time = time.perf_counter()
        pi_value = method_func(max_terms)
        compute_time = time.perf_counter() - start_time
        error = estimate_error(pi_value, method_name)
        results[method_name] = {
            'value': pi_value,
            'time': compute_time,
            'error': error
        }
    
    return results

def plot_comparison(results: dict):
    """绘制各方法性能和精度对比图"""
    method_names = list(results.keys())
    times = [results[name]['time'] for name in method_names]
    errors = [results[name]['error'] for name in method_names]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 计算时间对比
    ax1.bar(method_names, times)
    ax1.set_title('计算时间对比')
    ax1.set_ylabel('时间 (秒)')
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 误差对比（使用对数刻度）
    ax2.bar(method_names, errors)
    ax2.set_yscale('log')
    ax2.set_title('相对误差对比 (对数刻度)')
    ax2.set_ylabel('相对误差')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

def main():
    print("计算π值并比较各种方法...\n")
    
    # 比较所有方法
    results = compare_all_methods()
    
    # 输出结果
    print(f"真实的π值: {math.pi}\n")
    for method_name, result in results.items():
        print(f"{method_name}:")
        print(f"计算值: {result['value']:.12f}")
        print(f"相对误差: {result['error']:.2e}")
        print(f"计算时间: {result['time']:.3f}秒\n")
    
    # 绘制对比图
    print("正在生成性能和精度对比图...")
    plot_comparison(results)
    
    # 创建蒙特卡罗方法的动态可视化
    print("\n创建蒙特卡罗方法的动态可视化...")
    visualize_monte_carlo(save_gif=True)

if __name__ == "__main__":
    main()
