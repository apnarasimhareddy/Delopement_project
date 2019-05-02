import pygame
from pygame.sprite import Sprite

#A class represent single aeroplane in fleet
class Aeroplane(Sprite):
    def __init__(self,screen,setting):
        super(Aeroplane,self).__init__()
        self.screen=screen
        self.setting=setting

        #load the image and set rectangular atribute
        self.image=pygame.image.load('image/aeroplane.bmp')
        self.rect=self.image.get_rect()

        #start new aeroplane top left of screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #store aeroplane exact positon
        self.x=float(self.rect.x)

    #draw the aeroplane current location
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    #move aeroplane rght
    def update(self):
        self.x -=self.setting.aeroplane_speed*self.setting.fleet_direction
        self.rect.x=self.x

    #return the true aeroplane touch the edge
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right==screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
