import os
def process_payment(order_id):
    print("Processing payment...")
    # VULNERABILITY: Executing shell command with user input
    os.system("ping -c 1 " + order_id)
