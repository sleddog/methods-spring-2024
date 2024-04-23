from palindrome import isPalindrome
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # return 'hello'
    return open('index.html').read()

@app.route('/palindrome', methods=['POST'])
def palidrome_post():
    s = str(request.form.get('string'))
    result = isPalindrome(s, 0, len(s)-1)
    
    if result:
        return s + " is a palindrome!"
    else:
        return s + " is NOT a palindrome!"

if __name__ == '__main__':
    app.run()