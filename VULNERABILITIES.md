# Security Vulnerabilities and Issues Documentation

## Files with Vulnerabilities

### 1. vulnerable_code.py
Contains 40+ security vulnerabilities and code quality issues

### 2. security_issues.py
Contains 35+ additional security vulnerabilities

### 3. app.py
Flask application with 13+ vulnerabilities integrated with COBOL, C++, and Java systems

## Complete Vulnerability List

### Critical Vulnerabilities

1. **SQL Injection** (CWE-89)
   - Files: vulnerable_code.py, app.py
   - Lines: Multiple locations
   - Risk: CRITICAL

2. **Command Injection** (CWE-78)
   - Files: vulnerable_code.py, app.py
   - Risk: CRITICAL

3. **Code Injection** (CWE-94)
   - Files: vulnerable_code.py, security_issues.py
   - Risk: CRITICAL

4. **Insecure Deserialization** (CWE-502)
   - Files: vulnerable_code.py, app.py
   - Risk: CRITICAL

5. **Hardcoded Credentials** (CWE-798)
   - Files: All files
   - Risk: CRITICAL

6. **Hardcoded Cryptographic Keys** (CWE-321)
   - Files: vulnerable_code.py, security_issues.py
   - Risk: CRITICAL

### High Vulnerabilities

7. **Path Traversal** (CWE-22)
   - Files: vulnerable_code.py, app.py
   - Risk: HIGH

8. **Cross-Site Scripting (XSS)** (CWE-79)
   - Files: app.py, security_issues.py
   - Risk: HIGH

9. **Server-Side Request Forgery (SSRF)** (CWE-918)
   - Files: vulnerable_code.py, app.py
   - Risk: HIGH

10. **XML External Entity (XXE)** (CWE-611)
    - Files: vulnerable_code.py
    - Risk: HIGH

11. **YAML Deserialization** (CWE-502)
    - Files: vulnerable_code.py
    - Risk: HIGH

12. **Unrestricted File Upload** (CWE-434)
    - Files: vulnerable_code.py
    - Risk: HIGH

13. **Missing Authentication** (CWE-306)
    - Files: vulnerable_code.py, app.py
    - Risk: HIGH

14. **Missing Authorization** (CWE-862)
    - Files: security_issues.py
    - Risk: HIGH

15. **Information Disclosure** (CWE-200)
    - Files: All files
    - Risk: HIGH

### Medium Vulnerabilities

16. **Weak Cryptography - MD5** (CWE-327)
    - Files: vulnerable_code.py, security_issues.py
    - Risk: MEDIUM

17. **Weak Cryptography - SHA1** (CWE-327)
    - Files: security_issues.py
    - Risk: MEDIUM

18. **Insecure Random** (CWE-330)
    - Files: vulnerable_code.py, security_issues.py
    - Risk: MEDIUM

19. **Race Condition** (CWE-race)
    - Files: vulnerable_code.py, security_issues.py
    - Risk: MEDIUM

20. **Timing Attack** (CWE-208)
    - Files: vulnerable_code.py, security_issues.py
    - Risk: MEDIUM

21. **Insecure Direct Object Reference** (CWE-639)
    - Files: vulnerable_code.py
    - Risk: MEDIUM

22. **Unvalidated Redirect** (CWE-601)
    - Files: vulnerable_code.py
    - Risk: MEDIUM

23. **Mass Assignment** (CWE-915)
    - Files: vulnerable_code.py
    - Risk: MEDIUM

24. **Missing Rate Limiting** (CWE-770)
    - Files: app.py, security_issues.py
    - Risk: MEDIUM

25. **No CSRF Protection** (CWE-352)
    - Files: app.py
    - Risk: MEDIUM

26. **Insecure Cookie Handling** (CWE-614)
    - Files: security_issues.py
    - Risk: MEDIUM

27. **Cleartext Storage** (CWE-312)
    - Files: vulnerable_code.py, security_issues.py
    - Risk: MEDIUM

28. **Cleartext Transmission** (CWE-319)
    - Files: security_issues.py
    - Risk: MEDIUM

29. **Improper Certificate Validation** (CWE-295)
    - Files: vulnerable_code.py
    - Risk: MEDIUM

30. **Weak Password Policy** (CWE-521)
    - Files: security_issues.py
    - Risk: MEDIUM

### Low Vulnerabilities

31. **Missing Security Headers** (CWE-693)
    - Files: vulnerable_code.py
    - Risk: LOW

32. **Insufficient Logging** (CWE-778)
    - Files: vulnerable_code.py
    - Risk: LOW

33. **Sensitive Data in Logs** (CWE-532)
    - Files: vulnerable_code.py
    - Risk: LOW

34. **Debug Mode Enabled** (CWE-489)
    - Files: app.py, vulnerable_code.py
    - Risk: LOW

35. **Directory Listing** (CWE-548)
    - Files: vulnerable_code.py
    - Risk: LOW

### Code Quality Issues

36. **Dead Code**
37. **Duplicate Code**
38. **Complex Functions** (High Cyclomatic Complexity)
39. **Magic Numbers**
40. **Unused Imports**
41. **Commented Out Code**
42. **Long Parameter Lists**
43. **Nested Loops**
44. **Global Variables**
45. **Missing Error Handling**
46. **Improper Exception Handling**

## Testing Instructions

### Run Security Scanners

```bash
# Install security tools
pip install bandit safety semgrep

# Run Bandit
bandit -r . -f json -o bandit_report.json

# Run Safety
safety check --json > safety_report.json

# Run Semgrep
semgrep --config=auto --json -o semgrep_report.json .
```

### Manual Testing

```bash
# Start the Flask app
python app.py

# Run test script
python test_app.py
```

## Vulnerability Categories

- **Injection Flaws**: SQL, Command, Code, LDAP, XPath
- **Broken Authentication**: Weak passwords, insecure sessions
- **Sensitive Data Exposure**: Hardcoded secrets, cleartext storage
- **XML/YAML Issues**: XXE, unsafe deserialization
- **Broken Access Control**: Missing auth, IDOR
- **Security Misconfiguration**: Debug mode, default passwords
- **Cross-Site Scripting**: Reflected, Stored
- **Insecure Deserialization**: Pickle, YAML
- **Using Components with Known Vulnerabilities**
- **Insufficient Logging & Monitoring**

## OWASP Top 10 Coverage

✅ A01:2021 - Broken Access Control
✅ A02:2021 - Cryptographic Failures
✅ A03:2021 - Injection
✅ A04:2021 - Insecure Design
✅ A05:2021 - Security Misconfiguration
✅ A06:2021 - Vulnerable and Outdated Components
✅ A07:2021 - Identification and Authentication Failures
✅ A08:2021 - Software and Data Integrity Failures
✅ A09:2021 - Security Logging and Monitoring Failures
✅ A10:2021 - Server-Side Request Forgery

## Disclaimer

These files contain intentional security vulnerabilities for:
- Security testing
- SAST/DAST tool validation
- Security training
- Penetration testing practice

**DO NOT USE IN PRODUCTION**
