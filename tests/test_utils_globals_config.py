from zen.api.prelude import UserConfig
from zen.utils.globals.config import *


def some_mock_func():
    pass


def mock_user_main() -> UserConfig:
    cfg = UserConfig()
    return cfg


def test_config():
    cfg = mock_user_main()
    # Assert that CONFIG is correctly returned
    assert cfg == UserConfig()
