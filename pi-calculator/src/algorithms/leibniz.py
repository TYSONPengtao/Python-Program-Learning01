import numpy as np

def calculate_leibniz(terms: int = 1_000_000) -> float:
    """
    使用莱布尼茨级数计算π值
    π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    
    Args:
        terms: 计算项数，默认为1,000,000（使用下划线提高可读性）
    
    Returns:
        float: 计算得到的π值
        
    Performance:
        使用numpy的向量化运算提高性能
    """
    # 使用numpy的向量化运算提高性能
    k = np.arange(terms)
    series = (-1) ** k / (2 * k + 1)
    pi = 4 * np.sum(series)
    return float(pi)  # 确保返回Python float类型

if __name__ == "__main__":
    pi = calculate_leibniz()
    print(f"使用莱布尼茨级数计算的π值: {pi:.10f}")
