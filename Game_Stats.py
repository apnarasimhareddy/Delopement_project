class Gamestats:
    def __init__(self,setting):
        self.setting=setting
        self.game_active=False
        self.reset_stats()
        self.high_score=0
    #Initialize statistics that can change during game
    def reset_stats(self):
        self.ship_left=self.setting.ship_limit
        self.score=0
        
