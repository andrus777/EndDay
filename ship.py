import pygame

class Ship():
    def __init__(self, ai_game):
        # Инициализирует корабль и задает его начальную позицию
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник
        self.images = pygame.image.load('images/ships5_2.png')
        self.anim = []
        self.fill_anim()
        # print(self.anim)
        self.current_img = 4
        self.rect = self.anim[self.current_img].get_rect()

        # Каждый новый корабль появляется у края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    def fill_anim(self):
        for i in range(5):
            self.anim.append(pygame.transform.smoothscale(self.images.subsurface(pygame.Rect(152 * i , 0, 150, 207)), (100, 130)))


    def update_image(self):
        if self.current_img < 4:
            self.current_img += 1
        else:
            self.current_img = 0

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
        self.image = self.anim[self.current_img]

    def blitime(self):
        # Рисует корабль в текущей позиции
        self.update_image()
        self.screen.blit(self.anim[self.current_img], self.rect)







