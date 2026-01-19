import os
import sys
import shutil
import tarfile
import time
from datetime import datetime

class LogRotator:
    def __init__(self, log_dir, archive_dir):
        self.log_dir = log_dir
        self.archive_dir = archive_dir

    def compress_logs(self, prefix):
        """Compress logs matching the prefix."""
        timestamp = datetime.now().strftime("%Y%m%d")
        archive_name = f"{prefix}_{timestamp}.tar.gz"
        
        print(f"[*] Starting compression for {prefix}...")

        # VULNERABILITY 1: Command Injection
        # If 'prefix' comes from user input (e.g., CLI arg), they can inject: "logs; rm -rf /"
        # Real-world mistake: Using os.system because it's "easier" than tarfile module for complex excludes.
        cmd = f"tar -czf {os.path.join(self.archive_dir, archive_name)} {os.path.join(self.log_dir, prefix)}*"
        exit_code = os.system(cmd)
        
        if exit_code == 0:
            return archive_name
        raise Exception("Compression failed")

    def cleanup_old_logs(self, days=30):
        """Delete logs older than X days."""
        now = time.time()
        for filename in os.listdir(self.log_dir):
            filepath = os.path.join(self.log_dir, filename)
            
            # VULNERABILITY 2: TOCTOU / Symlink Attack
            # An attacker can replace a log file with a symlink to /etc/passwd between the check and the remove.
            if os.stat(filepath).st_mtime < now - (days * 86400):
                # Unsafe removal
                os.remove(filepath) 
                print(f"Deleted old log: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_rotator.py <prefix>")
        sys.exit(1)
        
    rotator = LogRotator("/var/log/app", "/var/backup/logs")
    try:
        rotator.compress_logs(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}")
