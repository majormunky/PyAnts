import pygame
import random
from Engine.Config import get_screenrect


class Ant:
    def __init__(self, x, y, game):
        self.game = game
        self.screenrect = get_screenrect()
        self.size = 5
        self.range = 50
        self.current_range = self.size + 1
        self.current_job = None
        self.scan_speed = 125
        self.scan_timer = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.random(), random.random())
        self.state = "scanning"
        self.colors = {
            "searching": (200, 0, 0),
            "scanning": (0, 0, 200),
            "found": (0, 200, 0),
        }
        self.speeds = {
            "searching": 0.15,
            "scanning": 0,
            "found": 0.35,
        }

    def update(self, dt):
        if self.state == "scanning":
            self.scan_timer += dt
            if self.scan_timer > self.scan_speed:
                self.scan_timer = 0
                self.current_range += 1
                jobs = self.game.get_jobs_in_range(self.position, self.current_range)
                if jobs:
                    if self.game.request_job(jobs[0]):
                        self.current_job = jobs[0]
                        self.state = "found"
                if self.current_range > self.range:
                    print("Unable to find any jobs, moving to searching state")
                    self.state = "searching"

    def draw(self, canvas):
        pygame.draw.circle(
            canvas,
            self.colors[self.state],
            (int(self.position.x), int(self.position.y)),
            self.size,
        )
        if self.state == "scanning":
            pygame.draw.circle(
                canvas,
                (255, 255, 255),
                (int(self.position.x), int(self.position.y)),
                self.current_range,
                1,
            )

    def handle_event(self, event):
        pass
