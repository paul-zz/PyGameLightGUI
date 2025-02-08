import pygame

class UIElements():

    def __init__(self, rect : pygame.Rect):
        self.rect = rect

        # Appearance
        self.enableBlur = True
        self.blurRadius = 5
        self.alpha = 127

    def fit_to_width(self, surf, proportion = 0.85):
        # Fit the text to the same width of the rect
        scale = proportion * self.rect.width / surf.get_width()
        surf = pygame.transform.scale(surf, (surf.get_width() * scale, surf.get_height() * scale))
        return surf
    
    def squeeze_to_width(self, surf, proportion = 0.85):
        surf = pygame.transform.scale(surf, (self.rect.width * proportion, surf.get_height()))
        return surf