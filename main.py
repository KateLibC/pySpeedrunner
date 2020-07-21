from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import json
import os
import time

'''
Init-related functions
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(8192)
startTime = time.time()
timerRunning = True
socketio = SocketIO(app)

'''
Timer-related functions
'''


def currentTimer():
    return {
        'Game': 'Legend of Illusion starring Mickey Mouse',
        'Goal': 'Any%',
        'Splits': [
            {'Order': 1, 'Title': 'Ghost', 'Best': 0, 'Current': 0},
            {'Order': 2, 'Title': 'Lion', 'Best': 0, 'Current': 0},
            {'Order': 3, 'Title': 'Centipede', 'Best': 0, 'Current': 0},
            {'Order': 4, 'Title': 'Sorcerer', 'Best': 0, 'Current': 0},
            {'Order': 5, 'Title': 'Ghost', 'Best': 0, 'Current': 0},
            {'Order': 6, 'Title': 'King Pete', 'Best': 0, 'Current': 0},
        ],
        'PB': 0,
        'WR': 0,
        'Current': 0
    }

'''
Flask-related functions
'''

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/timerInit', methods=['GET'])
def timer():
    return json.dumps(currentTimer())

@socketio.on('timer')
def timerNow():
    def timeCount():
        return {'data': time.time() - startTime}
    while True:
        t = timeCount()
        emit('timer', t)
        time.sleep(0.1)

if __name__ == '__main__':
    socketio.run(app, debug=True)