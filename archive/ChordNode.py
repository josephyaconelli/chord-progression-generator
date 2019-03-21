




class ChordNode:
    
    def __init__(self,chord):
        self.chord = chord
        self.nextChords = []    

    def add_next(self, nextChords):
        self.nextChords.extend(nextChords)

    def __str__(self):
        ret = ("Chord: " + str(self.chord) + '\n')
        for chord in self.nextChords:
            ret += "  Next: " + str(chord.chord) + '\n'

        return ret


    def __eq__(self, obj):
        return isinstance(obj, ChordNode) and obj.chord == self.chord


