from flask import Flask, jsonify, render_template
from game_stats import GameStats
from settings import Settings
import subprocess

app = Flask(__name__)
ai_settings = Settings()
stats = GameStats(ai_settings)


@app.route('/')
def index():
    # Start the game using a subprocess
    subprocess.Popen(['python', 'alien_space_defenders.py'])
    
    return render_template('index.html')


@app.route('/high_score', methods=['GET'])
def get_high_score():
    return jsonify({"high_score": stats.high_score})


if __name__ == '__main__':
    app.run(debug=True)




