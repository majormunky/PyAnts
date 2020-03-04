import pygame
from Engine.Text import text_surface


class Sidebar:
    def __init__(self, rect, game):
        self.background_color = (20, 0, 0)
        self.game = game
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
        ants_looking = [ant for ant in self.game.ants if ant.state == "searching"]
        looking_text = text_surface(
            "Looking: {}".format(len(ants_looking)), font_size=36
        )
        self.image.blit(
            looking_text,
            ((self.rect.width / 2) - (looking_text.get_rect().width / 2), 50),
        )
        ants_scanning = [ant for ant in self.game.ants if ant.state == "scanning"]
        scanning_text = text_surface(
            "Scanning: {}".format(len(ants_scanning)), font_size=36
        )
        self.image.blit(
            scanning_text,
            ((self.rect.width / 2) - (scanning_text.get_rect().width / 2), 80),
        )
        ants_found = [ant for ant in self.game.ants if ant.state == "found"]
        found_text = text_surface("Found: {}".format(len(ants_found)), font_size=36)
        self.image.blit(
            found_text,
            ((self.rect.width / 2) - (found_text.get_rect().width / 2), 110),
        )
        exit_found = [ant for ant in self.game.ants if ant.state == "moving_to_exit"]
        exit_text = text_surface("Exiting: {}".format(len(exit_found)), font_size=36)
        self.image.blit(
            exit_text, ((self.rect.width / 2) - (exit_text.get_rect().width / 2), 140),
        )

    def draw(self, canvas):
        canvas.blit(self.image, (self.rect.x, self.rect.y))

    def handle_event(self, event):
        pass
