#Создай собственный Шутер!

from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

#mixer.init()
#mixer.music.load('sans.mp3')
#mixer.music.play(loops=-1)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        
    def fire(self):
        bullet = Bullet('dragon.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
        
player = Player('shef.jpg', 300, 440, 50, 50, 15)
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
    monsters.add(monster)
bullets = sprite.Group()

clock = time.Clock()
game = True
FPS = 60
lost = 0
score = 0  

font.init()
font1 = font.SysFont('Arial', 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    window.blit(background, (0, 0))
    score_text = font1.render('Счёт: ' + str(score), 1, (255, 255, 255))
    window.blit(score_text, (20, 20))
    text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (20, 60))

    player.reset()

    if sprite.groupcollide(monsters, bullets, True, True):
        score += 1
        monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
        monsters.add(monster)

    if sprite.spritecollide(player, monsters, False):
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        player = Player('shef.jpg', 300, 440, 50, 50, 15)
        monsters = sprite.Group()
        for i in range(1, 6):
            monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
            monsters.add(monster)
        bullets = sprite.Group()
    
    if score == 100:
        for m in monsters:
            m.kill()
        for i in range(1, 9):
            monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
            monsters.add(monster)

    if score == 150:
        for m in monsters:
            m.kill()
        for i in range(1, 21):
            monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
            monsters.add(monster)

    if score == 200:
        for m in monsters:
            m.kill()
        for i in range(1, 100):
            monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
            monsters.add(monster)

    if score == 250:
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        player = Player('shef.jpg', 300, 440, 50, 50, 15)
        monsters = sprite.Group()
        for i in range(1, 6):
            monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
            monsters.add(monster)
        bullets = sprite.Group()

    if lost == 10:
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        player = Player('shef.jpg', 300, 440, 50, 50, 15)
        monsters = sprite.Group()
        for i in range(1, 6):
            monster = Enemy('eldorado.jpg', randint(80, win_width - 80), -40 , 80, 50, randint(1, 5))
            monsters.add(monster)
        bullets = sprite.Group()

    time.delay(40)

    player.update()
    player.reset()

    monsters.update()
    monsters.draw(window)

    bullets.update()
    bullets.draw(window)

    display.update()
    clock.tick(FPS)
