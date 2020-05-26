__author__ = 'Gabriel'
import pygame

SECONDS_PER_FRAME = 0.75
NUMBER_OF_FRAMES = 2


class GenericAlien:
    def __init__(self, x, y):
        """
        This is where we set up the variables for this particular object as soon as it is created.
        """
        self.x = x
        self.y = y
        self.vx = 50
        self.vy = 0
        self.i_am_alive = True
        self.alien_frames_list = []
        self.current_frame = 0
        self.time_since_last_animation = 0
        # self.width = self.alien_frames_list[0].get_rect().width
        # self.height = self.alien_frames_list[0].get_rect().height
        self.direction = 1 # 1 is right -1 is left

    def draw_self(self, screen_canvas):
        """
        It is this object's responsibility to draw itself on the surface. It will be told to do this often!
        :param screen_canvas:
        :return: None
        """


        screen_canvas.blit(self.alien_frames_list[self.current_frame],
                           (int(self.x) - self.width / 2, int(self.y) - self.height / 2))

    def step(self, delta_T):
        """
        In order to change over time, this method gets called very often. The delta_T variable is the amount of time it
        has been since the last time we called "step()" usually about 1/20 -1/60 of a second.
        :param delta_T:
        :return: None
        """
        # self.x = self.x + self.vx * delta_T
        # self.y = self.y + self.vy * delta_T

        self.time_since_last_animation += delta_T
        if self.time_since_last_animation > SECONDS_PER_FRAME:
            self.time_since_last_animation -= SECONDS_PER_FRAME
            self.current_frame = (self.current_frame + 1)%NUMBER_OF_FRAMES
            self.x += 80 * self.direction
            if self.x +self.width/2 > 1400:
                self.direction *= -1
                self.y += 60
            if self.x - self.width/2 < 0:
                self.direction *= -1
                self.y += 60
    def is_dead(self):
        """
        lets another object know whether this object is still live and on the board. Used by the main loop to clear objects
        in need of removal.
        :return: True or False - is this object dead?
        """
        return not self.i_am_alive


    def die(self):
        """
        change the status of this object so that it is dead.
        :return: None
        """
        self.i_am_alive = False