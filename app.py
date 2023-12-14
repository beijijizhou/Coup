from flask import Flask, render_template, redirect, url_for, request
import math

from  game_assets.game_manager import GameManager
app = Flask(__name__)
game_status = "started"
ai_number = 4


@app.route('/')
def index():
    game_manager = GameManager(ai_number + 1)

    return render_template('index.html', game_status=game_status,
                            ai_number = ai_number, game_manager=game_manager)

@app.route('/update_status', methods=['POST'])
def update_status():
    global game_status, ai_number
    # Change the game status here
    if game_status == "pending":
        game_status = "started" 
        game_manager = GameManager(ai_number + 1)

    else:
        game_status = "pending"
    return redirect(url_for('index')) 

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
if __name__ == '__main__':
    app.run(debug=True)