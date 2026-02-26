from . import mainloop
from . import script_parse
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mainloop import GUI
    from script_parse import Point

class GameRunner:
    def __init__(self, file: str) -> None:
        self.file: str = file

    def run_game(self) -> None:
        # 初始化全局应用实例
        game: 'GUI' = mainloop.GUI()  # 实例化GUI对象
        script: tuple[str, 'Point'] = script_parse.read_script(self.file)  # 读取脚本文件
        game.root.title(script[0])  # 设置窗口标题
        points: 'Point' = script[1]  # 读取脚本文件

        while True:
            try:
                # 输出节点文本，读取并输出选项文本
                game.output(points.text, [i[0] for i in points.choice])
            except AttributeError as e:
                raise Exception(f"由于游戏结束或遇到错误，游戏程序已停止，详细的信息如下：\n{e}")

            # 选择选项并更新节点
            points = script_parse.choose(points, game.input())

        # noinspection PyUnreachableCode
        game.root.mainloop()