import numpy as np
from numpy.random import default_rng

def calculate_monte_carlo(num_samples: int = 1_000_000, seed: int = None) -> float:
    """
    使用蒙特卡罗方法计算π值
    
    Args:
        num_samples: 采样点数量，默认为1,000,000
        seed: 随机数种子，用于复现结果，默认为None
    
    Returns:
        float: 计算得到的π值
        
    Performance:
        - 使用numpy的向量化运算提高性能
        - 使用新版random number generator提高性能
        - 避免重复计算
    """
    # 使用新版random number generator
    rng = default_rng(seed)
    
    # 一次性生成所有随机点
    points = rng.uniform(-1, 1, (num_samples, 2))
    
    # 计算点到原点的距离（使用einsum优化）
    distances = np.einsum('ij,ij->i', points, points)
    
    # 统计在单位圆内的点数
    inside_circle = np.sum(distances <= 1)
    
    return float(4 * inside_circle / num_samples)

if __name__ == "__main__":
    pi = calculate_monte_carlo()
    print(f"使用蒙特卡罗方法计算的π值: {pi:.10f}")
