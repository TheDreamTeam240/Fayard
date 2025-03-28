import random

import pygame
import src.utils as utils


class BackgroundEffects:
    class Circle:
        def __init__(self, radius, color, x, y, width):
            self.radius = radius
            self.color = color
            self.x = x
            self.y = y
            self.width = width

    def __init__(self):
        self.radius = 25
        self.colors = [(72, 59, 58), (119, 92, 85), (170, 141, 122), (211, 191, 169), (139, 0, 0)]
        self.surface = pygame.Surface((utils.world_size[0] / 4, utils.world_size[1] / 4),
                                      pygame.SRCALPHA).convert_alpha()
        self.circles = []
        self.counter = 0
        self.dest_surf = pygame.Surface((utils.world_size[0], utils.world_size[1]), pygame.SRCALPHA).convert_alpha()

    def update(self):
        if self.counter == 3:
            self.counter = 0
            for circle in self.circles:
                circle.y -= 1
                if circle.y < -25:
                    self.circles.remove(circle)
        else:
            self.counter += 1
        if random.randint(1, 25) == 1:
            self.add_circle()

    def add_circle(self):
        radius = random.randint(4, 25)
        color = random.choice(self.colors)
        x, y = random.randint(-25, int(utils.world_size[0] / 4 + 25)), utils.world_size[1] / 4
        width = random.randint(0, 25)
        self.circles.append(self.Circle(radius, color, x, y, width))

    def draw(self, surface):
        index = 0
        self.surface.fill((0, 0, 0, 0))
        for circle in self.circles:
            # Remplacez le dessin du cercle par le texte "43"
            font = pygame.font.Font(None, 36)
            if ((index % 2) == 0):
                text = font.render("GANG", True, circle.color)
            else:
                text = font.render("43", True, circle.color)

            text_rect = text.get_rect(center=(circle.x, circle.y))
            self.surface.blit(text, text_rect)
            index+=1

        surface.blit(pygame.transform.scale(self.surface, (utils.world_size[0], utils.world_size[1]), self.dest_surf),
                     (0, 0))
