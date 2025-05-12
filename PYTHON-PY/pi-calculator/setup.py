from setuptools import setup, find_packages

setup(
    name='pi-calculator',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # 在这里列出项目所需的依赖包
    ],
    entry_points={
        'console_scripts': [
            'pi-calculator=main:main',  # 假设 main.py 中有一个名为 main 的函数作为入口
        ],
    },
    author='你的名字',
    author_email='你的邮箱@example.com',
    description='一个计算圆周率的项目',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='项目的GitHub链接',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)