import pygame
import random
import time

pygame.init()

GREEN = [3, 252, 65]
SIZE = [400, 400]

shipSpeed = 4
meteorSpeed = 2

scoreTime = 0
scoreDelay = 420
score = 0

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Deszcz meteorów")

shipImg = pygame.image.load("spaceship.png")
shipImg = pygame.transform.scale(shipImg, (35, 50))

meteorImg = pygame.image.load("meteor.png")
meteorImg = pygame.transform.scale(meteorImg, (30, 30))

background = pygame.image.load("space.png")
explosion = pygame.image.load("explosion.png")
explosion = pygame.transform.scale(explosion, (50, 50))

meteorFall = []
for i in range(20):
    x = random.randrange(0, 400)
    y = random.randrange(-400, 0)
    meteorFall.append([x, y])

shipX = 175
shipY = 325


def game_over():
    font = pygame.font.SysFont('Arial', 40)
    gameOverText = font.render('Wynik końcowy: ' + str(score), True, GREEN)
    gameOverRect = gameOverText.get_rect()
    gameOverRect.midtop = (200, 150)
    screen.blit(gameOverText, gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


clock = pygame.time.Clock()
done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shipX -= shipSpeed
        if shipX < 0:
            shipX = 0
    elif keys[pygame.K_RIGHT]:
        shipX += shipSpeed
        if shipX > 365:
            shipX = 365
    elif keys[pygame.K_UP]:
        shipY -= shipSpeed
        if shipY < 0:
            shipY = 0
    elif keys[pygame.K_DOWN]:
        shipY += shipSpeed
        if shipY > 350:
            shipY = 350

    screen.blit(background, (0, 0))

    screen.blit(shipImg, (shipX, shipY))

    for i in range(len(meteorFall)):
        screen.blit(meteorImg, (meteorFall[i][0], meteorFall[i][1]))

        meteorFall[i][1] += meteorSpeed
        if meteorFall[i][1] > 400:
            y = random.randrange(-50, -10)
            meteorFall[i][1] = y

            x = random.randrange(0, 400)
            meteorFall[i][0] = x

    shipRect = pygame.Rect(shipX, shipY, 30, 40)

    for meteor in meteorFall:
        meteorRect = pygame.Rect(meteor[0], meteor[1], 20, 20)
        if shipRect.colliderect(meteorRect):
            explosion_pos = [shipX, shipY]
            screen.blit(explosion, explosion_pos)
            pygame.display.update()
            game_over()
            break

    scoreTime += clock.tick(60)
    if scoreTime > scoreDelay:
        score += 1
        scoreTime = 0

    scoreFont = pygame.font.SysFont("Arial", 20)
    scoreText = scoreFont.render("Wynik: " + str(score), True, GREEN)
    screen.blit(scoreText, [0, 0])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
