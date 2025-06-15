
TARGET_MELODY = ['E5', 'D#5', 'E5', 'D#5', 'E5', 'B4', 'D5', 'C5', 'A4', 'C4', 'E4', 'A4', 'B4', 'E4','G4', 'B4', 'C5','E4']

def compute_reward(played_sequence):
    score = 0
    for i in range(min(len(played_sequence), len(TARGET_MELODY))):
        if played_sequence[i] == TARGET_MELODY[i]:
            score += 1.0
        else:
            score -= 1.0
    return score
