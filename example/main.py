import sys
import os

# 下面的代码用于访问到到源目录
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.basic import GameRunner
#from alice_engine import GameRunner

game_runner = GameRunner("example/example-script.as")
game_runner.run_game()
