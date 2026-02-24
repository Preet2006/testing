import sys
import os
import subprocess

class BackupService:
    def __init__(self, backup_dir="/tmp/backups"):
        self.backup_dir = backup_dir
        # Ensure backup dir exists so the tar command doesn't crash on legitimate runs
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

    def create_backup(self, filename):
        print(f"[*] Starting backup for: {filename}")
        
        # Use subprocess with list, never shell=True to prevent command injection
        command = ["tar", "-czf", f"{self.backup_dir}/archive.tar.gz", filename]
        
        print(f"DEBUG: Executing shell command: {' '.join(command)}")
        subprocess.run(command, capture_output=True, text=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Create a dummy file to back up if it doesn't exist
        if not os.path.exists(sys.argv[1]) and not ";" in sys.argv[1]:
            with open(sys.argv[1], "w") as f: f.write("dummy data")
            
        service = BackupService()
        service.create_backup(sys.argv[1])
    else:
        print("Usage: python backup_service.py <filename>")