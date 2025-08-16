import pyodbc
import json
import os

# Load config.json
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path, 'r') as f:
    config = json.load(f)

def get_connection():
    db = config["database"]
    conn_str = (
        f"DRIVER={{{db['driver']}}};"
        f"SERVER={db['server']};"
        f"DATABASE={db['database']};"
        f"UID={db['username']};"
        f"PWD={db['password']};"
        f"Trusted_Connection={db['trusted_connection']};"
        f"Encrypt={db['encrypt']};"
        f"TrustServerCertificate={db['trust_server_certificate']};"
        f"MARS_Connection={db['multiple_active_result_sets']};"
        f"Connection Timeout={db['command_timeout']};"
    )
    return pyodbc.connect(conn_str)