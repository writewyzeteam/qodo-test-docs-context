"""
Public API endpoints for data access.
"""
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Simulated database
database = {
    'posts': [
        {'id': i, 'title': f'Post {i}', 'content': f'Content {i}'}
        for i in range(1, 101)
    ],
    'users': [
        {'id': i, 'name': f'User {i}', 'email': f'user{i}@example.com'}
        for i in range(1, 51)
    ]
}

# VIOLATION: No rate limiting on public endpoint
@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Get all posts.
    
    VIOLATION: Missing rate limiting as required by security policy.
    See /docs/security/security-policy.md
    """
    return jsonify(database['posts']), 200

# VIOLATION: No rate limiting on search endpoint
@app.route('/api/search', methods=['GET'])
def search():
    """
    Search across posts and users.
    
    VIOLATION: No rate limiting - vulnerable to abuse.
    This endpoint is computationally expensive and should be rate limited.
    """
    query = request.args.get('q', '')
    
    # Expensive operation - searches all posts and users
    results = {
        'posts': [p for p in database['posts'] if query.lower() in p['title'].lower()],
        'users': [u for u in database['users'] if query.lower() in u['name'].lower()]
    }
    
    return jsonify(results), 200

# VIOLATION: Public data endpoint without protection
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by ID.
    
    VIOLATION: Public endpoint with no rate limiting.
    Could be used for user enumeration attacks.
    """
    user = next((u for u in database['users'] if u['id'] == user_id), None)
    
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# VIOLATION: Data export endpoint without rate limiting
@app.route('/api/export', methods=['GET'])
def export_data():
    """
    Export all data (admin endpoint).
    
    CRITICAL VIOLATION: Expensive operation with no rate limiting.
    This could easily be abused to cause resource exhaustion.
    """
    export = {
        'posts': database['posts'],
        'users': database['users'],
        'stats': {
            'total_posts': len(database['posts']),
            'total_users': len(database['users'])
        }
    }
    
    return jsonify(export), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
