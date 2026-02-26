import pytest
from src.basic.runner import Runner, run_code, _is_expression


def test_is_expression():
    assert _is_expression("1 + 2") is True
    assert _is_expression("print('hello')") is True
    assert _is_expression("if True:\n    pass") is False

def test_runner_safe_globals():
    runner = Runner()
    assert 'os' not in runner.global_context
    assert 'api' in runner.global_context
    assert 'eval' not in runner.global_context
    assert 'abs' in runner.global_context

def test_run_code_basic():
    assert run_code("1 + 2") == "3"
    assert run_code("'hello'.upper()") == "HELLO"
    assert run_code("api.echo('test')") == ""

def test_run_code_disallowed_functions():
    with pytest.raises(NameError):
        run_code("os.listdir()")
    with pytest.raises(NameError):
        run_code("__import__('os')")

def test_run_code_context_persistence():
    run_code("x = 10")
    assert run_code("x + 5") == "15"
    run_code("x += 3")
    assert run_code("x") == "13"