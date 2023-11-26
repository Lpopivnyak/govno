import pygame
import sys

pygame.init()
window = pygame.display.set_mode((1370, 705))
fps = pygame.time.Clock()

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (1370, 705))

character1 = pygame.image.load("sprite1.png")
character1 = pygame.transform.scale(character1, (100, 100))
x1, y1 = 50, 50

character2 = pygame.image.load("background.png")
character2 = pygame.transform.scale(character2, (100, 100))

while True:
    #обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x1 += 5


    window.blit(backgroundImage, [0, 0])
    window.blit(character1, [x1, y1])
    pygame.display.flip()
    fps.tick(60)