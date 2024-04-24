from flask import Flask, jsonify
import sum 

app = Flask(__name__)

@app.route('/sumofprimes', methods=['POST'])
def runSum():
    number = int(request.form['numInput'])
    result = sum(number)
    return jsonify(result)

if __name__ = '__main__' :
    app.run(debug=True)