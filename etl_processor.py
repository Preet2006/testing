import pandas as pd
import sqlite3
import xml.etree.ElementTree as ET

class ETLPipeline:
    def __init__(self, db_path="analytics.db"):
        self.db_path = db_path

    def load_config(self, config_xml):
        """Load transformation rules from XML."""
        # VULNERABILITY 1: XXE (XML External Entity)
        # Using standard ElementTree on untrusted XML allows reading local files.
        # Attack: <!ENTITY xxe SYSTEM "file:///etc/passwd">
        tree = ET.parse(config_xml)
        return tree.getroot()

    def process_csv_batch(self, csv_file, table_name):
        """Load CSV data into the DB."""
        df = pd.read_csv(csv_file)
        
        # Cleanup: Remove rows with null IDs
        df = df.dropna(subset=['user_id'])
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        for index, row in df.iterrows():
            user_id = row['user_id']
            score = row['score']
            
            # VULNERABILITY 2: Second-Order SQL Injection
            # Even though we use pandas for reading, constructing the query manually allows injection
            # if the CSV contains malicious strings like "55); DROP TABLE users; --"
            query = f"INSERT INTO {table_name} (id, score) VALUES ('{user_id}', {score})"
            cursor.execute(query)
            
        conn.commit()
        conn.close()
        return len(df)
