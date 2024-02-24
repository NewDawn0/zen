import os
import sys
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from api.builtins import *


# Mock the App class and its methods
@pytest.fixture
def mock_app():
    app = MagicMock(spec=App)
    return app


# Mock the Widget class and its methods
@pytest.fixture
def mock_widget():
    widget = MagicMock(spec=Widget)
    return widget


def test_notify(mock_app):
    # Setup
    BUILTINS._app = mock_app
    msg = "Test message"
    severity = "information"
    # Call the method under test
    BUILTINS.notify(msg, severity)
    # Assert
    mock_app.notify.assert_called_once_with(msg, severity=severity)


def test_bell(mock_app):
    # Setup
    BUILTINS._app = mock_app
    # Call the method under test
    BUILTINS.bell()
    # Assert
    mock_app.bell.assert_called_once()


def test_toggle_widget(mock_app, mock_widget):
    # Setup
    BUILTINS._app = mock_app
    mock_app.query_one.return_value = mock_widget
    # Call the method under test
    BUILTINS.toggle_widget(mock_widget)
    # Assert
    mock_app.query_one.assert_called_once_with(mock_widget)
    mock_widget.toggle_class.assert_called_once_with("-hidden")


def test_quit(mock_app):
    # Setup
    BUILTINS._app = mock_app
    # Call the method under test
    BUILTINS.quit()
    # Assert
    mock_app.exit.assert_called_once()


def test_quit_buf(mock_app):
    # Setup
    BUILTINS._app = mock_app
    mock_app.query_one.return_value = MagicMock()
    # Call the method under test
    BUILTINS.quit_buf()
    # Assert
    mock_app.query_one.assert_called_once_with("BufManagerWrapper")
    mock_app.query_one.return_value._quit.assert_called_once()


def test_save_buf(mock_app):
    # Setup
    BUILTINS._app = mock_app
    mock_app.query_one.return_value = MagicMock()
    # Call the method under test
    BUILTINS.save_buf()
    # Assert
    mock_app.query_one.assert_called_once_with("BufManager")
    mock_app.query_one.return_value._save.assert_called_once()


def test_open_buf(mock_app):
    # Setup
    BUILTINS._app = mock_app
    file_name = "test_file.txt"
    mock_app.query_one.return_value = MagicMock()
    # Call the method under test
    BUILTINS.open_buf(file_name)
    # Assert
    mock_app.query_one.assert_called_once_with("BufManagerWrapper")
    mock_app.query_one.return_value._open.assert_called_once_with(file_name)
