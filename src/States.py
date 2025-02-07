import sys
import pygame
import random

from .AssetsLoader import AssetsLoader
from .LocaleManager import LocaleManager
from .OptionBox import OptionBox
from .PushButton import PushButton
from .SwitchButton import SwitchButton
from .LabelBox import LabelBox
from .Gauge import Gauge

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
    0, 100, 300, 50, (255, 255, 255), (100, 200, 255), AssetsLoader.getFont("smallfont"), ['One', 'Two', 'Three', 'Four. Very Very Long Option Text'])
        
        self.gauge1 = Gauge(
    0, 400, 600, 50, (255, 255, 255), (100, 200, 255), 50, 0, 100, True, AssetsLoader.getFont("smallfont"))

        self.btn_ok = PushButton(
    0, 668, 512, 50, (255, 255, 255), (100, 200, 255), AssetsLoader.getFont("smallfont"), "Confirm")
        
        self.btn_cancel = PushButton(
    512, 668, 512, 50, (255, 255, 255), (100, 200, 255), AssetsLoader.getFont("smallfont"), "Cancel")
        
        self.btn_switch = SwitchButton(
    300, 100, 300, 50, (255, 255, 255), (100, 200, 255), AssetsLoader.getFont("smallfont"), 
    "YES", "NO", False)
        
        self.label1 = LabelBox(0, 0, 1024, 80, "LightGUI demo", font=AssetsLoader.getFont("midfont"))

    def firstDisplay(self, screen : pygame.Surface):
        # Display only once when the state is created
        self.screen.blit(self.bg, (0, 0))
        pygame.display.flip()
    

    def handle(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        selected_option = self.list1.update(event)
        btn_ok_pressed = self.btn_ok.update(event)
        btn_cancel_pressed = self.btn_cancel.update(event)
        btn_switch_on = self.btn_switch.update(event)
        gauge_curr_val = self.gauge1.update(event)

        if selected_option >=0:
            # Set locale and refresh the titles
            LocaleManager.setLocale(selected_option)
            self.update(None)
        if btn_ok_pressed:
            print("PRESSED ON CONFIRM BUTTON")
        if btn_cancel_pressed:
            print("PRESSED ON CANCEL BUTTON")


    def update(self, game):
        # Clear the background
        self.screen.blit(self.bg, (0, 0))
        updates = [self.btn_ok.draw(self.screen)]
        updates.append(self.btn_cancel.draw(self.screen))
        updates.append(self.btn_switch.draw(self.screen))
        updates.append(self.label1.draw(self.screen))
        updates.append(self.gauge1.draw(self.screen))
        updates.extend(self.list1.draw(self.screen))
        pygame.display.update(updates)