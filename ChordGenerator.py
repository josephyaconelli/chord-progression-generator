from ChordGraph import ChordGraph


class ChordGenerator:
    notes        = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # no flats
    majorPattern = [2, 2, 1, 2, 2, 2, 1]
    minorPattern = [2, 1, 2, 2, 1, 2, 2]  # natural minor
    majorChords  = [None, 'I', 'ii', 'iii', 'IV', 'V', 'vi', 'viio/']
    minorChords  = [None, 'i', 'iio', 'III', 'iv', 'V', 'VI', 'VII']
    inversion    = [[None, '7'], ['6', '65'], ['64','43'], [None, '42']] # [triad, seventh]
    degrees      = [None, [(1,1,True)],[(2,1,True), (5,3,True), ()],[],[],[],[],[]] # [(chord, inversion, isTriad (else seventh)), (...)] ...


    def __init__(self, key = 'C', isMajor=True):

        self.keyCenter = key
        self.isMajor   = isMajor
        self.pattern   =  ChordGenerator.majorPattern if self.isMajor else ChordGenerator.minorPattern
        self.chords    =  ChordGenerator.majorChords  if self.isMajor else ChordGenerator.minorChords
        self.keyOffset = ChordGenerator.notes.index(self.keyCenter)
        self.setup_tonic_graph()
        
    def setup_tonic_graph(self):
       # create graph 
        self.tonic_graph = ChordGraph()
        self.tonic_graph.add_node(self.chords[1], [self.chords[2], self.chords[3]])

        for chord in self.tonic_graph.nodes:
            print(chord)

