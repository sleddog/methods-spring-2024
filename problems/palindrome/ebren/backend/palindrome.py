from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../')

def is_palindrome(s):
    cleanString = ''.join(char.lower() for char in s if char.isalnum())
    if len(cleanString) <= 1:
        return True
    left = 0
    right = len(cleanString) - 1
    while left < right:
        if cleanString[left] != cleanString[right]:
            return False
        left += 1
        right -= 1
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-palindrome', methods=['POST'])
def check_palindrome():
    data = request.get_json()
    try:
        palindrome = data['palindrome']
        if palindrome is not None:
            if is_palindrome(palindrome):
                return "true"
            else:
                return "false"
        else:
            return "Invalid input"
    except Exception as e:
        return f"The error: {str(e)}"
    

if __name__ == "__main__":
    app.run(debug=True)
