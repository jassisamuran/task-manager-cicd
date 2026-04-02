from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_age', methods=['POST'])
def check_age():
    data = request.get_json()
    age = data.get('age')

    if age is None or not isinstance(age, int):
        return jsonify({'error': 'Age is required and must be an integer.'}), 400

    if age >= 18:
        return jsonify({'message': 'User is eligible'}), 200
    else:
        return jsonify({'message': 'User is not eligible'}), 200

if __name__ == '__main__':
    app.run(debug=True)