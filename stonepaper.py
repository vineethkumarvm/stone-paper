from flask import Flask , render_template
from random import randint


app= Flask('vineeth')

def computer_move():
    options =['stone','paper','pencil','scissor']
    move = options[randint(0,3)]
    return move

def winner(computer_move,player_move):
    if computer_move==player_move:
        winner = "tie"
    elif player_move == "paper" and computer_move == "pencil":
        winner = "computer"
    elif player_move == "paper" and computer_move == "scissor":
        winner = "computer"
    elif player_move == "scissor" and computer_move == "stone":
        winner = "computer"
    else:
        winner = 'player'

    return winner

@app.route('/')
def index():
    print(computer_move())
    return render_template('index.html')

@app.route('/vineeth/<choice>')
def vineeth(choice):

    player_move = choice
    computer = computer_move()
    winner_g = winner(computer,player_move)
    print(player_move)
    print(computer)
    print(winner_g)

    return render_template('winner.html',vineeth = winner_g,computer=computer,player_move=player_move)

app.run()
