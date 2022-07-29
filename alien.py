import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represnet a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact location
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)