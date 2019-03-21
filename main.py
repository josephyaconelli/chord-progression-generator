import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.Key import Key


myKey = Key('a',True)

print(myKey)


for i in range(1, 8):
    print(myKey.getChord(i, False, 3).chordName(myKey))
    print('\n')
