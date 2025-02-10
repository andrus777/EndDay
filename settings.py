class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 20)
        self.game_caption = "Alien Invasion"

        self.ship_speed = 1.5
        self.ship_flame = 0.2

        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 255, 255, 102
        self.bullets_allowed = 3

        self.max_stars = 400
        self.star_speed = 2

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


