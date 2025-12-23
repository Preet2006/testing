from solution import login
import pytest
from unittest.mock import patch, MagicMock

@patch('sqlite3.connect')
def test_valid_login(mock_connect):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ('admin', 'password123')
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn
    result = login('admin', 'password123')
    assert result == True

@patch('sqlite3.connect')
def test_invalid_login(mock_connect):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn
    result = login('wrong', 'credentials')
    assert result == False

@patch('sqlite3.connect')
def test_sql_injection(mock_connect):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn
    result = login("' OR 1=1 --", 'anything')
    assert result == False