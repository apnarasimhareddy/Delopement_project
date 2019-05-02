import pygame
from pygame.sprite import Sprite

#a class manage to bullet from ship
class Bullet(Sprite):
    #create bullet object at ship current position
    def __init__(self,screen,setting,ship):

        #create the Sprite instances
        super(Bullet,self).__init__()
        self.screen=screen

        #create bullet positon(0,0)set the correct position
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)

        #set bullet position as it is ship position
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #store the bullet position at decimal value
        self.y=float(self.rect.y)

        #set bullet color
        self.color=setting.bullet_color

        #set bullet speed
        self.speed=setting.bullet_speed

    def update(self):
        """move the bullet up to screen"""
        #update the decimal position of bullet
        self.y -=self.speed

        #update the rect position
        self.rect.y=self.y


    #draw the bullet to screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)