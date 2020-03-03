import pygame
import random
from Engine.Engine import Engine
from Engine.Config import get_screenrect


class Game:
    def __init__(self):
        self.screenrect = get_screenrect()
        self.ants = []
        for _ in range(10):
            rx = random.randint(0, self.screenrect.width)
            ry = random.randint(0, self.screenrect.height)
            new_ant = Ant(rx, ry)
            self.ants.append(new_ant)

    def update(self, dt):
        for ant in self.ants:
            ant.update(dt)

    def draw(self, canvas):
        for ant in self.ants:
            ant.draw(canvas)

    def handle_event(self, event):
        pass


class Ant:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = (200, 0, 0)

    def update(self, dt):
        pass

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)

    def handle_event(self, event):
        pass


if __name__ == "__main__":
    e = Engine(Game)
    e.game_loop()
