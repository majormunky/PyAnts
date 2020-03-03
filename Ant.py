import math
import pygame
import random
from Engine.Config import get_screenrect
import utils


class Ant:
    def __init__(self, x, y, game):
        self.game = game
        self.screenrect = get_screenrect()
        self.size = 5
        self.range = 50
        self.current_range = self.size + 1
        self.current_job = None
        self.target = None
        self.scan_speed = 125
        self.scan_timer = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.random(), random.random())
        self.state = None
        self.change_state("scanning", "Ant Init")
        self.colors = {
            "searching": (200, 0, 0),
            "scanning": (0, 0, 200),
            "found": (0, 200, 0),
            "moving_to_exit": (200, 0, 200),
        }
        self.speeds = {
            "searching": 0.05,
            "found": 0.05,
            "moving_to_exit": 0.1,
        }

    def get_new_target(self):
        print("Getting New Target")
        while True:
            print("Trying..")
            rx = random.randint(20, self.screenrect.width - 20)
            ry = random.randint(20, self.screenrect.height - 20)
            d = utils.get_distance(self.position, (rx, ry))
            if d > 30:
                print("Found it")
                return (rx, ry)
            else:
                print("Trying Again")

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
                        angle = utils.get_angle(self.position, self.current_job)
                        rads = math.radians(angle)
                        vx = self.speeds["found"] * math.cos(rads)
                        vy = self.speeds["found"] * math.sin(rads)
                        self.velocity.x = vx
                        self.velocity.y = -vy
                        self.change_state("found", "Found Job")
                if self.current_range > self.range:
                    self.current_range = self.size + 1
                    self.change_state(
                        "searching",
                        "unable to find jobs at this position, moving to a new one",
                    )
                    # px = int(self.position.x)
                    # py = int(self.position.y)
                    # rx = random.randint(px - 250, px + 250)
                    # ry = random.randint(py - 250, py + 250)

                    self.target = self.get_new_target()

                    angle = utils.get_angle(self.position, self.target)
                    rads = math.radians(angle)
                    vx = self.speeds["found"] * math.cos(rads)
                    vy = self.speeds["found"] * math.sin(rads)
                    self.velocity.x = vx
                    self.velocity.y = -vy
        elif self.state == "found":
            self.update_position(dt)
            d = self.get_distance_to("job")
            if d < 5:
                self.change_state("moving_to_exit", "Found our job, moving to exit")
        elif self.state == "searching":
            self.update_position(dt)
            d = self.get_distance_to("target")
            if d < 20:
                self.target = None
                self.change_state(
                    "scanning", "After searching, we found a new spot to scan"
                )
            # if not self.screenrect.collidepoint(self.position):
            #     print("Going offscreen, generating new target")
            #     self.target = self.get_new_target()

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
                    canvas, (255, 255, 255), self.target, self.size + 4, 1
                )
        # elif self.state == "found":
        #     pygame.draw.line(canvas, (255, 255, 255), self.position, self.current_job)

    def handle_event(self, event):
        pass
