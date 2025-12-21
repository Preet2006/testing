import time
import threading

# A shared bank balance
balance = 0

def deposit(amount):
    global balance
    # LOGIC BUG: This is not thread-safe!
    # Reading and writing to a shared variable without a Lock
    # will cause data loss if two threads run this at the same time.
    
    current_val = balance
    time.sleep(0.1) # Simulate slow database
    balance = current_val + amount

def run_transactions():
    t1 = threading.Thread(target=deposit, args=(100,))
    t2 = threading.Thread(target=deposit, args=(100,))
    
    t1.start()
    t2.start()
