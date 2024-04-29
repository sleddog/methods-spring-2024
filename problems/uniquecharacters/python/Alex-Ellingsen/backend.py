from flask import Flask, request, render_template
import uniqueStrings

app = Flask(__name__)

# Route to serve the HTML form
@app.route('/')
def form():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/unique_string', methods=['POST'])
def submit():
    data = request.form.get('string')
    return render_template('index.html', answer=str(uniqueStrings.uniqueString(data)))

if __name__ == '__main__':
    app.run()