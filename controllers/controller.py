from flask import render_template, request, redirect
from rps import app
from models.game import *
from models.player import *


# initializes player and game objects
p1 = Player("","")
p2 = Player("","")
game = Game(p1, p2)


# route to INDEX page
@app.route('/')
def index():
    return render_template('index.html', title='RPSonline')


# route to FORM page with 2 Players
@app.route('/2_Players')
def game1():
    return render_template('2players.html', title="RPSonline - 2 Players")


# gets the data from the FORM page with 2 Players
# and redirect to the result page on submit
@app.route('/2_Players', methods=['POST'])
def play_game1():
    
    # gets the values from the forms and assign them to local variables
    player1 = request.form['p1']
    choice_player1 = request.form['choice_p1']
    player2 = request.form['p2']
    choice_player2 = request.form['choice_p2']

    # calls class Game methods to POST the values
    # into the game object
    game.get_input_player1(player1, choice_player1)
    game.get_input_player2(player2, choice_player2)

    # sets the variable "back" to the route to the 2 players game
    # for the back button "Play again?" on result page
    back = "2_Players"

    # redirects on submission to the result page with a dynamic
    # route based on variables "back" (game-mode 1 or 2 players)
    # and the combination of selected choices:
    # ("/2_Players/rock-rock", "1_Player/cissors-paper", etc...)
    return redirect(f'/{back}/{game.player1.choice}-{game.player2.choice}')


# route to FORM page with 1 Player - against the computer
@app.route('/1_Player')
def game2():
    return render_template('1player.html', title="RPSonline - 1 Player")


# gets the data from the FORM page with 1 Player and fills is the data
# for the computer, then redirects to the result page on submit
@app.route('/1_Player', methods=['POST'])
def play_game2():

    # gets the values from the forms and assign them to local variables
    player1 = request.form['p1']
    choice_player1 = request.form['choice_p1']

    # calls class Game method to POST the values
    # for Player 1 into the game object
    game.get_input_player1(player1, choice_player1)

    # calls class Game method to generate a random choice for
    # the computer and POST it the game object with the computer name
    game.get_computer_choices()
    
    # sets the variable "back" to the route to the 1 player game
    # for the back button "Play again?" on result page
    back = "1_Player"

    # redirects on submission to the result page with a dynamic
    # route as per the "@ Players game"
    return redirect(f'/{back}/{game.player1.choice}-{game.player2.choice}')


# route to RESULT page - using the dynamic address based on variables
# fromm the 2 possible games
@app.route('/<back>/<choice1>-<choice2>')
def result(choice1, choice2, back):

    # calls class Game method to get the winner and assign it to
    # a local variable
    winner = game.get_winner()

    return render_template('result.html', title="RPSonline - result", winner = winner, back = back, game = game)
