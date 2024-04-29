from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

@app.route('/backend', methods=['POST']) 
def palindrome_checker():
    word = request.form.get('word')
    is_pal = is_palindrome(word)
    if is_pal:
        return open('result.html').read()
    else:
        return open('result.html').read()
    
@app.route('/front-end', methods=['GET']) 
def front_end():
    return open('palindrom.html').read()

if __name__ == '__main__':
    app.run(debug=True)