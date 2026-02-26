from . import mainloop
from typing import Any


def echo(text: Any) -> None:
    """
    输出内容到控制台

    :param text: 要输出到控制台的内容，可以是任意类型
    """
    print(text)


def create_gui():
    """
    创造一个GUI对象

    :return: 一个GUI对象实例
    """
    return mainloop.GUI()
