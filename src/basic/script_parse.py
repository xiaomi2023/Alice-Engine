from . import runner
from typing import List, Tuple, Optional, Dict


class Point:
    def __init__(self, text: str = "", choice: Optional[List[Tuple[str, Optional['Point']]]] = None):
        if choice is None:
            choice = []
        self.text: str = text
        self.choice: List[Tuple[str, Optional['Point']]] = choice

    def __repr__(self) -> str:
        name: str = 'unnamed'
        # 读取Point节点的名字
        for obj_name, value in globals().items():
            if value is self:
                name = obj_name
        return f"Point object '{name}', text='{self.text}', choice={self.choice}"


def choose(_point: Point, _input: int) -> Optional[Point]:
    """对选项对应的节点进行链接"""
    return _point.choice[_input][1]


def parse_string(string: str) -> str:
    """输出字符串进行处理"""
    # 处理转义字符
    escape: List[Tuple[str, str]] = [
        ("$n", "\n"),
        ("$s", " "),
        ("$t", "\t"),
        ("$p", "#"),
        ("$l", "{"),
        ("$r", "}"),
        ("$b", "\r"),
        ("$k", "/")
    ]
    for i in escape:
        string = string.replace(i[0], i[1])
    # 删除结尾冗余换行符和空格
    while string and string[-1] in {"\n", " "}:
        string = string[:-1]
    return string


def read_script(file: str) -> Tuple[str, Point]:
    with open(file, encoding="utf-8") as f:
        string: str = f.read()
    return string.split("&")[0], parse_script("".join(string.split("&")[1:]))  # 解析脚本文件中定义的游戏名和游戏脚本（用“&”分隔）


def parse_script(string: str) -> Point:
    """将脚本文件解析为Point对象"""
    # 删除注释
    while "/*" in string:
        comment_start: Optional[int] = None
        for e in range(len(string)):
            if string[e:e + 2] == "/*" and comment_start is None:
                comment_start = e
            elif string[e:e + 2] == "*/":
                string = string[:comment_start] + string[e + 2:]
                break

    # 删除冗余空格
    after_newline: bool = False
    while " " in string:
        for i in range(len(string)):
            try:
                if string[i] == "\n":
                    after_newline = True
                elif string[i] != " ":
                    after_newline = False
                if after_newline and string[i] == " ":
                    string = string[:i] + string[i + 1:]
                    after_newline = False
                    break
            except IndexError:
                pass

    def _split(t: str, x: str) -> List[str]:
        """分割字符串"""
        num: int = 0  # 嵌套层数
        result: List[str] = []
        start: int = 0
        # 判断是否位于嵌套节点内
        for j in range(len(t)):
            try:
                if t[j] == "{":
                    num += 1
                elif t[j] == "}":
                    num -= 1
            except IndexError:
                pass
            if num == 0 and t[j:j + len(x)] == x:
                result.append(t[start:j])
                start = j + len(x)
        result.append(t[start:])
        return [d for d in result if d != ""]

    def parse_choice(choice: str) -> Tuple[str, Optional[Point]]:
        """解析选项"""
        choice = choice[1:]  # 删除选项脚本开头的“#”
        point_start: Optional[int] = None
        point_end: Optional[int] = None
        for c in range(len(choice)):
            if choice[c] == "{" and point_start is None:
                point_start = c
            elif choice[c] == "}":
                point_end = c
        if "{" in choice:
            return choice.split("{")[0], parse_point(choice[point_start:point_end + 1])  # 分别返回选项文本和选项文本对应的节点
        else:
            return choice, None  # 只返回选项文本

    def parse_point(point: str) -> Point:
        """解析节点"""
        point_start: Optional[int] = None
        point_end: int = 0
        for k in range(len(point)):
            if point[k] == "{" and point_start is None:
                point_start = k
            elif point[k] == "}":
                point_end = k
        point = point[point_start + 1:point_end]  # 截去大括号之外的冗余字符串
        # 解析代码调用
        for _ in range(int(point.count("@") / 2) + 1):
            code_start: Optional[int] = None
            n: int = 0  # 嵌套层数
            for k in range(len(point)):
                if point[k] == "{":
                    n += 1
                elif point[k] == "}":
                    n -= 1
                if n == 0 and point[k] == "@":
                    if code_start is None:
                        code_start = k
                        continue
                    else:
                        point = point[:code_start] + runner.run_code(point[code_start + 1:k]) + point[k + 1:]
                        break
        string_list: List[str] = _split(point, "#")  # 通过“#”分割节点文本和选项
        return Point(string_list[0],
                     [parse_choice("#" + string_list[a]) for a in range(len(string_list)) if a != 0])  # 返回Point节点，参数包括节点文本和选项列表
    return parse_point(string)  # 返回对脚本的解析