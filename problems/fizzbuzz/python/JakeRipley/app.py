from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from fizzbuzz import fizzbuzz

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/fizzbuzz', methods=['POST'])
def run_fizzbuzz():
    try:
        number = int(request.form['number'])
        results = fizzbuzz(number)
        return jsonify(results)
    except (ValueError, KeyError):
        return "Invalid input", 400

if __name__ == '__main__':
    app.run(debug=True)
