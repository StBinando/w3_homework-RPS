from flask import render_template, request, redirect
from rps import app
# from models.game import events


# @app.route('/')
# def index():
#     return render_template('index.html', title='Home', events=events)

@app.route('/RPS_2_Players')
def game1():
    return render_template('2players.html', title="Rock Paper Scissor")

@app.route('/RPS_2_Players', methods=['POST'])
def play_game1():
    p1 = request.form['p1']
    choice_p1 = request.form['choice_p1']

    p1 = request.form['p1']
    choice_p1 = request.form['choice_p1']

    return redirect('/<choice_p1>/<choice_p2>')

@app.route('/<choice_p1>/<choice_p2>')
def result():
    return render_template('result.html', title="Rock Paper Scissor", p1=play_game1.p1)
