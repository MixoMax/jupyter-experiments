# random 12 ton technik pattern generator

import random
import time
import winsound


note_lookup = {
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "H": 493.88
}


class Note:
    pitch: str # pitch name (C, C#, D, D#, E, F, F#, G, G#, A, A#, H)
    octave: int # octave number (0-8)
    duration: int # duration in 16th notes (1-16)
    
    def __init__(self, pitch: str, octave: int = 4, duration: int = 4):
        self.pitch = pitch
        self.octave = octave
        self.duration = duration
    
    def __str__(self):
        return f"{self.pitch}{self.octave}:{self.duration}"
    
    def play(self):
        freq = note_lookup[self.pitch] * (2 ** (self.octave - 4))
        duration = int(1000 * (60 / 120) * (4 / self.duration))
        
        print(freq)
        
        winsound.Beep(int(freq), duration)


notes = []
unused_notes = list(note_lookup.keys())

for i in range(12):
    pitch = random.choice(unused_notes)
    unused_notes.remove(pitch)
    octave = random.choice([3, 4, 5])
    duration = random.choice([1, 2, 4, 8])
    notes.append(Note(pitch, octave, duration))


for note in notes:
    print(note)
    note.play()
    time.sleep(note.duration / 4)
