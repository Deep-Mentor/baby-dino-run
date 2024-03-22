import pygame
import os
from enum import Enum
from sound import SoundManager

class Operation(Enum):
    """Enum to store different operations Dino can perform"""
    RUN = 1
    JUMP = 2

class Dino:
    """This class is for maintaining behaviour and state of Baby Dino"""

    JUMP_SUB_FOLDER_NAME = "jump"
    RUN_SUB_FOLDER_NAME = "run"

    def __init__(self,screen,dino_base_directory,dino_start_x,dino_start_y):
        self.screen = screen
        self.dino_base_directory = dino_base_directory

        self.dino_pos_x = dino_start_x
        self.dino_pos_y = dino_start_y
        self.ground_pos_y = dino_start_y

        self.present_image_index = 0
        self.movement_tracker = 1
        self.run_image_change_rate = 10

        self.dino_jump_speed = 5
        self.dino_max_jump = 200
        self.max_height_stay = 15
        self.max_height_stay_present_count = 0
        self.dino_reached_max_height = False
        self.dino_on_ground = True
        self.dino_jump = False

        self.dino_dead = False
        self.operation = Operation.RUN
        self.music = SoundManager("sound")

        self.load_behaviour_images(self.dino_base_directory)
        self.present_image = self.run_images[0]

        self.initialize_jump_image_change_distance()

    def run(self):
        """Initialize the different run values and flags"""
        self.operation = Operation.RUN
        self.present_image_index = 0

    def jump(self):
        """Initialize the different jump values and flags only in previous operation  is RUN"""
        if self.operation == Operation.RUN:
            self.operation = Operation.JUMP
            self.present_image_index = 0
            self.max_height_stay_present_count = 0
            self.dino_reached_max_height = False
            self.dino_on_ground = False
            self.music.play_jump_sound()

    def dead(self):
        """Update the dead flag when Dino is dead"""
        self.dino_dead = True
        self.music.play_dead_sound()

    def move_dino(self):
        """Move the Dino based on type of opetaion Dino is performing"""
        self.movement_tracker += 1
        if self.operation == Operation.JUMP:
            if not self.dino_on_ground:
                if self.dino_reached_max_height:
                    if self.max_height_stay_present_count == self.max_height_stay:
                        self.dino_pos_y += self.dino_jump_speed
                else:
                    self.dino_pos_y -= self.dino_jump_speed
                self.update_dino_flight_flags()
                if self.movement_tracker % self.run_image_change_rate == 0 and self.check_if_jump_images_need_to_be_changed():
                    self.update_present_image()
            else:
                self.run()
        elif self.operation == Operation.RUN:
            if self.movement_tracker%self.run_image_change_rate == 0:
                self.movement_tracker = 1
                self.update_present_image()
        self.draw_dino()

    def update_dino_flight_flags(self):
        """Update flags and count when Dino is on flight"""
        if not self.dino_reached_max_height:
            if self.dino_pos_y <= self.dino_max_jump:
                self.dino_reached_max_height = True
        elif self.max_height_stay_present_count < self.max_height_stay:
            self.max_height_stay_present_count += 1
        self.dino_on_ground = self.dino_pos_y >= self.ground_pos_y

    def update_present_image(self):
        """Update images for Dino"""
        if self.operation == Operation.JUMP:
            self.present_image_index += 1
            if self.present_image_index >= len(self.jump_images):
                self.present_image_index = 0
            else:
                self.present_image = self.jump_images[self.present_image_index]
            if self.dino_on_ground:
                self.operation = Operation.RUN
                self.present_image_index = 0
                self.present_image = self.run_images[self.present_image_index]
        elif self.operation == Operation.RUN:
            self.present_image_index += 1
            if self.present_image_index >= len(self.run_images):
                self.present_image_index = 0
            self.present_image = self.run_images[self.present_image_index]

    def check_if_jump_images_need_to_be_changed(self):
        """Check if Dino image need to be changed as per the height reached for jump"""
        if not self.dino_reached_max_height or not self.max_height_stay_present_count < self.max_height_stay:
            distance_travelled = self.ground_pos_y - self.dino_pos_y
            if self.dino_reached_max_height:
                distance_travelled += self.ground_pos_y -self.dino_max_jump
            return distance_travelled/(self.present_image_index + 1)*self.image_change_unit_distance > 0
        return False

    def initialize_jump_image_change_distance(self):
        """Initialize the image change rate based on number of images for jump"""
        half_of_jump_images = len(self.jump_images)/2
        distance_between_ground_and_max_jump = self.ground_pos_y - self.dino_max_jump
        self.image_change_unit_distance = int(distance_between_ground_and_max_jump/half_of_jump_images)

    def draw_dino(self):
        """Draw the Dino image"""
        self.screen.blit(self.present_image,(self.dino_pos_x,self.dino_pos_y))

    def load_behaviour_images(self,dino_base_directory):
        """Load behaviour images"""
        self.run_images = self.load_images(os.path.join(dino_base_directory,self.RUN_SUB_FOLDER_NAME))
        self.jump_images = self.load_images(os.path.join(dino_base_directory,self.JUMP_SUB_FOLDER_NAME))

    def load_images(self,source_folder_path):
        """Load images from a folder"""
        images = []
        for file_name in sorted(os.listdir(source_folder_path)):
            complete_file_path = os.path.join(source_folder_path,file_name)
            if ".png" in complete_file_path:
                images.append(pygame.image.load(complete_file_path))
        return images