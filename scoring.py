import pygame
import os

from settings import Settings

class Score:
    """Define scoring logic for the game"""
    def __init__(self,screen,display_position_x,display_position_y):
        pygame.font.init()
        self.screen = screen
        self.my_font = pygame.font.SysFont('Comic Sans MS',30)
        self.settings = Settings()
        self.score_display_position_x = display_position_x
        self.score_display_position_y = display_position_y
        self.populate_highest_score()

    def display_score(self,pixels_travelled):
        """Display present score"""
        self.calculate_score(pixels_travelled)
        self.update_highest_score()
        score_surface = self.my_font.render(str(self.score),False,(0,0,0))
        highest_score_surface =  self.my_font.render("Highest Score : " + str(self.highest_score),False,(0,0,0))
        self.screen.blit(score_surface,(self.score_display_position_x,self.score_display_position_y))
        self.screen.blit(highest_score_surface,(self.score_display_position_x - 400,self.score_display_position_y))

    def calculate_score(self,pixels_travelled):
        """Calculate score based on distance travelled"""
        self.score = int(pixels_travelled/10)

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
    
    def populate_highest_score(self):
        """Get the highest score for a user"""
        if os.path.isfile(self.settings.score_file_path):
            f = open(self.settings.score_file_path, "r")
            previous_score_string = f.read()
            if previous_score_string.strip() == '':
                self.highest_score = 0
            else:
                self.highest_score = int(previous_score_string)
        else:
            self.highest_score = 0

    def save_highest_score(self):
        """Save highest score for the user"""
        f = open(self.settings.score_file_path, "w")
        f.write(str(self.score))