import pygame
import os

def load_images(source_folder_path):
        """Load images from a folder"""
        images = []
        for file_name in sorted(os.listdir(source_folder_path)):
            complete_file_path = os.path.join(source_folder_path,file_name)
            if ".png" in complete_file_path:
                images.append(pygame.image.load(complete_file_path))
        return images