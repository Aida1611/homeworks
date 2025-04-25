import pygame
pygame.init()

display = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Hi this ')
icon = pygame.image.load('image/maska.png')
pygame.display.set_icon(icon)

square = pygame.Surface((150, 175))
square.fill('red')

run = True
while run:

    display.blit(square, (70, 60))
    pygame.draw.circle(display, 'white')


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.guit()
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                display.fill((255, 255, 255))