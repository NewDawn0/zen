from zen.utils.globals.bufs import BUF_NAME_TO_TEXT_BUF_DICT
from zen.utils.globals.bufs import CURR_BUF


def test_buf_name_to_text_buf_dict_initialization():
    assert BUF_NAME_TO_TEXT_BUF_DICT == {}


def test_curr_buf_initialization():
    assert CURR_BUF is None


def test_add_and_remove_buffer():
    # Test adding a buffer
    BUF_NAME_TO_TEXT_BUF_DICT["test_buf"] = "test_text"
    assert "test_buf" in BUF_NAME_TO_TEXT_BUF_DICT
    assert BUF_NAME_TO_TEXT_BUF_DICT["test_buf"] == "test_text"
    # Test removing a buffer
    del BUF_NAME_TO_TEXT_BUF_DICT["test_buf"]
    assert "test_buf" not in BUF_NAME_TO_TEXT_BUF_DICT


def test_set_and_clear_current_buffer():
    # Test setting the current buffer
    CURR_BUF = "test_buf"
    assert CURR_BUF == "test_buf"
    # Test clearing the current buffer
    CURR_BUF = None
    assert CURR_BUF is None
