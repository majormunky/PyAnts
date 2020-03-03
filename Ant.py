import math
import pygame
import random
from Engine.Config import get_screenrect


class Ant:
    def __init__(self, x, y):
        self.screenrect = get_screenrect()
        self.size = 5
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.random(), random.random())
        self.direction = random.randint(0, 360)
        self.color = (200, 0, 0)
        self.speed = 0.15
        self.reverse = 1

    def update(self, dt):
        pass

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
            canvas, self.color, (int(self.position.x), int(self.position.y)), self.size
        )

    def calculate_new_xy(self, old, speed, angle_in_radians):
        new_x = old[0] + (speed * math.cos(angle_in_radians))
        new_y = old[1] + (speed * math.sin(angle_in_radians))
        return new_x, new_y

    def handle_event(self, event):
        pass
