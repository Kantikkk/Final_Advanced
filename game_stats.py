import json
import requests

class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.load_high_score()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        data = {'high_score': self.high_score}
        with open('high_score.json', 'w') as file:
            json.dump(data, file)

    def load_high_score(self):
        try:
            with open('high_score.json', 'r') as file:
                data = json.load(file)
                self.high_score = int(data.get('high_score', 0))
        except FileNotFoundError:
            # Handle the case where the file doesn't exist initially
            pass
            self.high_score = 0

    def update_high_score(self):
        response = requests.get("http://127.0.0.1:5000/high_score")
        data = response.json()
        self.high_score = data.get('high_score', 0)