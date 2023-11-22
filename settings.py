class Settings():

    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 950
        self.bg_color = (4, 12, 6)

        # Ship settings
        self.ship_speed_factor = 0.4
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 238, 255, 204
        # Bullet interval settings (in milliseconds)
        self.attack_speed = 800  

        # Star settings
        self.num_stars = 100
        self.star_size = 2
        self.star_color = (255, 255, 255)

        # Alien settings
        self.alien_speed_factor = 0.15
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


        # How quickly the game speeds up
        self.speedup_scale = 1.2
        self.attack_speed_scale = 0.9
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.5


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 0.4
        self.attack_speed = 800  
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.2

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.alien_speed_factor *= self.speedup_scale
        self.attack_speed *= self.attack_speed_scale 
        self.bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)