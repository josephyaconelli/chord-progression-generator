from HarmonicFunction import HarmonicFunction
from consts import Keys as KeyConsts
from classes.Chord import Chord
import random

class Tonic(HarmonicFunction):
    
    stable = [1]
    unstable = [5]

    chords = stable + unstable

    def __init__(self, key):
        self.key = key
        self.currDegree = -1

    def getFirst(self):
        self.currDegree = stable[0]
        return self.key.getChord(stable[0])

    def getNext(self, currentChord, probabiltiy = 1.):
        prob = random.random()

        if 
