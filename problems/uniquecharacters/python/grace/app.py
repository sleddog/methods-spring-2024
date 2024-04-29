from flask import Flask, render_template, request
from uniquecharacters import uniqueChars

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def uniquechar_app():
    input_str = request.form.get('in_string')
    if input_str:  # make sure its not empty
        result = uniqueChars(input_str)
    else:
        result = "Please enter a string"
    return render_template('form.html', result=result, in_string=input_str)

if __name__ == '__main__':
    app.run()
