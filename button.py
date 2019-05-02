import pygame.font
class Button:
    def __init__(self,setting,screen,msg):
        self.setting=setting
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #set propeties of buttons
        self.width=200
        self.height=50
        self.button_color=(230,230,230)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,35)

        #build button's rect object and center
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #prepered button meassage only once
        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.image_msg=self.font.render(msg,True,self.text_color,self.button_color)
        self.image_msg_rect=self.image_msg.get_rect()
        self.image_msg_rect.center=self.rect.center

    #draw button and message
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.image_msg,self.image_msg_rect)

