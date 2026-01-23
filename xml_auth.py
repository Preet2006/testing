import sys
import xml.etree.ElementTree as ET

def parse_auth_token(xml_data):
    print("Parsing Auth Token...")
    try:
        # VULNERABILITY: XXE (XML External Entity)
        # Standard ElementTree allows entity expansion.
        # Red Team will try to inject <!ENTITY xxe SYSTEM "file:///etc/passwd">
        root = ET.fromstring(xml_data)
        
        user = root.find('user').text
        print(f"Authenticated User: {user}")
        return True
    except Exception as e:
        print(f"Auth Failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_auth_token(sys.argv[1])
    else:
        print("Usage: python xml_auth.py <xml_string>")
