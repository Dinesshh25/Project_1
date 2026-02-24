import json
import os

DB_FILE = 'data.json'

def load_data():
    """Membaca data dari JSON. Jika file tidak ada, buat baru."""
    if not os.path.exists(DB_FILE):
        return {"transactions": []}
    
    with open(DB_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"transactions": []}

def save_data(data):
    """Menyimpan data ke JSON dengan format yang rapi."""
    with open(DB_FILE, 'w') as file:
        json.dump(data, file, indent=4)