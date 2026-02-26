import pytest
from src.basic.main import GameRunner
from unittest.mock import patch, MagicMock

@pytest.fixture
def game_runner():    
    with patch('src.basic.main.mainloop.GUI') as mock_gui, \
         patch('src.basic.main.script_parse.read_script') as mock_read:
        mock_read.return_value = ('Test Game', MagicMock(text='Start', choice=[]))
        runner = GameRunner('test.as')
        yield runner


def test_game_runner_initialization(game_runner):
    assert game_runner.file == 'test.as'


def test_run_game_normal_flow(game_runner):
    # 模拟游戏流程直到结束
    mock_point = MagicMock()
    mock_point.text = 'End'
    mock_point.choice = []
    game_runner.run_game()
    assert game_runner.script_parse.read_script.called


def test_run_game_exception_handling(game_runner):
    # 测试游戏结束时的异常处理
    with patch('src.basic.main.script_parse.choose') as mock_choose:
        mock_choose.side_effect = AttributeError('Game Over')
        with pytest.raises(Exception) as excinfo:
            game_runner.run_game()
        assert '游戏结束' in str(excinfo.value)