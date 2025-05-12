from setuptools import setup, find_packages

setup(
    name="pi-calculator",
    version="0.2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pytest>=6.0.0",
        "matplotlib>=3.4.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="一个使用多种方法计算π值的Python项目",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pi-calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
