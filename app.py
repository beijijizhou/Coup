from flask import Flask, render_template, redirect, url_for, request
from game_assets.in_game_type import TargetType, CharacterType
import random
from game_assets.game_manager import GameManager
app = Flask(__name__)
game_status = "started"
ai_number = 4

game_manager = None

@app.route('/')
def index():
    global game_manager
    game_manager = GameManager(ai_number + 1)
    return render_template('index.html', game_status=game_status,
                            ai_number = ai_number, game_manager=game_manager)

# @app.route('/update_status', methods=['POST'])
# def update_status():
#     global game_status, ai_number
#     # Change the game status here
#     if game_status == "pending":
#         game_status = "started" 
#         game_manager = GameManager(ai_number + 1)

#     else:
#         game_status = "pending"
#     return redirect(url_for('index')) 

@app.route('/update_ai', methods=['POST'])
def update_ai():
    global ai_number
    if request.method == 'POST':
        action = request.form.get('action')  # Assuming 'action' is the name of the input to determine add or minus
        
        if action == 'add' and ai_number < 6:
            ai_number += 1
        elif action == 'minus' and ai_number > 1:
            ai_number -= 1
        
    return redirect(url_for('index')) 

@app.route('/', methods=['POST'])
def select_character_action():
    global game_manager
    if request.method == 'POST':
        action_type = request.form.get('action_type')
        if action_type in TargetType.AI.name:
            action_type = select_ai_action_type()
        game_manager.player_selected_action(action_type)
        
    return render_template('index.html', game_status=game_status,
                            ai_number = ai_number, game_manager=game_manager)


def select_ai_action_type():
    target_names = [member.name for member in CharacterType]
    return random.choice(target_names)


if __name__ == '__main__':
    app.run(debug=True)