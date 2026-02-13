# Multi-Language Integration System

## Overview
This Flask application integrates three different language systems:
- **Vehicle System** (COBOL integration)
- **Shape System** (C++ integration)  
- **Animal System** (Java integration)

## Setup

1. Install dependencies:
```bash
pip install -r requirements_app.txt
```

2. Run the application:
```bash
python app.py
```

3. Test the application:
```bash
python test_app.py
```

## API Endpoints

### Integration Endpoints
- `GET /` - Home page
- `GET/POST /vehicles` - Vehicle management (COBOL)
- `GET/POST /shapes` - Shape management (C++)
- `GET/POST /animals` - Animal management (Java)
- `GET /stats` - Get all statistics

### Admin Endpoints
- `POST /login` - User login
- `GET /admin` - Admin panel
- `GET /debug` - Debug information
- `POST /execute` - Execute commands
- `GET /file/<filename>` - File access
- `POST /load_data` - Load serialized data
- `POST /fetch` - Fetch URL
- `POST /encrypt` - Encrypt data

## Security Vulnerabilities (Intentional for Testing)

### 1. Hardcoded Credentials
- **Location**: Lines 13-16
- **Issue**: Credentials stored in source code
- **Risk**: HIGH

### 2. SQL Injection
- **Location**: `/login` endpoint (Line 48)
- **Issue**: No parameterized queries
- **Risk**: CRITICAL
- **Example**: `username: admin' OR '1'='1`

### 3. Cross-Site Scripting (XSS)
- **Location**: `/` endpoint (Line 32)
- **Issue**: No input sanitization
- **Risk**: HIGH
- **Example**: `/?user=<script>alert('XSS')</script>`

### 4. Command Injection
- **Location**: `/execute` endpoint (Line 60)
- **Issue**: Direct OS command execution
- **Risk**: CRITICAL
- **Example**: `{"command": "rm -rf /"}`

### 5. Path Traversal
- **Location**: `/file/<filename>` endpoint (Line 66)
- **Issue**: No path validation
- **Risk**: HIGH
- **Example**: `/file/../../../etc/passwd`

### 6. Insecure Deserialization
- **Location**: `/load_data` endpoint (Line 73)
- **Issue**: Using pickle.loads on user input
- **Risk**: CRITICAL

### 7. Information Disclosure
- **Location**: `/debug` endpoint (Line 145)
- **Issue**: Exposes environment variables and secrets
- **Risk**: CRITICAL

### 8. Missing Authentication
- **Location**: `/admin` endpoint (Line 135)
- **Issue**: No authentication required
- **Risk**: HIGH

### 9. Server-Side Request Forgery (SSRF)
- **Location**: `/fetch` endpoint (Line 155)
- **Issue**: Unvalidated URL fetching
- **Risk**: HIGH

### 10. Weak Cryptography
- **Location**: `/encrypt` endpoint (Line 161)
- **Issue**: Caesar cipher (shift by 1)
- **Risk**: MEDIUM

### 11. Debug Mode in Production
- **Location**: Line 180
- **Issue**: `debug=True` and `host='0.0.0.0'`
- **Risk**: HIGH

### 12. No Rate Limiting
- **Issue**: All endpoints vulnerable to brute force
- **Risk**: MEDIUM

### 13. No CSRF Protection
- **Issue**: State-changing operations without CSRF tokens
- **Risk**: MEDIUM

## Testing Vulnerabilities

Run the test script to see vulnerabilities in action:
```bash
python test_app.py
```

## Disclaimer
This application contains intentional security vulnerabilities for educational and testing purposes only. 
DO NOT use in production or expose to the internet.
