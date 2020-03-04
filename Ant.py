import math
import pygame
import random
from Engine.Config import get_screenrect
import utils


class Ant:
    def __init__(self, x, y, game):
        self.game = game
        self.screenrect = get_screenrect()
        self.size = random.randint(3, 6)
        self.range = random.randint(35, 60)
        self.current_range = self.size + 1
        self.current_job = None
        self.target = None
        self.scan_speed = random.randint(100, 200)
        self.scan_timer = 0
        self.found_waiting_timer = 0
        self.found_waiting_time = 500
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.random(), random.random())
        self.state = None
        self.change_state("scanning", "Ant Init")
        self.colors = {
            "searching": (50, 50, 50),
            "scanning": (100, 100, 100),
            "found": (150, 150, 150),
            "found_waiting": (175, 175, 150),
            "moving_to_exit": (200, 200, 200),
        }
        self.speeds = {
            "searching": 0.05,
            "found": 0.05,
            "moving_to_exit": 0.1,
        }
        self.speed = 0.05

    def get_new_target(self):
        print("Getting New Target")
        while True:
            print("Trying..")
            rx = random.randint(20, self.game.game_area.width - 20)
            ry = random.randint(20, self.game.game_area.height - 20)
            d = utils.get_distance(self.position, (rx, ry))
            if d > 30:
                print("Found it")
                return pygame.Vector2(rx, ry)
            else:
                print("Trying Again")

    def get_exit_target(self):
        return pygame.Vector2(self.game.drop_off.x, self.game.drop_off.y)

    def update(self, dt):
        if self.state == "scanning":
            self.scan_timer += dt
            if self.scan_timer > self.scan_speed:
                self.scan_timer = 0
                self.current_range += 1
                jobs = self.game.get_jobs_in_range(self.position, self.current_range)
                if jobs:
                    if self.game.request_job(jobs[0]):
                        # we need to setup our velocity before we switch to
                        # the found state
                        self.current_job = jobs[0]
                        new_target = pygame.Vector2(
                            self.current_job.x, self.current_job.y
                        )
                        self.set_target(new_target)
                        self.change_state("found", "Found Job")
                if self.current_range > self.range:
                    self.current_range = self.size + 1
                    self.change_state(
                        "searching",
                        "unable to find jobs at this position, moving to a new one",
                    )
                    new_target = self.get_new_target()
                    self.set_target(new_target)
        elif self.state == "found":
            self.update_position(dt)
            d = self.get_distance_to("job")
            if d < 5:
                self.change_state(
                    "found_waiting",
                    "We found our job, but, going to wait a second before going to exit",
                )
        elif self.state == "searching":
            self.update_position(dt)
            d = self.get_distance_to("target")
            # print(d)
            if d < 10:
                self.target = None
                self.change_state(
                    "scanning", "After searching, we found a new spot to scan"
                )
        elif self.state == "moving_to_exit":
            self.update_position(dt)
            d = self.get_distance_to("target")
            if d < 20:
                self.target = None
                self.game.job_completed(self.current_job)
                self.change_state("scanning", "Ant put job away, looking for new one")
        elif self.state == "found_waiting":
            self.found_waiting_time += dt
            if self.found_waiting_time > self.found_waiting_timer:
                self.found_waiting_time = 0
                new_target = self.get_exit_target()
                self.set_target(new_target)
                self.change_state("moving_to_exit", "Found our job, moving to exit")
            else:
                print("Waiting....")

    def set_target(self, target):
        self.target = target
        angle = utils.get_angle(self.position, target)
        rads = math.radians(angle)
        vx = self.speed * math.cos(rads)
        vy = self.speed * math.sin(rads)
        self.velocity.x = vx
        self.velocity.y = -vy

    def change_state(self, new_state, why):
        self.state = new_state
        print("Changed state to: {} ({})".format(self.state, why))

    def get_distance_to(self, job_type):
        if job_type == "job":
            return utils.get_distance(self.position, self.current_job)
        elif job_type == "target":
            return utils.get_distance(self.position, self.target)

    def update_position(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

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
        elif self.state == "searching":
            if self.target:
                pygame.draw.circle(
                    canvas,
                    (255, 255, 255),
                    (int(self.target.x), int(self.target.y)),
                    self.size + 4,
                    1,
                )

    def handle_event(self, event):
        pass
