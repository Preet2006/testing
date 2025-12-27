from unittest.mock import patch, MagicMock
from logic import search_user, login
@patch('logic.run_query_safe')
def test_search_user_success(mock_run_query_safe):
    mock_run_query_safe.return_value = [('admin', 'pass')]
    result = search_user('admin')
    assert result == [('admin', 'pass')]