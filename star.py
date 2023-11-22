import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a star in the background."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the star and set its starting position."""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Create a star rect at (0, 0) and then set a random position.
        self.rect = pygame.Rect(0, 0, ai_settings.star_size, ai_settings.star_size)
        self.rect.x = 0
        self.rect.y = 0
        
        # Create an image for the star
        self.image = pygame.Surface((ai_settings.star_size, ai_settings.star_size))
        self.image.fill(ai_settings.star_color)

    def update(self):
        """Update the position of the star."""
        # You can add movement logic here if you want stars to move
        pass

    def draw_star(self):
        """Draw the star to the screen."""
        self.screen.blit(self.image, self.rect)
