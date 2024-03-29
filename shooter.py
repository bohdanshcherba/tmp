#Створи власний Шутер!
from pygame import *
from random import randint
import time as timer
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
      
        self.speed = player_speed 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]== True:
            self.rect.x = self.rect.x-self.speed
        if keys[K_RIGHT]:
            self.rect.x = self.rect.x+self.speed
        #рух вправо вліво

    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top, 15,20,3)
        bullets.add(bullet)

lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global lost

        if self.rect.y >= 450:
            lost = lost + 1
            self.rect.y = 0
            self.rect.x = randint(50,650)
            self.speed = randint(1,2)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y <= 0:
            self.kill()

monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()


for i in range(1,6):
    monster = Enemy("ufo.png", randint(50,650), 0, 50,50, randint(1,2))
    monsters.add(monster)

for i in range(1,6):
    esteroid = Enemy("asteroid.png", randint(50,650), 0, 50,50, randint(1,5))
    asteroids.add(esteroid)


win_width = 700
win_height = 500

display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load(img_back), (win_width, win_height))

run = True  # прапорець скидається кнопкою закриття вікна
finish = False

clock = time.Clock()
FPS = 60

hero = Player(img_hero,350,450,50,50,5)

#шрифт
font.init()
font = font.SysFont('Arial',24)

score = 0
lifes = 3

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
    if not finish:
        window.blit(background, (0, 0))

        hero.reset()
        hero.move()

        bullets.draw(window)
        bullets.update()

        monsters.draw(window)
        monsters.update()

        asteroids.draw(window)
        asteroids.update()


        text = font.render("Пропущено: " + str(lost), True, (255,255,255))

        window.blit(text,(20,20))
    
        collides = sprite.groupcollide(monsters, bullets, True, True)

        for c in collides:
            score = score + 1 
            monster = Enemy("ufo.png", randint(50,650), 0, 50,50, randint(1,2))
            monsters.add(monster)

        if sprite.spritecollide(hero, monsters, False) or sprite.spritecollide(hero, asteroids, False):
            
            sprite.spritecollide(hero, monsters, True)
            sprite.spritecollide(hero, asteroids, True)
            lifes = lifes - 1

        if lifes == 3:
            color = (0,255,0)
        elif lifes == 2:
            color = (255,255,0)
        else:
            color = (255,0,0)

        text = font.render(str(lifes), True, color)
        window.blit(text, (650, 20))

        if lifes == 0:
            finish = True  

    else:
        finish = False
        score = 0
        lost = 0
        lifes = 3

        for b in bullets:
            b.kill()
        
        for m in monsters:
            m.kill()

        for a in asteroids:
            a.kill()

        timer.sleep(3)

        for i in range(1,6):
            monster = Enemy("ufo.png", randint(50,650), 0, 50,50, randint(1,2))
            monsters.add(monster)
        for i in range(1,6):
            asteroid = Enemy("ufo.png", randint(50,650), 0, 50,50, randint(1,2))
            asteroids.add(asteroid)

    display.update()
    clock.tick(FPS)
