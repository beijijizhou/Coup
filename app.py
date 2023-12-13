from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
game_status = "pending"
print(game_status )

@app.route('/')
def index():
    
    return render_template('index.html', game_status=game_status)

@app.route('/update_status', methods=['POST'])
def update_status():
    global game_status
    # Change the game status here
    game_status = "started" if game_status == "pending" else "pending"
    print(game_status)
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)