import pytest
from basic.script_parse import Point, read_script, choose, parse_string, parse_script
import os

def test_point_initialization():
    point = Point("test text", ["choice1", "choice2"])
    assert point.text == "test text"
    assert point.choice == ["choice1", "choice2"]

def test_choose_function():    
    next_point = Point("next point")
    current_point = Point("current", [("option1", next_point)])
    assert choose(current_point, 0) == next_point

def test_parse_string_escape_chars():    
    assert parse_string("line1$nline2") == "line1\nline2"
    assert parse_string("$s$t$p") == " \t#"
    assert parse_string("abc$kdef") == "abc/def"

@pytest.fixture
def sample_script_file(tmp_path):
    script_content = "Test Game&{Start Text#Option1{Next Text}#Option2}"
    file = tmp_path / "test_script.as"
    file.write_text(script_content, encoding="utf-8")
    return str(file)

def test_read_script(sample_script_file):    
    title, start_point = read_script(sample_script_file)
    assert title == "Test Game"
    assert start_point.text == "Start Text"
    assert len(start_point.choice) == 2

def test_parse_script_basic():    
    script_content = "{Root Text#Choice1{Child Text}#Choice2}"
    root = parse_script(script_content)
    assert root.text == "Root Text"
    assert len(root.choice) == 2
    assert root.choice[0][0] == "Choice1"
    assert root.choice[0][1].text == "Child Text"