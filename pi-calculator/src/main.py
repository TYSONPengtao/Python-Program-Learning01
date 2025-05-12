import time
import math
import matplotlib.pyplot as plt
import numpy as np
from algorithms.leibniz import calculate_leibniz
from algorithms.monte_carlo import calculate_monte_carlo

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

def main():
    print("计算π值并比较两种方法的性能...\n")
    
    # 使用较大的项数进行单次计算
    n = 1_000_000
    
    # 莱布尼茨方法
    start_time = time.perf_counter()
    leibniz_pi = calculate_leibniz(n)
    leibniz_time = time.perf_counter() - start_time
    
    # 蒙特卡罗方法
    start_time = time.perf_counter()
    monte_carlo_pi = calculate_monte_carlo(n)
    monte_carlo_time = time.perf_counter() - start_time
    
    # 输出结果
    print(f"真实的π值: {math.pi}")
    print("\n莱布尼茨公式:")
    print(f"计算值: {leibniz_pi:.10f}")
    print(f"误差: {abs(leibniz_pi - math.pi):.10f}")
    print(f"计算时间: {leibniz_time:.3f}秒")
    
    print("\n蒙特卡罗方法:")
    print(f"计算值: {monte_carlo_pi:.10f}")
    print(f"误差: {abs(monte_carlo_pi - math.pi):.10f}")
    print(f"计算时间: {monte_carlo_time:.3f}秒")
    
    # 绘制性能和精度对比图
    print("\n正在生成性能和精度对比图...")
    terms, l_errors, m_errors, l_times, m_times = compare_methods()
    plot_results(terms, l_errors, m_errors, l_times, m_times)

if __name__ == "__main__":
    main()
