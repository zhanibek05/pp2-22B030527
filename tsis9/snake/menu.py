import pygame, sys

pygame.init()

screen = pygame.display.set_mode((625, 625))

def Menu():
    menu_screen = pygame.Surface((300, 300))
    
    class Button():
        def __init__(self, name, y):
            self.name = name
            self.y = y
            self.surface = pygame.Surface((150, 50))
            self.rect = self.surface.get_rect()
            self.rect.center = (170, self.y)
        def draw(self):
            font = pygame.font.SysFont("Verdana", 30)
            self.surface.blit(font.render(self.name))
            menu_screen.blit(self.surface, self.rect)
            
            
    play_button = Button("Play", 160)
    Buttons = [
        play_button,
        
    ]
            
    while True:
        menu_screen.fill((255, 255, 255))
        screen.blit(menu_screen, (150, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    pass
        pygame.display.update()
        
Menu()