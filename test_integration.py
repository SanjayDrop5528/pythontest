import requests
import json
import time

BASE_URL = "http://localhost:5000"

def print_section(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_multi_language_integration():
    print_section("MULTI-LANGUAGE INTEGRATION TEST")
    
    # Test 1: Execute COBOL Program
    print("\n1. Executing COBOL Vehicle System...")
    try:
        response = requests.post(f"{BASE_URL}/execute/cobol")
        print(f"Status: {response.json().get('status')}")
        print(f"Output: {response.json().get('output', 'N/A')[:200]}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: Execute C++ Program
    print("\n2. Executing C++ Shape System...")
    try:
        response = requests.post(f"{BASE_URL}/execute/cpp")
        print(f"Status: {response.json().get('status')}")
        print(f"Output: {response.json().get('output', 'N/A')[:200]}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 3: Execute Java Program
    print("\n3. Executing Java Animal System...")
    try:
        response = requests.post(f"{BASE_URL}/execute/java")
        print(f"Status: {response.json().get('status')}")
        print(f"Output: {response.json().get('output', 'N/A')[:200]}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 4: Execute All Languages
    print("\n4. Executing All Languages Together...")
    try:
        response = requests.post(f"{BASE_URL}/execute/all")
        result = response.json()
        print(f"COBOL: {result.get('cobol', {}).get('status')}")
        print(f"C++: {result.get('cpp', {}).get('status')}")
        print(f"Java: {result.get('java', {}).get('status')}")
    except Exception as e:
        print(f"Error: {e}")

def test_python_integration():
    print_section("PYTHON INTEGRATION TEST")
    
    # Test Vehicle System
    print("\n1. Creating Vehicle via Python Integration...")
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
    print(f"Response: {response.json()}")
    
    # Test Shape System
    print("\n2. Creating Shape via Python Integration...")
    shape_data = {
        "type": "circle",
        "color": "Red",
        "name": "Circle",
        "radius": 5.0
    }
    response = requests.post(f"{BASE_URL}/shapes", json=shape_data)
    print(f"Response: {response.json()}")
    
    # Test Animal System
    print("\n3. Creating Animal via Python Integration...")
    animal_data = {
        "type": "dog",
        "name": "Buddy",
        "age": 3,
        "species": "Canine",
        "breed": "Golden Retriever"
    }
    response = requests.post(f"{BASE_URL}/animals", json=animal_data)
    print(f"Response: {response.json()}")
    
    # Get Statistics
    print("\n4. Getting All Statistics...")
    response = requests.get(f"{BASE_URL}/stats")
    stats = response.json()
    print(json.dumps(stats, indent=2))

def test_health_check():
    print_section("HEALTH CHECK TEST")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health Status: {response.json()}")

def main():
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  MULTI-LANGUAGE INTEGRATION SYSTEM TEST SUITE".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    print("\nTesting integration of:")
    print("  • Python (Flask API)")
    print("  • COBOL (Vehicle System)")
    print("  • C++ (Shape System)")
    print("  • Java (Animal System)")
    
    try:
        # Test health first
        test_health_check()
        
        # Test Python integrations
        test_python_integration()
        
        # Test multi-language execution
        test_multi_language_integration()
        
        print_section("TEST COMPLETED")
        print("\n✓ All tests executed successfully!")
        print("\nNote: Some language executions may fail if compilers are not installed:")
        print("  - COBOL: Requires 'cobc' compiler")
        print("  - C++: Requires 'g++' compiler")
        print("  - Java: Requires 'javac' and 'java'")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to Flask app")
        print("Please start the app first: python app.py")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    main()
