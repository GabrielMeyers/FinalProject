__author__ = 'Gabriel'
import pygame
from GenericAlienFile import GenericAlien


class Fourth_And_Fifth_Alien(GenericAlien):
    def __init__(self, x, y):
      super().__init__(x,y)
      self.alien_frames_list.append(pygame.image.load("images/AlienRow3-4v1.PNG"))
      self.alien_frames_list.append(pygame.image.load("images/AlienRow3-4v2.PNG"))
      self.width = self.alien_frames_list[0].get_rect().width
      self.height = self.alien_frames_list[0].get_rect().height
