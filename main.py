import pygame
import random
import math
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
            new_ant = Ant(rx, ry, self)
            self.ants.append(new_ant)
        # right now a job is just a position
        # we want the ant to pick up the thing
        # and move it to a spot to drop it off
        self.jobs = []
        self.working_jobs = []
        self.drop_off = pygame.Rect(20, 20, 20, 20)
        self.create_jobs(5)

    def get_jobs_in_range(self, pos, job_range):
        result = []
        for job in self.jobs:
            d = self.get_distance(pos, job)
            if d < job_range:
                result.append(job)
        return result

    def request_job(self, job):
        if job in self.jobs:
            self.jobs.remove(job)
            self.working_jobs.append(job)
            return True
        return False

    def get_distance(self, pos1, pos2):
        return math.sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2))

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

        for job in self.working_jobs:
            pygame.draw.rect(canvas, (255, 255, 255), (job[0], job[1], 5, 5))

        pygame.draw.rect(canvas, (255, 255, 255), self.drop_off)

    def handle_event(self, event):
        pass


if __name__ == "__main__":
    e = Engine(Game)
    e.game_loop()
