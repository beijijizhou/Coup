from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
game_status = "pending"
ai_number = 1
print(game_status )

@app.route('/')
def index():
    
    return render_template('index.html', game_status=game_status, ai_number = ai_number)

@app.route('/update_status', methods=['POST'])
def update_status():
    global game_status
    # Change the game status here
    game_status = "started" if game_status == "pending" else "pending"
    print(game_status)
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