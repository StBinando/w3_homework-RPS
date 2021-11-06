from flask import render_template, request, redirect
from rps import app
from models.game import *
from models.player import *

p1 = Player("a","b")
p2 = Player("c","d")
game = Game(p1, p2)

@app.route('/')
def index():
    return render_template('index.html', title='RPSonline')


@app.route('/2_Players')
def game1():
    return render_template('2players.html', title="RPSonline - 2 Players")


@app.route('/2_Players', methods=['POST'])
def play_game1():
    player1 = request.form['p1']
    choice_player1 = request.form['choice_p1']
    player2 = request.form['p2']
    choice_player2 = request.form['choice_p2']

    game.get_input_player1(player1, choice_player1)
    game.get_input_player2(player2, choice_player2)
    back = "2_Players"
    return redirect(f'/{back}/{game.player1.choice}-{game.player2.choice}')



@app.route('/1_Player')
def game2():
    return render_template('1player.html', title="RPSonline - 1 Player")

@app.route('/1_Player', methods=['POST'])
def play_game2():
    player1 = request.form['p1']
    choice_player1 = request.form['choice_p1']
    game.get_input_player1(player1, choice_player1)
    game.get_computer_choices()

    back = "1_Player"
    return redirect(f'/{back}/{game.player1.choice}-{game.player2.choice}')


@app.route('/<back>/<choice1>-<choice2>')
def result(choice1, choice2, back):
    winner = game.get_winner()
    return render_template('result.html', title="RPSonline - result", winner = winner, back = back)
