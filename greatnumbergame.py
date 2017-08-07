from flask import Flask, session, request, redirect, render_template
import random


app = Flask(__name__)
app.secret_key = 'colab'

@app.route('/')
def start():
    if 'random_number' not in session:
        session['random_number'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    print session['random_number'] 
    print request.form['guess']
    return redirect('/')




app.run(debug=True)