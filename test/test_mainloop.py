import pytest
from src.basic.mainloop import GUI
import tkinter as tk
from unittest.mock import patch, MagicMock
import time

@pytest.fixture
def gui(monkeypatch):
    # 防止Tkinter创建实际窗口
    monkeypatch.setattr(tk, 'Tk', MagicMock())
    gui = GUI()
    return gui

def test_gui_initialization(gui):
    assert gui.text == ""
    assert gui.choice == []
    assert isinstance(gui.update_queue, GUI.update_queue.__class__)
    assert gui.choice_index is None

def test_update_interface(gui):
    # 测试界面内容更新
    gui.update_interface("测试文本", ["选项1", "选项2"])
    # 检查队列处理
    gui.check_updates()
    # 验证内容更新
    assert gui.text == "测试文本"
    assert gui.choice == ["选项1", "选项2"]

def test_on_button_click(gui):
    # 测试按钮点击事件
    gui.on_button_click(1)
    assert gui.choice_index == 1

def test_output_method(gui):
    with patch('src.basic.script_parse.parse_string') as mock_parse:
        mock_parse.side_effect = lambda x: x
        gui.output("原始文本", ["原始选项"])
        gui.check_updates()
        assert gui.label.config.called_with(text="原始文本")

def test_input_method(gui):
    # 模拟用户输入
    with patch.object(gui, 'root') as mock_root:
        # 第一次调用：没有选择，等待
        mock_root.update_idletasks.side_effect = lambda: setattr(gui, 'choice_index', 0)
        result = gui.input()
        assert result == 0
        assert gui.choice_index is None