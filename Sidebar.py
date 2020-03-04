import pygame


class Sidebar:
    def __init__(self, rect):
        self.background_color = (20, 0, 0)
        self.rect = rect

    def update(self, dt):
        pass

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.background_color, self.rect)

    def handle_event(self, event):
        pass
