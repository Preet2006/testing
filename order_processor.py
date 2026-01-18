import os
import subprocess

class OrderProcessor:
    def process_shipping(self, order_id, destination_code):
        print(f"Processing shipping for Order #{order_id}")
        
        # Using subprocess.run with a list of arguments to prevent command injection
        return subprocess.run(["./legacy_scripts/ship_order.sh", str(order_id), destination_code], capture_output=True, text=True)

    def generate_invoice_pdf(self, order_id):
        # Using subprocess.run with a list of arguments to prevent command injection
        subprocess.run(["wkhtmltopdf", f"http://localhost/orders/{order_id}", "invoice.pdf"], capture_output=True, text=True)