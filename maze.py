from pygame import*

window = display.set_mode((1000, 650))
display.set_caption('Лапиринд')
background = transform.scale(image.load("background.jpg"), (1000, 650))

finish = False

clock = time.Clock()
FPS = 15

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, spid):
        super().__init__()
        self.image = transform.scale(image.load(image1), (70, 70))
        self.speed = spid
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 950:
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
        
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x < 750 :
            self.direction = 'right'
        if self.rect.x > 950 :
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else :
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__ (self, width, height, color_1, color_2, color_3, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font = font.Font(None, 140)
gameover = font.render('GAME OVER', True, (255, 0, 0))
youwin = font.render('U WIN', True, (0, 255, 0))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

hero = Player("hero.png", 100, 100, 10)

cyborg = Enemy("cyborg.png", 950, 400, 15)

treasure = GameSprite("treasure.png", 900, 550, 0)

wall = Wall(17, 700, 221, 66, 255, 200, 235)
wall2 = Wall(15, 700, 77, 67, 246, 300, -150)
wall3 = Wall(15, 1000, 63, 23, 135, 400, 300)
wall4 = Wall(15, 800, 22, 42, 135, 400, -600)
wall5 = Wall(150, 15, 4, 81, 111, 450, 200)
wall6 = Wall(150, 15, 8,99, 86, 450, 300)
wall7 = Wall(15, 700, 6, 0, 0, 700, 100)


game = True
while game:
    
    clock.tick(FPS)
    if finish != True:
        window.blit(background, (0, 0))    
        hero.update()
        cyborg.update()
        treasure.update()


        hero.reset()
        cyborg.reset()
        treasure.reset()
        wall.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        wall5.reset()
        wall6.reset()
        wall7.reset()
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7):
                    window.blit(gameover, (200, 200))
                    kick.play()
                    finish = True
        if sprite.collide_rect(hero, treasure):
                    window.blit(youwin, (300, 200))
                    money.play()
                    finish = True
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
        

    display.update()
    