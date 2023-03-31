import pygame

pygame.init()
HEIGHT, WIDTH = 800, 800
screen = pygame.display.set_mode(size=(HEIGHT, WIDTH))
surface = pygame.Surface((400, 400), pygame.SRCALPHA)
image = pygame.image.load('task_1/images/body.jpeg')
second = pygame.image.load('task_1/images/second.png')
minute = pygame.image.load('task_1/images/minute.png')
done = False
clock = pygame.time.Clock()
second = pygame.transform.rotate(second, 90)
a1 = 360
a2 = 360


while not done:
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    min = pygame.transform.rotate(minute, a1)
    rect3 = min.get_rect(center=(400, 400))
    screen.blit(min, rect3)
    sec = pygame.transform.rotate(second, a2)
    rect4 = sec.get_rect(center=(400, 400))
    screen.blit(sec, rect4)
    if a1 > 0:
        a1 -= 1
    else:
        a1 = 360
        a2 -= 6
    if a2 <= 0:
        a2 = 360

    pygame.display.flip()
    clock.tick(30)