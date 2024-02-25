from zen.utils.key_chords import *


# Mock CONFIG.key_binds for testing
CONFIG.key_binds = {
    ("ctrl", "c"): lambda: print("Ctrl+C pressed"),
    ("ctrl", "v"): lambda: print("Ctrl+V pressed"),
}


def test_add_key():
    key_chorder = KeyChorder()
    key_chorder.add("ctrl")
    assert key_chorder.get() == ["ctrl"]


def test_try_exec_success():
    key_chorder = KeyChorder()
    key_chorder.add("ctrl")
    key_chorder.add("c")
    assert key_chorder.try_exec() == 2


def test_try_exec_failure():
    key_chorder = KeyChorder()
    key_chorder.add("ctrl")
    key_chorder.add("x")
    assert key_chorder.try_exec() == 0


def test_normalize_key():
    key_chorder = KeyChorder()
    assert key_chorder._normalize("space") == "spc"
    assert key_chorder._normalize("left_parenthesis") == "("
    assert key_chorder._normalize("unknown_key") == "unknown_key"


def test_reset_timer():
    key_chorder = KeyChorder()
    key_chorder.add("ctrl")
    key_chorder.add("c")
    assert key_chorder.timer is not None
    key_chorder._reset_timer()
    assert key_chorder.timer is not None


def test_clear():
    key_chorder = KeyChorder()
    key_chorder.add("ctrl")
    key_chorder.add("c")
    assert key_chorder.get() == ["ctrl", "c"]
    key_chorder.clear()
    assert key_chorder.get() == []
