import platform
import subprocess
import re

def ping_ip(ip):
    # Sanitize the input
    if not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip):
        raise ValueError('Invalid IP address')

    # Replace os.system() with a secure alternative
    try:
        if platform.system() == 'Windows':
            cmd = ['ping', '-n', '1', ip]
        else:
            cmd = ['ping', '-c', '1', ip]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        return False
    except subprocess.TimeoutExpired as e:
        return False
    except Exception as e:
        raise ValueError(f'Invalid expression: {str(e)}')
