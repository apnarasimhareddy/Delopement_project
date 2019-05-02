import pygame.font
class Scoreboard:

    #initialze scoreKeeping attributes
    def __init__(self,setting,screen,stats):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.setting=setting
        self.stats=stats

        #font setting for scoring information
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,35)

        #preper the initialze image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        round_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(round_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.setting.bg_color)

        #Display score at the top  right of the screen
        self.score_rect=self.score_image.get_rect()
        self.screen_rect.left=self.screen_rect.left
        self.screen_rect.top=10

     #Draw score to screen
    def show_score(self):
        self.screen.blit(self.score_image,self.screen_rect)
        #self.screen.blit(self.high_score_image,self.high_score_rect)

    def prep_high_score(self):
        high_score=int(round(self.stats.score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.setting.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.center=self.screen_rect.center
        self.high_score_rect.top=self.score_rect.top

