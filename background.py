import pygame
import os

class Background:
    """Adding a background to the game"""
    def __init__(self,screen,background_file_location):
        self.screen = screen
        self.background_image = pygame.image.load(background_file_location)
        self.background_image_width = self.background_image.get_width()
        self.background_image_1_x = 0
        self.background_image_2_x = self.background_image_width

    def check_if_background_reached_end(self):
        """Checks if the background image is outside game area and updates postion accordingly"""
        if self.background_image_1_x < -1*self.background_image_width:
            self.background_image_1_x = self.background_image_width
        if self.background_image_2_x < -1*self.background_image_width:
            self.background_image_2_x = self.background_image_width

    def move_background(self,speed):
        """Move the background to give illusion of Dino movement"""
        self.background_image_1_x -= speed
        self.background_image_2_x -= speed
        self.check_if_background_reached_end()
        self.draw_background()

    def draw_background(self):
        """Draw the background image"""
        self.screen.blit(self.background_image,(self.background_image_1_x,0))
        self.screen.blit(self.background_image,(self.background_image_2_x,0))