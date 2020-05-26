__author__ = 'Gabriel'
import pygame
from GenericAlienFile import GenericAlien

class Row0Alien(GenericAlien):
    def __init__(self, x, y):
      super().__init__(x,y)
      self.alien_frames_list.append(pygame.image.load("images/AlienRow0v1.PNG"))
      self.alien_frames_list.append(pygame.image.load("images/AlienRow0v2.PNG"))
      self.width = self.alien_frames_list[0].get_rect().width
      self.height = self.alien_frames_list[0].get_rect().height
      self.width = 80

