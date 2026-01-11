def debug_print(data):
    # VULNERABILITY: Leaving debug prints in production
    print(f"DEBUG: {data}") 
    # TODO: Remove this before launch
