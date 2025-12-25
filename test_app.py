from unittest.mock import patch, MagicMock
from app import login
@patch('sqlite3.connect')
def test_login_success(mock_connect):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ('admin', 'pass')
    mock_connect.return_value.cursor.return_value = mock_cursor
    assert login('admin', 'pass') == True