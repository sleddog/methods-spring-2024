from flask import Flask, request, render_template_string
import fizzbuzz as fb
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def wbapp():
    if request.method == 'POST':
        number = int(request.form['number'])
        result = fb.fizzBuzz(number)[1]
        return render_template_string("{{ result }}", result=result)

if __name__ == '__main__':
    app.run()