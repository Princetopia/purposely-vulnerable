"""
Purposely Vulnerable Application - DO NOT USE IN PRODUCTION
This file contains intentional security vulnerabilities for testing purposes.
"""
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def init_db():
    """Initialize a simple SQLite database"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin@example.com', 'admin')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'user', 'user@example.com', 'user')")
    conn.commit()
    conn.close()

@app.route('/user/<username>')
def get_user(username):
    """
    VULNERABLE: SQL Injection vulnerability
    This endpoint is intentionally vulnerable to SQL injection attacks.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # FIXED: Using parameterized query to prevent SQL injection
    # The ? placeholder ensures username is properly escaped
    query = "SELECT * FROM users WHERE username = ?"

    cursor.execute(query, (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return jsonify({
            'id': result[0],
            'username': result[1],
            'email': result[2],
            'role': result[3]
        })
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/search')
def search_users():
    """
    VULNERABLE: SQL Injection vulnerability via query parameter
    """
    search_term = request.args.get('q', '')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # FIXED: Using parameterized query to prevent SQL injection
    query = "SELECT username, email FROM users WHERE username LIKE ?"
    
    cursor.execute(query, (f'%{search_term}%',))
    results = cursor.fetchall()
    conn.close()
    
    return jsonify([{'username': r[0], 'email': r[1]} for r in results])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

