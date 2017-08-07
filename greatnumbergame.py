from flask import Flask, session, request, redirect, render_template


app = Flask(__name__)
app.secret_key = 'colab'

@app.route('/')
def start():
    if 'random_number' not in session:
        random_number = session['random_number']
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    if session['random_number'] > request.form['name']:
        {{'low'}}
    return redirect('/')




app.run(debug=True)