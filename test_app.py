import requests
import json

BASE_URL = "http://localhost:5000"

def test_integration():
    print("=== Testing Multi-Language Integration System ===\n")
    
    # Test 1: Create Vehicle (COBOL Integration)
    print("1. Creating Vehicle...")
    vehicle_data = {
        "type": "car",
        "id": 10001,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2024,
        "color": "Silver",
        "price": 35000.00,
        "doors": 4,
        "fuel_type": "Petrol"
    }
    response = requests.post(f"{BASE_URL}/vehicles", json=vehicle_data)
    print(f"Response: {response.json()}\n")
    
    # Test 2: Create Shape (C++ Integration)
    print("2. Creating Shape...")
    shape_data = {
        "type": "circle",
        "color": "Red",
        "name": "Circle",
        "radius": 5.0
    }
    response = requests.post(f"{BASE_URL}/shapes", json=shape_data)
    print(f"Response: {response.json()}\n")
    
    # Test 3: Create Animal (Java Integration)
    print("3. Creating Animal...")
    animal_data = {
        "type": "dog",
        "name": "Buddy",
        "age": 3,
        "species": "Canine",
        "breed": "Golden Retriever"
    }
    response = requests.post(f"{BASE_URL}/animals", json=animal_data)
    print(f"Response: {response.json()}\n")
    
    # Test 4: Get All Stats
    print("4. Getting Statistics...")
    response = requests.get(f"{BASE_URL}/stats")
    print(f"Stats: {json.dumps(response.json(), indent=2)}\n")

def test_vulnerabilities():
    print("\n=== Testing Security Vulnerabilities ===\n")
    
    # VULNERABILITY 1: SQL Injection
    print("1. SQL Injection Test...")
    sql_payload = {
        "username": "admin' OR '1'='1",
        "password": "anything"
    }
    response = requests.post(f"{BASE_URL}/login", json=sql_payload)
    print(f"SQL Injection Result: {response.json()}\n")
    
    # VULNERABILITY 2: XSS
    print("2. XSS Test...")
    xss_url = f"{BASE_URL}/?user=<script>alert('XSS')</script>"
    print(f"XSS URL: {xss_url}\n")
    
    # VULNERABILITY 3: Path Traversal
    print("3. Path Traversal Test...")
    try:
        response = requests.get(f"{BASE_URL}/file/../app.py")
        print(f"Path Traversal: File accessed\n")
    except:
        print("Path Traversal: Failed\n")
    
    # VULNERABILITY 4: Information Disclosure
    print("4. Information Disclosure Test...")
    response = requests.get(f"{BASE_URL}/debug")
    print(f"Exposed Secrets: {response.json().get('secret_key')}\n")
    
    # VULNERABILITY 5: Exposed Admin Panel
    print("5. Exposed Admin Panel Test...")
    response = requests.get(f"{BASE_URL}/admin")
    print(f"Admin Data: {response.json()}\n")

if __name__ == "__main__":
    print("Starting tests...\n")
    print("Make sure the Flask app is running: python app.py\n")
    
    try:
        test_integration()
        test_vulnerabilities()
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to Flask app. Please start it first with: python app.py")
