
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret'

import random

# attempts=100






# def number(guess,secret,attempts):
#     for attempt in range(attempts):
#         guess=int(input('take a guess:'))
#
#         if guess > secret:
#             print ('Too High!')
#         elif guess < secret:
#             print ('Too Low')
#         elif guess == secret:
#             print('You guessed the number correctly! The number was',secret)
#
#             break


@app.route('/')
def index():
    if (session.get('secret_num') == None):
        session['secret_num'] = random.randrange(1,101)
        session['guess'] = 102
    return render_template('index.html')


@app.route('/users', methods=['post'])
def submit():
    session['guess']=int(request.form['guess_num'])
    return redirect('/')
# @app.route('/')
# def random():
@app.route('/reset', methods=['get'])
def reset():
    session.pop('secret_num')
    session.pop('guess')
    return redirect('/')


app.run(debug=True)
