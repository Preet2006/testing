import os
def unsafe_ping(ip):
    # Vulnerable to Command Injection
    os.system(f"ping -c 1 {ip}")
