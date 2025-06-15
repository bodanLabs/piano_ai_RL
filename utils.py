
import pygame
import os

pygame.init()
pygame.mixer.init()

NOTE_FILES = {
    'C4': 'sounds/C4.mp3',
    'E4': 'sounds/E4.mp3',
    'A4': 'sounds/A4.mp3',
    'B4': 'sounds/B4.mp3',
    'G4': 'sounds/G4.mp3',
    'C5': 'sounds/C5.mp3',
    'D5': 'sounds/D5.mp3',
    'D#5': 'sounds/Ds5.mp3',
    'E5': 'sounds/E5.mp3'
}
current_note = None  # Global tracker for visual display


def play_note(note):
    global current_note
    current_note = note
    if note in NOTE_FILES and os.path.exists(NOTE_FILES[note]):
        sound = pygame.mixer.Sound(NOTE_FILES[note])
        sound.play()
