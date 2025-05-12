import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from typing import Tuple, List

def create_monte_carlo_animation(num_points: int = 1000, frames: int = 100) -> animation.FuncAnimation:
    """
    创建蒙特卡罗方法计算π的动画可视化
    
    Args:
        num_points: 每帧的点数
        frames: 动画帧数
    
    Returns:
        animation.FuncAnimation: 动画对象
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 设置第一个子图（散点图）
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    circle = plt.Circle((0, 0), 1, fill=False, color='red')
    ax1.add_artist(circle)
    ax1.set_aspect('equal')
    ax1.grid(True)
    ax1.set_title('蒙特卡罗采样点')
    
    # 设置第二个子图（收敛曲线）
    ax2.set_xlim(0, frames)
    ax2.set_ylim(3.0, 3.3)
    ax2.axhline(y=np.pi, color='r', linestyle='--', label='真实π值')
    ax2.grid(True)
    ax2.set_title('π值收敛过程')
    ax2.legend()
    
    points_inside = []
    points_outside = []
    pi_estimates = []
    
    def init():
        return []
    
    def animate(frame):
        # 生成新的随机点
        x = np.random.uniform(-1, 1, num_points)
        y = np.random.uniform(-1, 1, num_points)
        distances = np.sqrt(x**2 + y**2)
        
        # 分类点
        inside_mask = distances <= 1
        points_inside.append((x[inside_mask], y[inside_mask]))
        points_outside.append((x[~inside_mask], y[~inside_mask]))
        
        # 计算π值
        total_points = num_points * (frame + 1)
        total_inside = sum(len(x) for x, _ in points_inside)
        pi_estimate = 4 * total_inside / total_points
        pi_estimates.append(pi_estimate)
        
        # 更新散点图
        ax1.clear()
        ax1.set_xlim(-1, 1)
        ax1.set_ylim(-1, 1)
        circle = plt.Circle((0, 0), 1, fill=False, color='red')
        ax1.add_artist(circle)
        ax1.set_aspect('equal')
        ax1.grid(True)
        ax1.set_title(f'蒙特卡罗采样点 (n={total_points})')
        
        for in_x, in_y in points_inside:
            ax1.scatter(in_x, in_y, c='blue', alpha=0.6, s=1)
        for out_x, out_y in points_outside:
            ax1.scatter(out_x, out_y, c='gray', alpha=0.6, s=1)
            
        # 更新收敛曲线
        ax2.clear()
        ax2.set_xlim(0, frames)
        ax2.set_ylim(3.0, 3.3)
        ax2.axhline(y=np.pi, color='r', linestyle='--', label='真实π值')
        ax2.plot(pi_estimates, 'b-', label='估算值')
        ax2.grid(True)
        ax2.set_title(f'π值收敛过程 (当前估计: {pi_estimate:.6f})')
        ax2.legend()
        
        return []
    
    ani = animation.FuncAnimation(
        fig, animate, frames=frames,
        init_func=init, blit=True, interval=50
    )
    
    plt.tight_layout()
    return ani

def save_animation(animation: animation.FuncAnimation, filename: str = 'pi_calculation.gif'):
    """
    保存动画为GIF文件
    
    Args:
        animation: 动画对象
        filename: 输出文件名
    """
    animation.save(filename, writer='pillow')
