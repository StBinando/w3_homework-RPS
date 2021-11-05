from flask import render_template, request, redirect
from rps import app
from models.game import *
from models.player import *

p1 = Player("a","b")
p2 = Player("c","d")
game = Game(p1, p2)

# @app.route('/')
# def index():
#     return render_template('index.html', title='Home', events=events)

@app.route('/RPS_2_Players')
def game1():
    return render_template('2players.html', title="Rock Paper Scissor")

@app.route('/RPS_2_Players', methods=['POST'])
def play_game1():
    player1 = request.form['p1']
    choice_player1 = request.form['choice_p1']
    player2 = request.form['p2']
    choice_player2 = request.form['choice_p2']

    game.get_input_2_players(player1, choice_player1, player2, choice_player2)

    # return redirect('/result')

    return redirect(f'/{game.player1.choice}/{game.player2.choice}')


@app.route(f'/{game.player1.choice}/{game.player2.choice}')


# @app.route('/result')
def result():
    winner = game.get_winner()
    return render_template('result.html', title="Rock Paper Scissor", winner = winner)
