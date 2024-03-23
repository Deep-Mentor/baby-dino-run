import pygame
import os
import image_utils

class Enemy:
    """Adding an enemy to the game. The images should be of same size and png type"""

    def __init__(self,screen,enemy_folder_location,start_x,start_y):
        self.screen = screen
        self.enemy_images = image_utils.load_images(enemy_folder_location)
        self.enemy_image_x = start_x
        self.enemy_image_y = start_y

        self.present_image_index = 0
        self.movement_tracker = 1

        self.run_image_change_rate = 25

    def check_visibility(self):
        """Check if the enemy is outside game area"""
        return self.enemy_image_x + self.enemy_images[0].get_width() > 0
        
    def move_enemy(self,speed):
        """Move the enemy as per speed"""
        self.enemy_image_x -= speed
        self.movement_tracker += 1

        if self.movement_tracker % self.run_image_change_rate == 0:
            self.movement_tracker = 1
            self.change_image()
        self.draw_enemy()

    def change_image(self):
        """Change image for the enemy"""
        self.present_image_index += 1
        if self.present_image_index >= len(self.enemy_images):
            self.present_image_index = 0

    def draw_enemy(self):
        """draw the Enemy image"""
        if self.check_visibility():
            self.screen.blit(self.enemy_images[self.present_image_index],(self.enemy_image_x,self.enemy_image_y))