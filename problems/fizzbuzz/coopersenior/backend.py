from flask import Flask, render_template, request
from fizzbuzz import fizzBuzz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fizzbuzz_app.html')

@app.route('/fizzbuzz_app', methods=['POST'])
def fizz_buzz_app():
    number_str = request.form.get('number')
    if number_str and number_str.isdigit():  # make sure its not empty and valid number
        n = int(number_str)
        result = numbers(n)
    else:
        result = "Please enter a valid number."
    return render_template('fizzbuzz_app.html', result=result, number=number_str)

def numbers(n):
    result = fizzBuzz(n)
    return ''.join(map(str, result))  

if __name__ == '__main__':
    app.run()
