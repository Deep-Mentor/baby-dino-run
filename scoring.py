import pygame

class Score:
    """Define scoring logic for the game"""
    def __init__(self,screen,display_position_x,display_position_y):
        pygame.font.init()
        self.screen = screen
        self.my_font = pygame.font.SysFont('Comic Sans MS',30)
        self.display_position_x = display_position_x
        self.display_position_y = display_position_y

    def display_score(self,pixels_travelled):
        """Display present score"""
        self.calculate_score(pixels_travelled)
        text_surface = self.my_font.render(str(self.score),False,(0,0,0))
        self.screen.blit(text_surface,(self.display_position_x,self.display_position_y))

    def calculate_score(self,pixels_travelled):
        """Calculate score based on distance travelled"""
        self.score = int(pixels_travelled/10)