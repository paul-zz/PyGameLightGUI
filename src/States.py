import sys
import pygame

from .AssetsLoader import AssetsLoader
from .LocaleManager import LocaleManager
from .OptionBox import OptionBox
from .PushButton import PushButton

class State:
    def handle(self,event):
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

    def firstDisplay(self, screen : pygame.Surface):
        pass
        # screen.blit(bg,(0,0))
        # pygame.display.flip()


class Paused(State):
    finished = 0
    image = None
    text = ''

    def handle(self, event):
        State.handle(self, event)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            self.finished = 1

    def update(self, game):
        pass


class Homepage(State):
    def __init__(self, screen : pygame.Surface):
        self.screen = screen
        self.font_big = AssetsLoader.getFont("bigfont")
        self.font_mid = AssetsLoader.getFont("midfont")
        self.bg = AssetsLoader.getImage("background")

        self.finished = False

        # Init elements
        self.list1 = OptionBox(
    0, 0, 300, 100, (255, 255, 255), (100, 200, 255), AssetsLoader.getFont("midfont"), ['One', 'Two', 'Three', '4. Very Long Option'])
        
        self.button1 = PushButton(
    300, 0, 300, 100, (255, 255, 255), (100, 200, 255), AssetsLoader.getFont("midfont"), 
    "BUTTON")
        

    def firstDisplay(self, screen : pygame.Surface):
        # Display only once when the state is created
        self.refreshOnce()
    
    def refreshOnce(self):
        # Function to refresh the titles once
        # Trigger only when the titles are changed
        self.screen.blit(self.bg, (0, 0))       
        self.list1.draw(self.screen)
        pygame.display.update()

    def handle(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        selected_option = self.list1.update(event)
        button_pressed = self.button1.update(event)
        if selected_option >=0:
            # Set locale and refresh the titles
            LocaleManager.setLocale(selected_option)
            self.refreshOnce()
        if button_pressed:
            print("PRESSED ON BUTTON 1")

    def update(self, game):
        # Clear the background
        self.screen.blit(self.bg, (0, 0))
        updates = [self.button1.draw(self.screen)]
        updates.extend(self.list1.draw(self.screen))
        pygame.display.update(updates)