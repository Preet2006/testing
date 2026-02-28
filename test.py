import os

def delete_user_file():
    filename = input("Enter the filename to delete: ")
    # VULNERABLE: Direct shell execution with user input
    os.system(f"rm temp_files/{filename}")
    print(f"Deleted {filename}")

if __name__ == "__main__":
    delete_user_file()
