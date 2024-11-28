from flask import Flask,request
from services import Player,Session

app = Flask(__name__)

sessions = {}

@app.route('/create/session',methods=['POST'])
def create_session():
    body = request.get_json()
    Owner = Player(body['Owner']['id'],body['Owner']['name'])
    session = Session([Owner])
    sessions[str(session.getId())] = session
    return str(session.getId())

@app.route('/join/session',methods=['POST'])
def join_session():
    body = request.get_json()
    session = sessions[body['session']]
    player = Player(body['Player']['id'],body['Player']['name'])
    session.players.append(player)
    return f'{len(session.players)}'

@app.route('/session/start',methods=['POST'])
def start_session():
    body = request.get_json()
    session = sessions[body['session']]
    player = Player(body['Player']['id'],body['Player']['name'])
    if session.owner != player:
        return 'You are not the owner of this session'
    session.start()
    return 'Session started'    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4160)