class Settings:
    """Class to store settings for the game"""

    def __init__(self):
        self.screen_dimension = (1400,550)
        self.background_file_location = "images/background/background.png"

        self.dino_position = (0,0)
        self.dino_file_location = "images/dino"

        self.enemy_position = (1400,340)
        self.enemy_file_location = "images/enemy"

        self.score_position = (1300,50)
        self.game_over_message_position = (600,100)