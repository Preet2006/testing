import subprocess
def process_payment(order_id):
    print("Processing payment...")
    subprocess.run(["ping", "-c", "1", order_id], capture_output=True, text=True)