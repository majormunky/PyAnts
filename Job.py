import pygame


class Job:
    def __init__(self, position):
        self.position = position
        self.size = 2
        self.is_active = True

    def update(self, dt):
        pass

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def __getitem__(self, key):
        if key not in [0, 1]:
            raise KeyError
        if key == 0:
            return self.position.x
        elif key == 1:
            return self.position.y

    def draw(self, canvas):
        if self.is_active:
            pygame.draw.rect(
                canvas,
                (255, 255, 255),
                (self.position.x, self.position.y, self.size, self.size),
            )

    def handle_event(self, event):
        pass
