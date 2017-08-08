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
    if session['random_number'] > int(request.form['guess']):
        print 'too low'
        result = "too low"
        return render_template("index.html", result = result)
        

    elif session['random_number'] == int(request.form['guess']):
        print 'you win'
        result = "you win"
        return render_template("index.html", result = result)
    
    else: 
        print 'too high'
        result = "too high"
        return render_template("index.html", result = result)

   

    print session['random_number'] 
    print int(request.form['guess'])
    





app.run(debug=True)