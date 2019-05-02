import pygame
class Ship:
    def __init__(self,screen,setting):
        self.screen=screen
        self.setting=setting

        #load the image
        self.image=pygame.image.load('image/ship.bmp')

        #set ship shape in rectangular
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start new ship at bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #self.rect.right=self.screen_rect.right

        #coverting to the floating value
        self.center=float(self.rect.centerx)

        #ship moves left and right
        self.move_right=False
        self.move_left=False

    #blit the image
    def builtme(self):
        self.screen.blit(self.image,self.rect)

    #create the ship moves
    def ship_moves(self):
        if self.move_right and self.rect.right<self.screen_rect.right:
            self.center +=self.setting.ship_speed
        if self.move_left and self.rect.left>self.screen_rect.left:
            self.center -=self.setting.ship_speed
        self.rect.centerx=self.center

    #create center ship
    def ship_center(self):
        self.centerx=self.screen_rect.centerx