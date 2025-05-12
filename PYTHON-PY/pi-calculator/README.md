# README.md

# Pi Calculator

该项目是一个计算圆周率的应用程序，提供了两种算法：莱布尼茨公式和蒙特卡罗方法。用户可以通过运行主程序来计算圆周率并查看结果。

## 文件结构

```
pi-calculator
├── src
│   ├── main.py          # 应用程序入口点
│   ├── algorithms       # 存放计算圆周率算法的目录
│   │   ├── __init__.py  # 将 algorithms 目录标记为一个包
│   │   ├── leibniz.py   # 莱布尼茨公式算法实现
│   │   └── monte_carlo.py # 蒙特卡罗方法算法实现
│   └── tests            # 存放单元测试的目录
│       ├── __init__.py  # 将 tests 目录标记为一个包
│       └── test_algorithms.py # 对算法的单元测试
├── requirements.txt      # 项目所需的Python依赖包
├── setup.py              # 项目的打包和分发
└── README.md             # 项目的文档
```

## 使用说明

1. 克隆该项目到本地：
   ```
   git clone <repository-url>
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 运行主程序：
   ```
   python src/main.py
   ```

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。