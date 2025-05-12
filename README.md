# Python-Program-Learning01

本仓库专注于使用多种算法计算圆周率 (π)，旨在帮助读者理解不同算法的原理与实现，并比较它们的精度与效率。项目示例覆盖从最基础的无穷级数到随机模拟和高效收敛算法，适合 Python 学习者与对数值计算感兴趣的开发者。

## 概述

圆周率 π 是数学常数，表示圆的周长与直径之比，约等于 3.14159… ([en.wikipedia.org](https://en.wikipedia.org/wiki/Pi?utm_source=chatgpt.com))。
本项目实现了以下几类常见的 π 计算方法：

* **无穷级数法**：如格里高利–莱布尼茨级数 (Leibniz Series) ([en.wikipedia.org](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80?utm_source=chatgpt.com))；
* **Nilakantha 级数**：改进的无穷级数，收敛速度更快 ([geeksforgeeks.org](https://www.geeksforgeeks.org/calculate-pi-using-nilkanthas-series/?utm_source=chatgpt.com))；
* **蒙特卡罗模拟**：基于随机点落在单位圆内的概率估计 ([geeksforgeeks.org](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/?utm_source=chatgpt.com))；
* **Gauss–Legendre 算法**：二次收敛，迭代次数少但对内存要求高 ([en.wikipedia.org](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm?utm_source=chatgpt.com))；
* **Chudnovsky 算法**（可选扩展）：高效计算上亿位 π，用于极限精度需求。

## 目录结构

```plaintext
Python-Program-Learning01/
├── leibniz.py         # 实现格里高利–莱布尼茨级数计算 π
├── nilakantha.py      # 实现 Nilakantha 级数计算 π
├── monte_carlo.py     # 实现蒙特卡罗方法估算 π
├── gauss_legendre.py  # 实现 Gauss–Legendre 算法计算 π
├── chudnovsky.py      # (可选) Chudnovsky 快速算法示例
├── requirements.txt   # 依赖列表
└── README.md          # 本文件
```

## 快速开始

1. 克隆仓库并进入目录：

   ```bash
   git clone https://github.com/TYSONPengtao/Python-Program-Learning01.git
   cd Python-Program-Learning01
   ```
2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```
3. 运行示例：

   ```bash
   python leibniz.py --iterations 1000000
   python monte_carlo.py --points 1000000
   ```

## 算法介绍

### 格里高利–莱布尼茨级数

使用以下无穷级数：

$$
\frac{\pi}{4} = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}
$$

实现简单，但收敛极慢。要获得 3 位小数准确度，需约 5000 项 ([proofwiki.org](https://proofwiki.org/wiki/Leibniz%27s_Formula_for_Pi?utm_source=chatgpt.com))。

### Nilakantha 级数

改良的无穷级数：

$$
\pi = 3 + \sum_{k=0}^{\infty} \frac{4(-1)^k}{(2k+2)(2k+3)(2k+4)}
$$

收敛速度较 Leibniz 快，约 1000 项可得 5 位精度 ([geeksforgeeks.org](https://www.geeksforgeeks.org/calculate-pi-using-nilkanthas-series/?utm_source=chatgpt.com))。

### 蒙特卡罗模拟

在单位正方形内随机撒点，统计落入单位圆内的点数比例：

$$
\pi \approx 4 \times \frac{\text{CirclePoints}}{\text{TotalPoints}}
$$

适合并行计算，但精度依赖随机数数量 ([geeksforgeeks.org](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/?utm_source=chatgpt.com))。

### Gauss–Legendre 算法

初始化：

$$
a_0 = 1, \quad b_0 = \frac{1}{\sqrt{2}}, \quad t_0 = \frac{1}{4}, \quad p_0 = 1
$$

迭代：

$$
a_{n+1} = \frac{a_n + b_n}{2}, \quad b_{n+1} = \sqrt{a_n b_n},
$$

$$
t_{n+1} = t_n - p_n(a_n - a_{n+1})^2, \quad p_{n+1} = 2p_n
$$

收敛二次，被广泛用于高精度计算 ([en.wikipedia.org](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm?utm_source=chatgpt.com))。

## 性能对比

| 算法              | 收敛速度     | 空间复杂度    | 备注     |
| --------------- | -------- | -------- | ------ |
| Leibniz         | 极慢       | O(1)     | 仅教学示例  |
| Nilakantha      | 中速       | O(1)     | 实用基础   |
| Monte Carlo     | 随机收敛     | O(1)     | 支持并行   |
| Gauss–Legendre  | 快（二次收敛）  | O(1)     | 对内存略敏感 |
| Chudnovsky (扩展) | 超快（线性收敛） | O(n) 或更高 | 用于超高精度 |

## 贡献指南

欢迎提交 Issue 或 Pull Request，完善算法实现、优化性能、增加新方法或测试。

## 作者

* **TYSON Pengtao**

如有问题，请通过 GitHub Issues 联系。
