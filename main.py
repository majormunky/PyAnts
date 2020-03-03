import pygame
import random
from Engine.Engine import Engine
from Engine.Config import get_screenrect
from Ant import Ant


class Game:
    def __init__(self):
        self.screenrect = get_screenrect()
        self.ants = []
        for _ in range(10):
            rx = random.randint(0, self.screenrect.width)
            ry = random.randint(0, self.screenrect.height)
            new_ant = Ant(rx, ry)
            self.ants.append(new_ant)
        # right now a job is just a position
        # we want the ant to pick up the thing
        # and move it to a spot to drop it off
        self.jobs = []
        self.drop_off = pygame.Rect(20, 20, 20, 20)
        self.create_jobs(5)

    def create_jobs(self, amount):
        padding = 40
        while len(self.jobs) < amount:
            rx = random.randint(padding, self.screenrect.width - padding)
            ry = random.randint(padding, self.screenrect.height - padding)
            if (rx, ry) not in self.jobs:
                self.jobs.append((rx, ry))

    def update(self, dt):
        for ant in self.ants:
            ant.update(dt)

    def draw(self, canvas):
        for ant in self.ants:
            ant.draw(canvas)

        for job in self.jobs:
            pygame.draw.rect(canvas, (0, 200, 200), (job[0], job[1], 5, 5))

        pygame.draw.rect(canvas, (255, 255, 255), self.drop_off)

    def handle_event(self, event):
        pass


if __name__ == "__main__":
    e = Engine(Game)
    e.game_loop()
