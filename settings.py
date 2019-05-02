#creat the Game settings
class Settings:
    def __init__(self):
        self.height=715
        self.width=1365
        self.bg_color=(230,230,230)
        #self.ship_speed=2
        self.ship_limit=3
        #bullet settings
        self.bullet_height=15
        self.bullet_width=3
        #self.bullet_speed=5
        self.bullet_color=(60,60,60)
        self.bullet_allowed=10
        #self.aeroplane_speed=1
        self.fleet_drop_speed=20
        #fleet drection 1 represent the right -1 represents left
        #self.fleet_direction=1
        self.speedup_scale=1.1
        self.initialize_dynamic_setting()
        self.speed_scale=1.5

    #initialize settings throught the game
    def initialize_dynamic_setting(self):
        self.aeroplane_points=50
        self.ship_speed=2
        self.bullet_speed=3
        self.aeroplane_speed=1
        self.fleet_direction=1

    #Increase speed
    def increase_speed(self):
        self.ship_speed *=self.speedup_scale
        self.bullet_speed *=self.speedup_scale
        self.aeroplane_speed *=self.speedup_scale
        self.aeroplane_points=int(self.aeroplane_points*self.speed_scale)
