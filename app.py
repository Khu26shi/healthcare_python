from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        # Handle file upload and processing here
        return render_template('dashboard.html', name=name, age=age)
    return render_template('dashboard.html')

@app.route('/process_file', methods=['POST'])
def process_file():
    # Handle file upload and processing here
    return 'File processed successfully'

if __name__ == '__main__':
    app.run(debug=True)