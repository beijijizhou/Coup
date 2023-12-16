from flask import Flask, render_template, redirect, url_for, request, jsonify
import time
from game_assets.in_game_type import TargetType, CharacterActions, ActionType, GameStatus
import game_assets.in_game_type as in_game_type
import random
from game_assets.game_manager import GameManager


app = Flask(__name__)

ai_number = 2
game_manager = None


@app.route('/')
def index():
    global game_manager
    game_manager = GameManager(ai_number + 1)
    return game_templates()

@app.route('/start_game', methods=['POST'])
def start_game():
    global game_status, ai_number
    # Change the game status here
    if game_status == GameStatus.NOT_STARTED:
        game_status = GameStatus.IN_GAME,
        game_manager = GameManager(ai_number + 1)

    return game_templates()


@app.route('/update_ai', methods=['POST'])
def update_ai():
    global ai_number
    if request.method == 'POST':
        # Assuming 'action' is the name of the input to determine add or minus
        action = request.form.get('action')

        if action == 'add' and ai_number < 6:
            ai_number += 1
        elif action == 'minus' and ai_number > 1:
            ai_number -= 1

    return redirect(url_for('index'))


@app.route('/', methods=['POST'])
def select_character_action():
    global game_manager
    
    if request.method == 'POST':
        if 'start' in request.form:
             return game_templates()
        player_type = request.form.get('player_type')
        if player_type == TargetType.AI:
            player_action_type = select_ai_action_type()
            game_status = game_manager.player_selected_action(
                player_action_type, TargetType.AI)
            return jsonify(updated_message=game_manager.announcer.message)
        else:
            player_action_type = request.form.get('player_action_type')
            game_status = game_manager.player_selected_action(
                player_action_type, TargetType.PLAYER)

        return check_game_status(game_status)

def start_game():
    global game_manager
    game_manager = GameManager(ai_number + 1)
    return game_templates()
def check_game_status(game_status):
    if game_status == GameStatus.IN_GAME:
        print(game_status)
    else:
        game_manager.clear_announcer()
        return render_template('index.html', game_status=GameStatus.WIN,
                               ai_number=ai_number,
                               in_game_type=in_game_type)
    return game_templates()
    # else:

    #     return render_template('index.html', game_result=game_status, in_game_type=in_game_type)


def select_ai_action_type():
    target_names = [member.name for member in CharacterActions]
    # time.sleep(1)
    return random.choice(target_names)


def game_templates():
    return render_template('index.html', game_status=GameStatus.IN_GAME,
                           ai_number=ai_number, game_manager=game_manager,
                           in_game_type=in_game_type)


if __name__ == '__main__':
    app.run(debug=True)
