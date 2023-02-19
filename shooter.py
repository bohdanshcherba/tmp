#Створи власний Шутер!
from pygame import *

# фонова музика
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"  # фон гри
img_hero = "rocket.png"  # герой
img_enemy = "ufo.png"  # ворог


class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
      
        self.speed = player_speed  self.image = transform.scale(image.load(player_image), (size_x, size_y))
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        #рух вправо вліво

class Enemy(GameSprite):
    def move(self):
        #рух вправо вліво

monsters = sprite.Group()
monsters.add()

win_width = 700
win_height = 500

display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load(img_back), (win_width, win_height))

run = True  # прапорець скидається кнопкою закриття вікна
clock = time.Clock()
FPS = 60

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0, 0))
    display.update()
    clock.tick(FPS)
