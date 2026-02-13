import os
import sys
import json
import pickle
import subprocess
import sqlite3
from flask import Flask, request, jsonify, render_template_string
from vehicle_integration import VehicleIntegration
from shape_integration import ShapeIntegration
from animal_integration import AnimalIntegration

app = Flask(__name__)

# SECURITY ISSUE: Hardcoded credentials
DB_USER = "admin"
DB_PASSWORD = "admin123"
SECRET_KEY = "my_secret_key_12345"
API_KEY = "sk_test_1234567890abcdef"

app.config['SECRET_KEY'] = SECRET_KEY

# Initialize integrations
vehicle_system = VehicleIntegration()
shape_system = ShapeIntegration()
animal_system = AnimalIntegration()

# VULNERABILITY: Command execution for multi-language integration
def execute_cobol_program():
    try:
        result = subprocess.run(['cobc', '-x', 'Vehicle.cbl'], capture_output=True, text=True, timeout=10)
        return {"status": "executed", "output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

def execute_cpp_program():
    try:
        subprocess.run(['g++', 'Shape.cpp', '-o', 'shape_exec'], capture_output=True, timeout=10)
        result = subprocess.run(['./shape_exec'], capture_output=True, text=True, timeout=10)
        return {"status": "executed", "output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

def execute_java_program():
    try:
        subprocess.run(['javac', 'Animal.java'], capture_output=True, timeout=10)
        result = subprocess.run(['java', 'AnimalDemo'], capture_output=True, text=True, timeout=10)
        return {"status": "executed", "output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# VULNERABILITY: SQL Injection - No parameterized queries
def init_db():
    conn = sqlite3.connect('app_data.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, action TEXT, data TEXT)")
    cursor.execute(f"INSERT OR IGNORE INTO users VALUES (1, '{DB_USER}', '{DB_PASSWORD}', 'admin')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    # VULNERABILITY: XSS - No input sanitization
    user = request.args.get('user', 'Guest')
    html = f"""
    <html>
        <head><title>Integration System</title></head>
        <body>
            <h1>Welcome {user}!</h1>
            <h2>Multi-Language Integration System</h2>
            <ul>
                <li><a href="/vehicles">Vehicle System (COBOL)</a></li>
                <li><a href="/shapes">Shape System (C++)</a></li>
                <li><a href="/animals">Animal System (Java)</a></li>
                <li><a href="/stats">Statistics</a></li>
                <li><a href="/admin">Admin Panel</a></li>
            </ul>
            <h3>Execute Native Programs</h3>
            <ul>
                <li><form action="/execute/cobol" method="post"><button>Run COBOL</button></form></li>
                <li><form action="/execute/cpp" method="post"><button>Run C++</button></form></li>
                <li><form action="/execute/java" method="post"><button>Run Java</button></form></li>
                <li><form action="/execute/all" method="post"><button>Run All</button></form></li>
            </ul>
        </body>
    </html>
    """
    return render_template_string(html)

# VULNERABILITY: SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    conn = sqlite3.connect('app_data.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({"status": "success", "api_key": API_KEY, "secret": SECRET_KEY})
    return jsonify({"status": "failed"})

# VULNERABILITY: Command Injection
@app.route('/execute', methods=['POST'])
def execute_command():
    cmd = request.json.get('command')
    result = os.system(cmd)
    return jsonify({"result": result})

# VULNERABILITY: Path Traversal
@app.route('/file/<path:filename>')
def get_file(filename):
    file_path = f"data/{filename}"
    with open(file_path, 'r') as f:
        content = f.read()
    return content

# VULNERABILITY: Insecure Deserialization
@app.route('/load_data', methods=['POST'])
def load_data():
    data = request.data
    obj = pickle.loads(data)
    return jsonify({"loaded": str(obj)})

@app.route('/vehicles', methods=['GET', 'POST'])
def vehicles():
    if request.method == 'POST':
        data = request.json
        vehicle_type = data.get('type')
        
        if vehicle_type == 'car':
            vehicle = vehicle_system.create_car(data)
        elif vehicle_type == 'truck':
            vehicle = vehicle_system.create_truck(data)
        else:
            vehicle = vehicle_system.create_motorcycle(data)
        
        vehicles = vehicle_system.load_vehicles()
        vehicles.append(vehicle)
        vehicle_system.save_vehicles(vehicles)
        
        return jsonify({"status": "created", "vehicle": vehicle})
    
    vehicles = vehicle_system.load_vehicles()
    stats = vehicle_system.get_vehicle_stats(vehicles)
    return jsonify({"vehicles": vehicles, "stats": stats})

@app.route('/shapes', methods=['GET', 'POST'])
def shapes():
    if request.method == 'POST':
        data = request.json
        shape_type = data.get('type')
        
        if shape_type == 'circle':
            shape = shape_system.create_circle(data)
        elif shape_type == 'rectangle':
            shape = shape_system.create_rectangle(data)
        else:
            shape = shape_system.create_triangle(data)
        
        shapes = shape_system.load_shapes()
        shapes.append(shape)
        shape_system.save_shapes(shapes)
        
        return jsonify({"status": "created", "shape": shape})
    
    shapes = shape_system.load_shapes()
    stats = shape_system.get_shape_stats(shapes)
    return jsonify({"shapes": shapes, "stats": stats})

@app.route('/animals', methods=['GET', 'POST'])
def animals():
    if request.method == 'POST':
        data = request.json
        animal_type = data.get('type')
        
        if animal_type == 'dog':
            animal = animal_system.create_dog(data)
        elif animal_type == 'cat':
            animal = animal_system.create_cat(data)
        else:
            animal = animal_system.create_bird(data)
        
        animals = animal_system.load_animals()
        animals.append(animal)
        animal_system.save_animals(animals)
        
        return jsonify({"status": "created", "animal": animal})
    
    animals = animal_system.load_animals()
    stats = animal_system.get_animal_stats(animals)
    return jsonify({"animals": animals, "stats": stats})

# VULNERABILITY: Exposed admin panel without authentication
@app.route('/admin')
def admin():
    conn = sqlite3.connect('app_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    return jsonify({"users": users, "db_password": DB_PASSWORD})

# VULNERABILITY: Information disclosure
@app.route('/debug')
def debug():
    return jsonify({
        "env": dict(os.environ),
        "secret_key": SECRET_KEY,
        "api_key": API_KEY,
        "db_user": DB_USER,
        "db_password": DB_PASSWORD
    })

# VULNERABILITY: SSRF
@app.route('/fetch', methods=['POST'])
def fetch_url():
    url = request.json.get('url')
    result = subprocess.check_output(['curl', url])
    return result

# VULNERABILITY: Weak cryptography
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data')
    encrypted = ''.join([chr(ord(c) + 1) for c in data])
    return jsonify({"encrypted": encrypted})

@app.route('/stats')
def all_stats():
    vehicles = vehicle_system.load_vehicles()
    shapes = shape_system.load_shapes()
    animals = animal_system.load_animals()
    
    return jsonify({
        "vehicles": vehicle_system.get_vehicle_stats(vehicles),
        "shapes": shape_system.get_shape_stats(shapes),
        "animals": animal_system.get_animal_stats(animals)
    })

# Execute native language programs
@app.route('/execute/cobol', methods=['POST'])
def run_cobol():
    result = execute_cobol_program()
    return jsonify(result)

@app.route('/execute/cpp', methods=['POST'])
def run_cpp():
    result = execute_cpp_program()
    return jsonify(result)

@app.route('/execute/java', methods=['POST'])
def run_java():
    result = execute_java_program()
    return jsonify(result)

@app.route('/execute/all', methods=['POST'])
def run_all_languages():
    return jsonify({
        "cobol": execute_cobol_program(),
        "cpp": execute_cpp_program(),
        "java": execute_java_program()
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "timestamp": str(subprocess.check_output(['date']).decode())})

# VULNERABILITY: No rate limiting, no CSRF protection
if __name__ == '__main__':
    # Execute integration files main functions before starting app
    print("\n=== Initializing Vehicle Integration (COBOL) ===")
    from vehicle_integration import main as vehicle_main
    vehicle_main()
    
    print("\n=== Initializing Shape Integration (C++) ===")
    from shape_integration import main as shape_main
    shape_main()
    
    print("\n=== Initializing Animal Integration (Java) ===")
    from animal_integration import main as animal_main
    animal_main()
    
    print("\n=== Starting Flask Application ===")
    # VULNERABILITY: Debug mode enabled in production
    app.run(host='0.0.0.0', port=5000, debug=True)
