__author__ = 'Gabriel'
import pygame
from GenericAlienFile import GenericAlien


class Second_And_Third_Alien(GenericAlien):
    def __init__(self, x, y):
      super().__init__(x,y)
      self.alien_frames_list.append(pygame.image.load("images/AlienRow1-2v1.PNG"))
      self.alien_frames_list.append(pygame.image.load("images/AlienRow1-2v2.PNG"))
      self.width = self.alien_frames_list[0].get_rect().width
      self.height = self.alien_frames_list[0].get_rect().height