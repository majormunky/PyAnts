import pygame
from Engine.Engine import Engine


class Game:
    def __init__(self):
        pass

    def update(self, dt):
        pass

    def draw(self, canvas):
        pygame.draw.rect(canvas, (200, 0, 0), (25, 25, 25, 25))

    def handle_event(self, event):
        pass


if __name__ == "__main__":
    e = Engine(Game)
    e.game_loop()
