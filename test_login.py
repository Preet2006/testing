from login import login
import pytest
import unittest
from unittest.mock import patch

@pytest.fixture
def mock_db_connection():
    with patch('psycopg2.connect') as mock_connect:
        yield mock_connect

def test_valid_login(mock_db_connection):
    mock_db_connection.return_value.cursor.return_value.fetchall.return_value = [(1, 'testuser', 'testpassword')]
    assert login('testuser', 'testpassword') == True

def test_invalid_login(mock_db_connection):
    mock_db_connection.return_value.cursor.return_value.fetchall.return_value = []
    assert login('testuser', 'wrongpassword') == False

def test_sql_injection_payload(mock_db_connection):
    mock_db_connection.return_value.cursor.return_value.fetchall.return_value = []
    with pytest.raises(ValueError):
        login("' OR '1'='1", 'testpassword')

def test_sql_injection_payload_admin(mock_db_connection):
    mock_db_connection.return_value.cursor.return_value.fetchall.return_value = []
    with pytest.raises(ValueError):
        login("' admin' -- '", 'testpassword')

def test_invalid_input(mock_db_connection):
    with pytest.raises(ValueError):
        login('!@#$', 'testpassword')
