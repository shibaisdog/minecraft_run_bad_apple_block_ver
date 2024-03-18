import pygame
pygame.init()
pygame.mixer.init()
def play():
    sound = "./source/video.wav"
    so = pygame.mixer.Sound(sound)
    so.set_volume(0.5)
    so.play()