import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

songs = ["16_qyz.mp3", "song2.mp3", "song3.mp3"]  
current_song = 0

pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(songs)
                play_music()
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(songs)
                play_music()

    pygame.display.flip()

pygame.quit()
sys.exit()
