from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='.')

def palindrome_check(user_string):
    user_string = user_string.lower()
    for index in range(len(user_string) // 2):
        if user_string[index] != user_string[len(user_string) - index - 1]:
            return False
    return True

@app.route('/script.js')
def script():
    return send_from_directory('.', 'palinScript.js')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def main():
    user_input = request.form.get('input_String', "Nostringdetected")
    result = palindrome_check(user_input)
    if result:
        response = f"{user_input} is a palindrome"
    else:
        response = f"{user_input} is not a palindrome"
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

