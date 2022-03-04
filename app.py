from boggle import Boggle
from flask import Flask, jsonify, request, session, redirect, render_template

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

boggle_game = Boggle()


@app.route('/')
def index():
    """Generate board and display board on webpage"""

    board = boggle_game.make_board()

    session['board'] = board
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)

    return render_template('index.html', board=board, highscore=highscore, nplays=nplays)


@app.route('/check-word')
def check_word():
    """Check if word is valid in dictionary"""

    word = request.args['word']
    board = session['board']
    res = boggle_game.check_valid_word(board, word)

    return jsonify({'result': res})


@app.route('/post-score', methods=['POST'])
def post_score():
    """Receive score, update nplays, and update highscore if possible."""

    score = request.join['score']
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)
