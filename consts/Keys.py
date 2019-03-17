

notes = {'sharps': ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'],
         'flats' : ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']}

majorScale = [0, 2, 2, 1, 2, 2, 2, 1]
minorScale = [0, 2, 1, 2, 2, 1, 2, 2]

scales = {'major' : majorScale, 'minor' : minorScale}

AUGMENTED  = 999
MAJOR      = 888
MINOR      = 777
DIMINISHED = 666

majorChords = [None, MAJOR, MINOR, MINOR, MAJOR, MAJOR, MINOR, DIMINISHED]
minorChords = [None, MINOR, DIMINISHED, AUGMENTED, MINOR, MAJOR, MAJOR, DIMINISHED]

chords = {'major' : majorChords, 'minor' : minorChords}
