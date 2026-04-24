import pygame
import random
from pygame.locals import *

pygame.init()

# ---------------- SETTINGS ----------------
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
SPEED = 6

# Colors
NEON_PINK = (255, 20, 147)
NEON_BLUE = (0, 255, 255)
PURPLE = (120, 0, 255)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SWAG RACER 💜")

font_big = pygame.font.SysFont("Verdana", 28, True)
font_small = pygame.font.SysFont("Verdana", 18)

clock = pygame.time.Clock()

# ---------------- PLAYER CAR ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 90))
        self.rect = self.image.get_rect(center=(200, 600))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-7, 0)

        if keys[K_RIGHT] and self.rect.right < 400:
            self.rect.move_ip(7, 0)

# ---------------- ENEMY CAR ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 90))
        self.rect = self.image.get_rect(
            center=(random.randint(40, 360), 0)
        )

    def move(self):
        self.rect.move_ip(0, 6)

        if self.rect.top > 700:
            self.rect.center = (random.randint(40, 360), 0)

# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()

# ---------------- BACKGROUND ----------------
def draw_background(offset):
    screen.fill(BLACK)
    for i in range(0, SCREEN_HEIGHT, 40):
        pygame.draw.rect(screen, PURPLE, (190, i + offset, 20, 20))

# ---------------- SETUP ----------------
player = Player()
enemy = Enemy()
coin = Coin()

enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)
all_sprites = pygame.sprite.Group(player, enemy, coin)

coin_score = 0
offset = 0

# ---------------- GAME LOOP ----------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    player.move()
    enemy.move()
    coin.move()

    offset += 5
    if offset > 40:
        offset = 0

    # collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        running = False

    # coin collect
    if pygame.sprite.spritecollideany(player, coins):
        coin_score += 1
        coin.spawn()

    draw_background(offset)

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    text = font_small.render(f"💰 {coin_score}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH - 80, 10))

    pygame.display.update()
    clock.tick(60)

# ---------------- GAME OVER ----------------
screen.fill(BLACK)
font = pygame.font.SysFont("Verdana", 40, True)
text = font.render("GAME OVER", True, (255, 0, 0))
screen.blit(text, (80, 300))
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
