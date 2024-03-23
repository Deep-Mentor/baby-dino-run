import pygame
import sys
import random
import math
from settings import Settings
from background import Background
from enemy import Enemy
from dino import Dino
from scoring import Score
from sound import SoundManager

class Baby_Dino_Game:
    """Main controller for the game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_dimension)
        self.distance_threshold = 85
        pygame.display.set_caption("Baby Dino Run")
        self.initialize_game()

    def initialize_game(self):
        self.background = Background(self.screen,self.settings.background_file_location)
        self.music = SoundManager("sound")
        self.dino = Dino(self.screen,
                         self.settings.dino_file_location,
                         self.settings.dino_position[0],
                         self.settings.dino_position[1])

        self.enemies = []
        self.enemies.append(self.create_enemy())

        self.speed =5
        self.loop_count = 0
        self.score = Score(self.screen,self.settings.score_position[0],self.settings.score_position[1])

        self.music.load_background_sound()
        pygame.mixer.music.play(-1)

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Loop to run the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.jump()
                    elif event.key == pygame.K_q:
                        sys.exit()
                    elif self.dino.dino_dead and event.key == pygame.K_p:
                        self.initialize_game()
                elif event.type == pygame.QUIT:
                    sys.exit()
            if not self.dino.dino_dead:
                self.loop_count+=1
                self.background.move_background(self.speed)
                self.calculate_and_display_score()
                self.update_enemies()
                self.add_enemy_if_applicable()
                self.dino.move_dino()
                self.check_dino_enemy_collision()
                pygame.display.flip()
            self.clock.tick(60)

    def update_enemies(self):
        """Update enemy state"""
        enemies_copy = self.enemies[:]
        for enemy in self.enemies:
            enemy.move_enemy(self.speed)
            if not enemy.check_visibility():
                enemies_copy.remove(enemy)
        self.enemies = enemies_copy

    def add_enemy_if_applicable(self):
        """Add new enemy if there are few enemies on screen"""
        if not self.enemies or self.enemies[-1].enemy_image_x<700:
            if random.randrange(100) > 96:
                self.enemies.append(self.create_enemy())

    def create_enemy(self):
        return Enemy(self.screen,
                     self.settings.enemy_file_location,
                     self.settings.enemy_position[0],
                     self.settings.enemy_position[1])
    
    def check_dino_enemy_collision(self):
        """Check for collision between Dino and enemies"""
        dino_centre = [self.dino.dino_pos_x + 50,self.dino.dino_pos_y + 50]
        for enemy in self.enemies:
            enemy_centre = [enemy.enemy_image_x + 75,enemy.enemy_image_y + 75]
            if self.check_collision(dino_centre,enemy_centre):
                self.dino.dead()
                self.speed = 0
                self.display_game_over_message()
    
    def check_collision(self,first_object,second_object):
        """Checks if Dino has collided with an enemy"""
        return math.dist(first_object,second_object) < self.distance_threshold
    
    def calculate_and_display_score(self):
        """Calculate and display score"""
        score_value = self.loop_count * self.speed
        self.score.display_score(score_value)
    
    def display_game_over_message(self):
        """Display game over message"""
        my_font = pygame.font.SysFont('Comic Sans MS',30)
        text_surface = my_font.render("Game Over", False,(0,0,0))
        self.screen.blit(text_surface,(self.settings.game_over_message_position[0],self.settings.game_over_message_position[1]))
        text_surface = my_font.render("Press P if you want to play again", False,(0,0,0))
        self.screen.blit(text_surface,(self.settings.game_over_message_position[0] - 150,self.settings.game_over_message_position[1] + 30))
        text_surface = my_font.render("Press Q if you want to quit game", False,(0,0,0))
        self.screen.blit(text_surface,(self.settings.game_over_message_position[0] - 150,self.settings.game_over_message_position[1] + 60))

if __name__ == "__main__":
    baby_dino_run = Baby_Dino_Game()
    baby_dino_run.run_game()