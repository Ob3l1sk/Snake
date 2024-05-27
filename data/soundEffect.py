import pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

mainSong = pygame.mixer.Sound('C:/Users/dalto/Desktop/Python Programs/Games/Snake/data/Sound/mainLoop.wav')

nom = pygame.mixer.Sound('C:/Users/dalto/Desktop/Python Programs/Games/Snake/data/Sound/Nom.wav')