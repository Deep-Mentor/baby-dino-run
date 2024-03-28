import pygame
import os
import image_utils

class Background:
    """Adding a background to the game"""
    def __init__(self,screen,background_folder_location):
        self.screen = screen
        self.background_layers = image_utils.load_images(background_folder_location)
        self.background_image_width = self.background_layers[0].get_width()
        self.background_layer_length = len(self.background_layers)
        self.background_layer_positions = []
        self.background_layer_speed_factor = []
        self.initialize_background_layer_position_and_speed()

    def move_background(self,speed):
        """Move the background to give illusion of Dino movement"""
        self.update_image_positions(speed)
        self.check_if_any_background_layer_reached_end()
        self.draw_background_layers()

    def update_image_positions(self,speed):
        """Update the different layers based on different speeds"""
        for _ in range(self.background_layer_length):
            speed_factor = speed/self.background_layer_speed_factor[-1]*self.background_layer_speed_factor[_]
            first_image_position = self.background_layer_positions[_][0] - speed_factor
            second_image_position = self.background_layer_positions[_][1] - speed_factor
            self.background_layer_positions[_] = (first_image_position,second_image_position)

    def check_if_any_background_layer_reached_end(self):
        for _ in range(self.background_layer_length):
            self.check_if_background_layer_reached_end(_)

    def check_if_background_layer_reached_end(self,index):
        """Checks if the background image is outside game area and updates postion accordingly"""
        first_image_position = self.background_layer_positions[index][0]
        second_image_position = self.background_layer_positions[index][1]
        if first_image_position <= -1*self.background_image_width:
            first_image_position = second_image_position + self.background_image_width
        if second_image_position <= -1*self.background_image_width:
            second_image_position = first_image_position + self.background_image_width
        self.background_layer_positions[index] = (first_image_position,second_image_position)

    def draw_background_layers(self):
        """Draw all the background layers"""
        for _ in range(self.background_layer_length):
            self.draw_background_layer(_)

    def draw_background_layer(self,index):
        """Draw the background image"""
        self.screen.blit(self.background_layers[index],(self.background_layer_positions[index][0],0))
        self.screen.blit(self.background_layers[index],(self.background_layer_positions[index][1],0))

    def initialize_background_layer_position_and_speed(self):
        """Initialize speed factor for different layers and their positions"""
        speed_factor = 1
        for _ in range(self.background_layer_length):
            self.background_layer_speed_factor.append(speed_factor)
            speed_factor *= 2
            self.background_layer_positions.append((0,self.background_image_width))