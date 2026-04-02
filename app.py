from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Generate JWT token
@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not 'username' in auth or not 'password' in auth:
        return jsonify({'message': 'Could not verify'}), 401
    # Here you would normally verify the username and password
    token = jwt.encode({'user': auth['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    refresh_token = jwt.encode({'user': auth['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)}, app.config['SECRET_KEY'])
    return jsonify({'token': token, 'refresh_token': refresh_token})

# Refresh JWT token
@app.route('/refresh', methods=['POST'])
def refresh():
    auth = request.json
    if not auth or not 'refresh_token' in auth:
        return jsonify({'message': 'Could not verify'}), 401
    try:
        jwt.decode(auth['refresh_token'], app.config['SECRET_KEY'])
        new_token = jwt.encode({'user': auth['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': new_token})
    except:
        return jsonify({'message': 'Token is invalid'}), 401

if __name__ == '__main__':
    app.run(debug=True)