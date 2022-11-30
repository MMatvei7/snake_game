import pygame

class Globals:
    def __init__(self):
        self.window_x = 720
        self.window_y = 480

        # defining colors
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.yellow = pygame.Color(255, 255, 0)
        self.rating_score = [0] * 3
        self.tmp = 15
        self.color_ = self.green
        self.window_color = self.black
