import os
import pickle
import subprocess
import sqlite3
import hashlib
import random
from flask import Flask, request
import yaml

# SECURITY ISSUE: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
API_SECRET_KEY = "sk_live_51234567890abcdefghijklmnop"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA..."

app = Flask(__name__)

# VULNERABILITY: SQL Injection
def get_user_by_name(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

# VULNERABILITY: Command Injection
def execute_system_command(user_input):
    os.system("ping -c 1 " + user_input)
    subprocess.call("ls " + user_input, shell=True)
    result = eval(user_input)
    return result

# VULNERABILITY: Path Traversal
def read_file(filename):
    path = "/var/data/" + filename
    with open(path, 'r') as f:
        return f.read()

# VULNERABILITY: Insecure Deserialization
def load_user_data(data):
    user_obj = pickle.loads(data)
    return user_obj

# VULNERABILITY: Weak Cryptography
def encrypt_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def simple_encrypt(text):
    return ''.join([chr(ord(c) + 1) for c in text])

# VULNERABILITY: YAML Deserialization
def parse_config(yaml_string):
    config = yaml.load(yaml_string)
    return config

# VULNERABILITY: XXE (XML External Entity)
def parse_xml(xml_data):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_data)
    return root

# VULNERABILITY: Insecure Random
def generate_token():
    return random.randint(1000, 9999)

def generate_session_id():
    return str(random.random())

# VULNERABILITY: Information Disclosure
@app.route('/debug')
def debug_info():
    return {
        "database_password": DATABASE_PASSWORD,
        "api_key": API_SECRET_KEY,
        "aws_key": AWS_ACCESS_KEY,
        "aws_secret": AWS_SECRET_KEY,
        "environment": dict(os.environ)
    }

# VULNERABILITY: No Input Validation
@app.route('/user/<user_id>')
def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()

# VULNERABILITY: Mass Assignment
@app.route('/update_user', methods=['POST'])
def update_user():
    user_data = request.json
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET role='{user_data['role']}', admin={user_data['admin']} WHERE id={user_data['id']}")
    conn.commit()
    return {"status": "updated"}

# VULNERABILITY: Unvalidated Redirect
@app.route('/redirect')
def redirect_user():
    url = request.args.get('url')
    return f"<meta http-equiv='refresh' content='0; url={url}'>"

# VULNERABILITY: SSRF
@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    import urllib.request
    response = urllib.request.urlopen(url)
    return response.read()

# VULNERABILITY: Directory Listing
@app.route('/files')
def list_files():
    files = os.listdir('/var/www/uploads')
    return {"files": files}

# VULNERABILITY: Unrestricted File Upload
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/var/www/uploads/' + file.filename)
    return {"status": "uploaded"}

# VULNERABILITY: Race Condition
balance = 1000
@app.route('/withdraw')
def withdraw():
    global balance
    amount = int(request.args.get('amount'))
    if balance >= amount:
        balance -= amount
        return {"balance": balance}
    return {"error": "insufficient funds"}

# VULNERABILITY: Integer Overflow
def calculate_total(price, quantity):
    return price * quantity

# VULNERABILITY: Buffer Overflow (Python doesn't have this but simulating)
def unsafe_copy(data):
    buffer = [0] * 10
    for i in range(len(data)):
        buffer[i] = data[i]
    return buffer

# VULNERABILITY: Use of Dangerous Functions
def execute_code(code):
    exec(code)
    return eval(code)

# VULNERABILITY: Improper Error Handling
def divide_numbers(a, b):
    return a / b

# VULNERABILITY: Sensitive Data in Logs
def log_user_action(username, password, credit_card):
    print(f"User {username} logged in with password {password} and card {credit_card}")

# VULNERABILITY: No Authentication
@app.route('/admin/delete_user/<user_id>')
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
    return {"status": "deleted"}

# VULNERABILITY: Timing Attack
def check_password(input_password, stored_password):
    if len(input_password) != len(stored_password):
        return False
    for i in range(len(input_password)):
        if input_password[i] != stored_password[i]:
            return False
    return True

# VULNERABILITY: Insecure Direct Object Reference
@app.route('/document/<doc_id>')
def get_document(doc_id):
    with open(f'/documents/{doc_id}.pdf', 'rb') as f:
        return f.read()

# VULNERABILITY: Missing Security Headers
@app.route('/page')
def serve_page():
    return "<html><body>Content</body></html>"

# VULNERABILITY: Cleartext Storage of Sensitive Data
def save_credentials(username, password, ssn):
    with open('credentials.txt', 'w') as f:
        f.write(f"{username}:{password}:{ssn}")

# VULNERABILITY: Improper Certificate Validation
def make_request(url):
    import requests
    response = requests.get(url, verify=False)
    return response.text

# VULNERABILITY: Use of Hard-coded Cryptographic Key
def encrypt_data(data):
    key = b'1234567890123456'
    from Crypto.Cipher import AES
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)

# VULNERABILITY: Insufficient Logging
@app.route('/transfer', methods=['POST'])
def transfer_money():
    amount = request.json.get('amount')
    return {"status": "transferred"}

# VULNERABILITY: Code Injection
def run_template(template_string, context):
    return eval(f"f'{template_string}'")

# VULNERABILITY: LDAP Injection
def ldap_search(username):
    import ldap
    filter_str = f"(uid={username})"
    return filter_str

# VULNERABILITY: XPath Injection
def xpath_query(user_input):
    query = f"//users/user[username='{user_input}']"
    return query

# VULNERABILITY: Null Pointer Dereference
def get_user_email(user):
    return user['email'].lower()

# VULNERABILITY: Memory Leak
cache = {}
@app.route('/cache')
def add_to_cache():
    key = request.args.get('key')
    value = request.args.get('value') * 1000000
    cache[key] = value
    return {"cached": key}

# CODE QUALITY ISSUE: Dead Code
def unused_function():
    x = 10
    y = 20
    z = x + y
    return None

# CODE QUALITY ISSUE: Duplicate Code
def calculate_area_circle(radius):
    return 3.14159 * radius * radius

def calculate_circle_area(r):
    return 3.14159 * r * r

# CODE QUALITY ISSUE: Complex Function
def complex_business_logic(a, b, c, d, e, f, g, h):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            if g > 0:
                                if h > 0:
                                    return a + b + c + d + e + f + g + h
    return 0

# CODE QUALITY ISSUE: Magic Numbers
def calculate_discount(price):
    if price > 100:
        return price * 0.15
    elif price > 50:
        return price * 0.10
    else:
        return price * 0.05

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=None)
