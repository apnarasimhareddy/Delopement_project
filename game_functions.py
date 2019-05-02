import sys
import pygame
from bullet import Bullet
from aeroplane import Aeroplane
from time import sleep

#create the keydown events
def get_keydown_events(event,screen,setting,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.move_right=True

    if event.key==pygame.K_LEFT:
        ship.move_left=True

    if event.key==pygame.K_SPACE:
        #create the new bullet and add bullets broup.
        if len(bullets)<setting.bullet_allowed:
            new_bullet=Bullet(screen,setting,ship)
            bullets.add(new_bullet)

    #press the Q game exit
    if event.key==pygame.K_q:
        sys.exit()

#create the keyup events
def get_keyup_events(event,screen,setting,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.move_right=False

    if event.key==pygame.K_LEFT:
        ship.move_left=False

#start game when player click the play
def check_play_buttons(setting,screen,ship,aeroplane,bullets,stats,play_button,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #hide mouse cursor
        #reset game
        setting.initialize_dynamic_setting()
        pygame.mouse.set_visible(False)
        #reset game
        stats.reset_stats()
        stats.game_active=True

        #empty the list of aeroplane and bullets
        aeroplane.empty()
        bullets.empty()

        #create new fleet and center the ship
        create_fleet(setting,screen,aeroplane)
        ship.ship_center()


#create the game events
def get_events(screen,setting,ship,aeroplane,bullets,stats,play_button):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            get_keydown_events(event,screen,setting,ship,bullets)

        if event.type==pygame.KEYUP:
            get_keyup_events(event,screen,setting,ship,bullets)

        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_buttons(setting,screen,ship,aeroplane,bullets,stats,play_button,mouse_x,mouse_y)

#set background color
#load the image
#make the most recent drawn screen visible
def screen_update(setting,screen,ship,bullets,aeroplane,stats,play_button,sb):
    screen.fill(setting.bg_color)

    #redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.builtme()
    #aeroplane.blitme()
    aeroplane.draw(screen)
    sb.show_score()

    #draw play button game is inactive
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

#redraw bullets and remove the bullets after top of screen
def update_bullet(bullets,aeroplane,setting,screen,stats,sb):
    bullets.update()
    #check any bullet that have hit aeroplane
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_aeroplane_collision(setting,screen,aeroplane,bullets,stats,sb)

#remove any bullet aeroplane collided
def check_bullet_aeroplane_collision(setting,screen,aeroplane,bullets,stats,sb):
    collisions=pygame.sprite.groupcollide(bullets,aeroplane,True,True)
    if collisions:
        for aeroplanes in collisions.values():
            stats.score +=setting.aeroplane_points*len(aeroplane)
            sb.prep_score()
        #check_high_score(stats,sb)

    if len(aeroplane)==0:
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting,screen,aeroplane)

#create fleet of aeroplanes in one row
def get_number_aeroplanes_x(setting,aeroplanes_width):
    avaible_space_x = setting.width - 2 * aeroplanes_width
    number_aeroplanes_x = int(avaible_space_x / (2 * aeroplanes_width))
    return number_aeroplanes_x

#create first row of aeroplanes
def create_aeroplane(setting,screen,aeroplane,aeroplane_number,row_number):
    aeroplanes = Aeroplane(screen, setting)
    aeroplanes_width = aeroplanes.rect.width
    aeroplanes.x = aeroplanes_width + 2 * aeroplanes_width * aeroplane_number
    aeroplanes.rect.x = aeroplanes.x
    aeroplanes.y = aeroplanes.rect.height + 2 * aeroplanes.rect.height * row_number
    aeroplanes.rect.y=aeroplanes.y
    aeroplane.add(aeroplanes)

#determine number row of aeroplane of that fit on the screeen
def get_number_row_y(setting,aeroplane_height):
    aviable_space_y=(setting.height-(3*aeroplane_height))
    number_row=int(aviable_space_y/(3*aeroplane_height))
    return number_row

#create fleet of aeroplanes
def create_fleet(setting,screen,aeroplane):
    """create full fleet of line"""
    #create aeroplane and find number aeroplane set in row
    #spaceng between each aeroplane and equal each others
    aeroplanes=Aeroplane(screen,setting)
    number_aeroplanes_x=get_number_aeroplanes_x(setting,aeroplanes.rect.width)
    get_number_rows=get_number_row_y(setting,aeroplanes.rect.height)

    #create number row of aeroplanes
    for row_number in range(get_number_rows):
        for aeroplane_number in range(number_aeroplanes_x):
            create_aeroplane(setting,screen,aeroplane,aeroplane_number,row_number)

def update_aeroplane(setting,screen,bullets,aeroplane,ship,stats):
    aeroplane.update()
    check_fleet_edges(setting,aeroplane,screen)
    if pygame.sprite.spritecollideany(ship,aeroplane):
        ship_hit(setting,screen,ship,aeroplane,bullets,stats)
        #print('ship hit')
        #look aeroplane hitting the bottom of screen
    check_aeroplane_bottom(screen, setting, ship, aeroplane, bullets, stats)

#respondes appropriately if any aeroplane reached edge
def check_fleet_edges(setting,aeroplane,screen):
    for aeroplanes in aeroplane.sprites():
        if aeroplanes.check_edges():
            change_fleet_direction(setting,aeroplane,screen)
            break

#drop the entri fleet and change the direction
def change_fleet_direction(setting,aeroplane,screen):
    for aeroplanes in aeroplane.sprites():
        aeroplanes.rect.y +=setting.fleet_drop_speed
        setting.fleet_direction *=-1

def ship_hit(setting,screen,ship,aeroplane,bullets,stats):
    """respond to ship being hit by aeroplane"""
    #determine ship left
    if stats.ship_left>0:
        stats.ship_left -=1

        #empty of the ship and aeroplane
        aeroplane.empty()
        bullets.empty()

        #create new fleet and ship
        create_fleet(setting,screen,aeroplane)
        ship.ship_center()

        #pase
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

#check if any aeroplane reach the bottom
def check_aeroplane_bottom(screen,setting,ship,aeroplane,bullets,stats):
    screen_rect=screen.get_rect()
    for aeroplanes in aeroplane.sprites():
        if aeroplanes.rect.bottom >= screen_rect.bottom:
            ship_hit(setting,screen,ship,aeroplane,bullets,stats)
            break
            #same as ship got it

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score=stats.score
        sb.prep_score()

