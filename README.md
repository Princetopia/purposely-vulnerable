# purposely-vulnerable

⚠️ **WARNING: This repository contains intentionally vulnerable code!** ⚠️

## About

This is a test repository that contains **intentional security vulnerabilities** for testing security scanning and automated fixing tools. 

**DO NOT:**
- Use this code in production
- Deploy this application anywhere
- Copy code patterns from this repository

**Purpose:**
- Testing GitHub Code Scanning with CodeQL
- Testing automated security fix tools
- Demonstrating common vulnerability patterns

## Vulnerabilities

This repository contains examples of:
- **SQL Injection** - String concatenation in SQL queries
- Unsafe query parameter handling
- Missing input validation

## Setup

This is a Python Flask application managed with Poetry.

```bash
# Install dependencies
poetry install

# Run the vulnerable app (for testing only!)
poetry run python vulnerable_app.py
```

## Security Scanning

This repository uses:
- **CodeQL** - Automated code scanning for security vulnerabilities
- **Claude Security Autofixer** - AI-powered automated vulnerability fixing

The CodeQL workflow runs automatically on push and pull requests, as well as weekly.

## Testing the Autofixer

To test the security autofixer:

1. Wait for CodeQL to detect vulnerabilities (check Security tab)
2. Note the alert number
3. Go to Actions > Test Security Autofixer
4. Run workflow manually with the alert number
5. Review the generated PR with the fix

## License

This is test code for educational and testing purposes only.
