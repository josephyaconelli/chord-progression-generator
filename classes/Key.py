

from consts import Keys as KeyConsts
from classes.Chord import Chord

class Key:

    def __init__(self, center = 'C', isMajor = True):
        self.center = center.upper()
        self.scale  = KeyConsts.majorScale if isMajor else KeyConsts.minorScale
        self.chords = KeyConsts.majorChords if isMajor else KeyConsts.minorChords
        self.isMajor = isMajor


    def __str__(self):
        return self.center + (' major' if self.isMajor else ' minor')


    def getChord(self, degree, isTriad = True, inversion = 0):
         quality = self.chords[degree]
         return Chord(degree, quality, isTriad, inversion)

