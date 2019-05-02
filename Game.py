import pygame #import pygame module
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from Game_Stats import Gamestats
from button import Button
from scoreboard import Scoreboard
from aeroplane import Aeroplane

def run_game():

    #install the game
    pygame.init()

    #create the instance of Settings
    setting=Settings()

    #create screen object and set screen size
    screen=pygame.display.set_mode((setting.width,setting.height))

    #make paly buttons
    paly_button=Button(setting,screen,'Play')

    #creste instance to store game statics
    stats=Gamestats(setting)

    #create instance of store game statics and create scoreboard
    sb=Scoreboard(setting,screen,stats)

    #create instance of ship
    ship=Ship(screen,setting)


    #make group store bullets and aeroplane
    bullets=Group()
    aeroplane=Group()

    #create a group fleet
    gf.create_fleet(setting,screen,aeroplane)

    #set the caption of the game
    pygame.display.set_caption('Game')

    # run game main loop
    while True:
        #install game events
        gf.get_events(screen,setting,ship,aeroplane,bullets,stats,paly_button)
        if stats.game_active:
            #install ship moves
            ship.ship_moves()

            #bullet position and get rid of old bullets
            gf.update_bullet(bullets,aeroplane,setting,screen,stats,sb)

            #update the aeroplane
            gf.update_aeroplane(setting,screen,bullets,aeroplane,ship,stats)

            #set background color and load ship image and make the most recent drawn screen visible
            #redraw all bullets behind ship
        gf.screen_update(setting,screen,ship,bullets,aeroplane,stats,paly_button,sb)
run_game()