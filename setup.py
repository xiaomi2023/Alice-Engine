from setuptools import setup, find_packages

setup(
    name="alice_engine",          # 包名（PyPI上的名称）
    version="1.0",                # 版本号
    author="xiaomi2023",           # 作者名
    description="Alice Engine(v0.1)是一个文字游戏引擎，旨在让游戏开发者简便地开发属于自己的文字游戏。引擎使用 python 语言开发,而用户可以使用一个名为alice_script的语言开发，操作简单，新手可轻松上手。",  # 简短描述
    long_description=open("README.md","r",encoding="utf-8").read(),            # 长描述（通常从README.md读取）
    long_description_content_type="text/markdown",        # 长描述格式（Markdown）
    url="https://github.com/xiaomi2023/Alice-Engine",   # 项目GitHub地址
    packages=['alice_engine'],
    package_dir={
        'alice_engine': 'src/basic'
    },
    python_requires=">=3.7",                                  # Python版本要求
    classifiers=[                                             # 分类标签（PyPI元数据）
        "Programming Language :: Python :: 3",
    ],
)

#如何构建？运行python setup.py sdist bdist_wheel即可