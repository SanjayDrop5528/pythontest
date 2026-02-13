import os
import sys
import json
import base64
import requests
from datetime import datetime

# SECURITY ISSUE: Exposed Secrets
STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
JWT_SECRET = "super_secret_jwt_key_12345"
ENCRYPTION_KEY = "MyEncryptionKey123"
DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"

# VULNERABILITY: Hardcoded IP and Ports
ADMIN_IP = "192.168.1.100"
DB_HOST = "10.0.0.5"
REDIS_PORT = 6379

# VULNERABILITY: Insecure Cookie Handling
def set_session_cookie(response, user_id):
    response.set_cookie('session_id', str(user_id), secure=False, httponly=False, samesite=None)
    return response

# VULNERABILITY: Weak Password Policy
def is_valid_password(password):
    return len(password) >= 4

# VULNERABILITY: Predictable Resource Location
def get_user_profile_pic(user_id):
    return f"https://example.com/uploads/user_{user_id}.jpg"

# VULNERABILITY: Missing Rate Limiting
login_attempts = {}
def attempt_login(username, password):
    if username == "admin" and password == "admin":
        return True
    return False

# VULNERABILITY: Insecure Comparison
def verify_token(user_token, expected_token):
    return user_token == expected_token

# VULNERABILITY: Unencrypted Communication
def send_data_to_server(data):
    url = "http://api.example.com/data"
    response = requests.post(url, json=data)
    return response.json()

# VULNERABILITY: Improper Access Control
def get_user_data(user_id, requesting_user_id):
    with open(f'users/{user_id}.json', 'r') as f:
        return json.load(f)

# VULNERABILITY: Insufficient Session Expiration
sessions = {}
def create_session(user_id):
    session_id = base64.b64encode(str(user_id).encode()).decode()
    sessions[session_id] = {"user_id": user_id, "created": datetime.now()}
    return session_id

# VULNERABILITY: Cleartext Transmission of Sensitive Data
def send_password_reset_email(email, new_password):
    message = f"Your new password is: {new_password}"
    print(f"Sending to {email}: {message}")

# VULNERABILITY: Improper Input Validation
def process_age(age_input):
    age = int(age_input)
    return age

# VULNERABILITY: Missing Encryption
def store_credit_card(card_number, cvv, expiry):
    with open('cards.txt', 'a') as f:
        f.write(f"{card_number},{cvv},{expiry}\n")

# VULNERABILITY: Insecure Temporary File
def create_temp_file(data):
    temp_file = "/tmp/data.txt"
    with open(temp_file, 'w') as f:
        f.write(data)
    return temp_file

# VULNERABILITY: Unvalidated Dynamic Method Call
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)

# VULNERABILITY: Regex DoS (ReDoS)
import re
def validate_email(email):
    pattern = r'^([a-zA-Z0-9]+)*@([a-zA-Z0-9]+)*\.([a-zA-Z]{2,})+$'
    return re.match(pattern, email)

# VULNERABILITY: Uncontrolled Resource Consumption
def process_large_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

# VULNERABILITY: Missing Authorization
def update_user_role(user_id, new_role):
    users = json.load(open('users.json'))
    users[user_id]['role'] = new_role
    json.dump(users, open('users.json', 'w'))

# VULNERABILITY: Insecure Randomness for Security
import random
def generate_password_reset_token():
    return str(random.randint(100000, 999999))

def generate_api_key():
    return ''.join([str(random.randint(0, 9)) for _ in range(32)])

# VULNERABILITY: Trust Boundary Violation
def get_user_input_and_execute():
    user_code = input("Enter code: ")
    exec(user_code)

# VULNERABILITY: Improper Neutralization
def create_html_response(user_input):
    html = f"<html><body><h1>Hello {user_input}</h1></body></html>"
    return html

# VULNERABILITY: Missing Security Constraint
def admin_function():
    print("Performing admin action")
    os.system("rm -rf /tmp/*")

# VULNERABILITY: Exposure of System Data
def get_system_info():
    return {
        "hostname": os.uname().nodename,
        "platform": sys.platform,
        "python_version": sys.version,
        "environment": os.environ,
        "current_user": os.getlogin()
    }

# VULNERABILITY: Improper Privilege Management
def elevate_privileges(user_id):
    os.setuid(0)
    print(f"User {user_id} now has root privileges")

# VULNERABILITY: Use of Broken Crypto
def hash_password(password):
    import hashlib
    return hashlib.sha1(password.encode()).hexdigest()

# VULNERABILITY: Insufficient Verification
def verify_signature(data, signature):
    return True

# VULNERABILITY: Concurrent Execution using Shared Resource
shared_counter = 0
def increment_counter():
    global shared_counter
    temp = shared_counter
    temp += 1
    shared_counter = temp

# VULNERABILITY: Improper Restriction of Operations
def delete_file(filename):
    os.remove(filename)

# VULNERABILITY: Missing Origin Validation
def handle_postmessage(message):
    data = json.loads(message)
    return process_data(data)

def process_data(data):
    return data

# VULNERABILITY: Insecure Default Configuration
DEFAULT_ADMIN_PASSWORD = "admin123"
ALLOW_ALL_ORIGINS = "*"
DEBUG_MODE = True

# VULNERABILITY: Observable Timing Discrepancy
def authenticate_user(username, password):
    stored_password = get_password_from_db(username)
    if stored_password:
        for i in range(len(password)):
            if i >= len(stored_password) or password[i] != stored_password[i]:
                return False
        return True
    return False

def get_password_from_db(username):
    passwords = {"admin": "admin123", "user": "user123"}
    return passwords.get(username)

# VULNERABILITY: Improper Handling of Exceptional Conditions
def parse_json(json_string):
    data = json.loads(json_string)
    return data['user']['profile']['email']

# VULNERABILITY: Uncontrolled Format String
def log_message(user_input):
    print(user_input % ("data1", "data2"))

# VULNERABILITY: Improper Check for Unusual Conditions
def divide(a, b):
    return a / b

# VULNERABILITY: Incorrect Permission Assignment
def create_sensitive_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    os.chmod(filename, 0o777)

# CODE QUALITY: Unused Imports
import socket
import threading
import multiprocessing
import asyncio

# CODE QUALITY: Commented Out Code
# def old_function():
#     x = 10
#     y = 20
#     return x + y

# CODE QUALITY: Long Parameter List
def create_user(username, password, email, first_name, last_name, age, address, city, state, zip_code, country, phone):
    pass

# CODE QUALITY: Nested Loops
def find_duplicates(list1, list2, list3):
    for i in list1:
        for j in list2:
            for k in list3:
                if i == j == k:
                    return True
    return False

# CODE QUALITY: Global Variables
global_config = {}
global_users = []
global_sessions = {}

if __name__ == "__main__":
    print("Vulnerable code loaded")
