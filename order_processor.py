import os
import subprocess

class OrderProcessor:
    def process_shipping(self, order_id, destination_code):
        print(f"Processing shipping for Order #{order_id}")
        
        # VULNERABILITY: Command Injection
        # If destination_code is "; rm -rf /", the server is destroyed.
        # This simulates calling a legacy shipping script.
        command = f"./legacy_scripts/ship_order.sh {order_id} {destination_code}"
        
        # os.system executes the command in a shell
        return os.system(command)

    def generate_invoice_pdf(self, order_id):
        # VULNERABILITY: Another Command Injection vector
        # Using subprocess.call with shell=True is dangerous
        subprocess.call(f"wkhtmltopdf http://localhost/orders/{order_id} invoice.pdf", shell=True)
