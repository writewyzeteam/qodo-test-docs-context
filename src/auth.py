"""
Authentication module for user login/logout functionality.
"""
from flask import Flask, session, request, jsonify, redirect
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# User database (simplified for testing)
users = {
    'admin@example.com': {'password': 'admin123', 'user_id': 1},
    'user@example.com': {'password': 'user123', 'user_id': 2}
}

@app.route('/login', methods=['POST'])
def login():
    """Handle user login with session-based authentication."""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Validate credentials
    if email in users and users[email]['password'] == password:
        # Store user info in session (VIOLATION: Should use JWT)
        session['user_id'] = users[email]['user_id']
        session['email'] = email
        session['authenticated'] = True
        
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'user_id': users[email]['user_id']
        }), 200
    
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    # Clear session (VIOLATION: Session-based auth)
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

@app.route('/profile', methods=['GET'])
def get_profile():
    """Get current user profile (requires authentication)."""
    # Check session for authentication (VIOLATION: Should verify JWT)
    if not session.get('authenticated'):
        return jsonify({'error': 'Not authenticated'}), 401
    
    user_id = session.get('user_id')
    email = session.get('email')
    
    return jsonify({
        'user_id': user_id,
        'email': email
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
