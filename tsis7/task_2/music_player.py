import pygame

pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()


album = ("AC-DC - Back In Black.mp3",
         "AC-DC - Highway To Hell.mp3",
         "AC-DC - Thunderstruck.mp3")


is_playing = False
pygame.mixer.music.load("sounds/AC-DC - Back In Black.mp3")
pygame.mixer.music.play(0)
    

SONG_END = pygame.USEREVENT + 1
def playing(n):
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(f"sounds/{album[n]}")
    pygame.mixer.music.play(0)

i = 0
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Play or pause the music depending on the current state
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                pygame.quit()
                quit()
            elif event.key == pygame.K_LEFT:
                # Jump to the previous track in the playlist
                pygame.mixer.music.stop()
                i += 1
                if i > len(album) - 1:
                    i = 0
                playing(i)
            elif event.key == pygame.K_RIGHT:
                # Jump to the next track in the playlist
                pygame.mixer.music.stop()
                i -= 1
                if i < 0:
                    i = len(album) - 1
                playing(i)
   
    screen.fill((255, 255, 255))
    

    
    pygame.display.update()


    clock.tick(60)
