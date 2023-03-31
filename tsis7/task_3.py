import pygame

pygame.init()

W = 500
H = 500
screen = pygame.display.set_mode(size=(W, H))
pygame.display.set_caption("red ball")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

X = W/2
Y = H/2

running = True

while running:
    screen.fill(WHITE)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        X -= 20
    if keys[pygame.K_RIGHT]:
        X += 20
    if keys[pygame.K_DOWN]:
        Y += 20
    if keys[pygame.K_UP]:
        Y -= 20
    
    if X - 20 <= 0:
        X += 20
    if X + 20 >= W:
        X -= 20
    if Y + 20 >= H:
        Y -= 20
    if Y - 20 <= 0:
        Y += 20    
    
    pygame.draw.circle(surface=screen,
                       color=RED,
                       center=(X, Y), radius=25)
    
    pygame.display.flip()  
    clock.tick(30)