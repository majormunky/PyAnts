import pygame
from Engine.Text import text_surface


class Sidebar:
    def __init__(self, rect, game):
        self.background_color = (20, 0, 0)
        self.rect = rect
        self.image = None
        self.title_text = text_surface("Ants", font_size=36)
        self.update_limit = 400
        self.update_timer = 0
        self.render()

    def update(self, dt):
        self.update_timer += dt
        if self.update_timer > self.update_limit:
            self.update_timer = 0
            self.render()

    def render(self):
        self.image = pygame.Surface(
            (self.rect.width, self.rect.height), pygame.SRCALPHA
        )
        self.image.fill(self.background_color)
        self.image.blit(
            self.title_text,
            ((self.rect.width / 2) - (self.title_text.get_rect().width / 2), 20),
        )

    def draw(self, canvas):
        canvas.blit(self.image, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        pass
