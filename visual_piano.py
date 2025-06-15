import pygame
import time
from utils import current_note

pygame.init()
screen = pygame.display.set_mode((700, 200))
pygame.display.set_caption("AI Piano Player")

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
key_width = 100
font = pygame.font.SysFont(None, 36)

def draw_piano(active_note=None):
    screen.fill((0, 0, 0))
    for i, note in enumerate(notes):
        x = i * key_width
        color = (255, 255, 255)
        if note == active_note:
            color = (255, 200, 200)
        pygame.draw.rect(screen, color, (x, 50, key_width - 5, 100))
        text = font.render(note, True, (0, 0, 0))
        screen.blit(text, (x + 35, 90))
    pygame.display.flip()

def visual_loop():
    while True:
        draw_piano(current_note)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        time.sleep(0.1)
