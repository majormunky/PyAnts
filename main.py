import pygame
import random
from Engine.Engine import Engine
from Engine.Config import get_screenrect, set_screensize
from Ant import Ant
from Sidebar import Sidebar
from Job import Job
import utils


class Game:
    def __init__(self):
        self.screenrect = get_screenrect()
        self.sidebar_width = 200
        self.game_area = pygame.Rect(
            0, 0, self.screenrect.width - self.sidebar_width, self.screenrect.height
        )
        self.ant_count = 4
        self.ants = []
        self.create_ants(self.ant_count)
        self.sidebar = Sidebar(
            pygame.Rect(
                self.screenrect.width - self.sidebar_width,
                0,
                self.sidebar_width,
                self.screenrect.height,
            ),
            self,
        )

        # right now a job is just a position
        # we want the ant to pick up the thing
        # and move it to a spot to drop it off
        self.jobs = []
        self.working_jobs = []
        self.done_jobs = []
        self.drop_off = pygame.Rect(20, 20, 20, 20)
        self.create_jobs(self.ant_count)
        # self.create_single_job()

    def create_ants(self, amount):
        if amount == 0:
            return
        for _ in range(self.ant_count):
            rx = random.randint(0, self.game_area.width)
            ry = random.randint(0, self.game_area.height)
            new_ant = Ant(rx, ry, self)
            self.ants.append(new_ant)

    def create_single_job(self):
        self.create_jobs(1)
        x = self.jobs[0][0] + 80
        y = self.jobs[0][1] + 80
        ant = Ant(x, y, self)
        self.ants.append(ant)

    def get_jobs_in_range(self, pos, job_range):
        result = []
        for job in self.jobs:
            d = utils.get_distance(pos, job)
            if d < job_range:
                result.append(job)
        return result

    def request_job(self, job):
        if job in self.jobs:
            self.jobs.remove(job)
            self.working_jobs.append(job)
            return True
        return False

    def job_completed(self, job):
        if job in self.working_jobs:
            self.working_jobs.remove(job)
        else:
            print("Job not found in working jobs!")
            print(job)
            print(self.working_jobs)
        self.done_jobs.append(job)

    def create_jobs(self, amount):
        padding = 40
        job_cache = []
        while len(self.jobs) < amount:
            rx = random.randint(padding, self.game_area.width - padding)
            ry = random.randint(padding, self.game_area.height - padding)
            if (rx, ry) not in job_cache:
                new_job = Job(utils.Point(rx, ry))
                self.jobs.append(new_job)
                job_cache.append((rx, ry))

    def update(self, dt):
        self.sidebar.update(dt)
        for ant in self.ants:
            ant.update(dt)

    def draw(self, canvas):
        self.sidebar.draw(canvas)
        pygame.draw.rect(canvas, (40, 0, 0), self.game_area)
        for ant in self.ants:
            ant.draw(canvas)

        for job in self.jobs:
            job.draw(canvas)

        for job in self.working_jobs:
            job.draw(canvas)

        pygame.draw.rect(canvas, (255, 255, 255), self.drop_off)

    def handle_event(self, event):
        pass


if __name__ == "__main__":
    set_screensize(1280, 720)
    e = Engine(Game)
    e.game_loop()
