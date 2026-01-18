import os
import subprocess

class OrderProcessor:
    def process_shipping(self, order_id, destination_code):
        print(f"Processing shipping for Order #{order_id}")
        
        command = ["./legacy_scripts/ship_order.sh", str(order_id), destination_code]
        
        return subprocess.run(command, capture_output=True, text=True).returncode

    def generate_invoice_pdf(self, order_id):
        command = ["wkhtmltopdf", f"http://localhost/orders/{order_id}", "invoice.pdf"]
        return subprocess.run(command, capture_output=True, text=True).returncode