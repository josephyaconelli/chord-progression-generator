import functools
from consts import chords as chordConsts
from consts import Keys as KeyConsts

class Chord:

    def __init__(self, degree, quality, isTriad = True, inversion = 0):
        self.inversion = chordConsts.inversions['triad' if isTriad else 'seven'][inversion]
        self.degree = degree
        self.quality = quality

        # establish chord tones
        self.tones = [(x + degree - 1) % 7 for x in [1,3,5]] if isTriad else [(x + degree - 1) % 7 for x in [1,3,5,7]]
        # fix 0 == 7 issue
        self.tones = [x if x > 0 else 7 for x in self.tones]
        # rotate for inversion
        self.tones = self.tones[inversion:] + self.tones[:inversion]
        self.base = self.tones[0]


        print("TONES : ", self.tones)
        print("BASE : ", self.base)

    def toNumeral(self):
        numerals = [None, 'i','ii','iii','iv','v','vi','vii']
        numeral = numerals[self.degree]
        numeral = numeral.upper() if self.quality == KeyConsts.MAJOR or self.quality == KeyConsts.AUGMENTED else numeral.lower()
        if self.quality == KeyConsts.DIMINISHED:
            numeral += 'o'
        elif self.quality == KeyConsts.AUGMENTED:
            numeral += '+'
        
        numeral += str(self.inversion)
        return numeral


    def chordName(self, key):
        offset = functools.reduce(lambda a,b : a+b, key.scale[:self.degree])
        centerOffset = KeyConsts.notes['sharps'].index(key.center)
        print("OFFSET ", offset)
        name = KeyConsts.notes['sharps'][(centerOffset + offset) % len(KeyConsts.notes['sharps'])]
        return name

    def __str__(self):
        return self.toNumeral()
        
