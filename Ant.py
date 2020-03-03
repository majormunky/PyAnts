import pygame
import random
from Engine.Config import get_screenrect


class Ant:
    def __init__(self, x, y, game):
        self.screenrect = get_screenrect()
        self.size = 5
        self.range = 50
        self.current_range = self.size + 1
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
                if self.current_range > self.range:
                    print("Unable to find any jobs, moving to searching state")
                    self.state = "searching"

    def update_old(self, dt):
        self.position.x += self.velocity.x * self.speed * dt
        self.position.y += self.velocity.y * self.speed * dt

        if self.position.x < 0:
            self.velocity.x *= -1
        if self.position.y < 0:
            self.velocity.y *= -1
        if self.position.x > self.screenrect.width:
            self.velocity.x *= -1
        if self.position.y > self.screenrect.height:
            self.velocity.y *= -1

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
