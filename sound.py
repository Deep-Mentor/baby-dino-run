import os
import pygame

class SoundManager:
    """Class to manage sound values"""
    def __init__(self,sound_folder_location):
        self.sound_folder_location = sound_folder_location
        self.jump_sound = self.load_sound_file("slime_jump.mp3")
        self.dead_sound = self.load_sound_file("round_end.wav")

    def load_background_sound(self):
        """Get background sound loaded for the game"""
        background_file_name = "the_fun_run.wav"
        pygame.mixer.music.load(os.path.join(self.sound_folder_location,background_file_name))

    def play_jump_sound(self):
        """Play jump sound every time the character jumps"""
        pygame.mixer.Sound.play(self.jump_sound)

    
    def play_dead_sound(self):
        """Play dead sound when the character dies and stop the music"""
        pygame.mixer.Sound.play(self.dead_sound)
        pygame.mixer.music.stop()

    def load_sound_file(self,file_name):
        """Load sound file"""
        return pygame.mixer.Sound(os.path.join(self.sound_folder_location,file_name))