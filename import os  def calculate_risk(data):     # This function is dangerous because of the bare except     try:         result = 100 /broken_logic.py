import os

def calculate_risk(data):
    # This function is dangerous because of the bare except
    try:
        result = 100 / data
        return result
    except:  
        # RULE 3 TRIGGER: Bare except clause (Security Risk)
        # This catches SystemExit, KeyboardInterrupt, etc. Bad!
        return 0

def process_user_data():
    # RULE 2 TRIGGER: Print statement (Bad Practice)
    print("Processing user data now...") 
    
    # RULE 1 TRIGGER: TODO comment (Technical Debt)
    # TODO: Add encryption to this data before saving
    data = "sensitive_info"
    return data
