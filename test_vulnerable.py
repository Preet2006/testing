from vulnerable import ping_ip
import pytest
from unittest.mock import patch, MagicMock
import subprocess

@patch('vulnerable.subprocess.run')
def test_ping_success(mock_run):
    # Mock successful ping
    mock_run.return_value = MagicMock(returncode=0, stdout='Reply from...')
    result = ping_ip('8.8.8.8')
    assert result == True
    mock_run.assert_called_once()

@patch('vulnerable.subprocess.run')
def test_ping_failure(mock_run):
    # Mock failed ping
    mock_run.return_value = MagicMock(returncode=1)
    result = ping_ip('192.168.1.1')
    assert result == False

@patch('vulnerable.subprocess.run')
def test_ping_timeout(mock_run):
    # Mock timeout
    mock_run.side_effect = subprocess.TimeoutExpired(1, ['ping', '-c', '1', '8.8.8.8'])
    result = ping_ip('8.8.8.8')
    assert result == False

def test_invalid_ip():
    with pytest.raises(ValueError):
        ping_ip('256.1.1.1')

def test_valid_ip():
    result = ping_ip('8.8.8.8')
    assert result == True
