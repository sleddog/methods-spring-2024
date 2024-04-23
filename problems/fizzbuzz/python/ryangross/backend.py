from flask import Flask, request, render_template_string, render_template
import fizzbuzz as fb
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def fizz_buzz_app():
    number_str = request.form.get('number')
    if number_str and number_str.isdigit():  # make sure its not empty and valid number
        n = int(number_str)
        result = numbers(n)
    else:
        result = "Please enter a valid number."
    return render_template('index.html', result=result, number=number_str)

def numbers(n):
    result = fb.fizzbuzz(n)[1]
    return ''.join(map(str, result)) 


if __name__ == '__main__':
    app.run()