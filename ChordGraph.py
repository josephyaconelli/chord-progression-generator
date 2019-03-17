import random

from ChordNode import ChordNode



class ChordGraph:

    def __init__(self):
        self.root = None
        self.nodes = []

    def add_node(self, chord, nextChords):
        
        getChordDuple = self.get_chord_from_str(chord)
        
        chordNode  = getChordDuple[0]
        isNewChord = not getChordDuple[1]

        nextChords_checked = []
        for chord in nextChords:

            check = self.get_chord_from_str(chord)
            if not check[1]:
                self.nodes.append(check[0])

            nextChords_checked.append(check[0])
            
        chordNode.add_next(nextChords_checked)

        if isNewChord:
            self.nodes.append(chordNode)


        if self.root is None:
            self.root = chordNode

    def set_root(self, root):
        self.root = root

    def get_chord_from_str(self, chordStr):
        if chordStr in self.nodes:
            idx = self.nodes.index(chordStr)
            return (self.nodes[idx], True)
        
        node = ChordNode(chordStr)
        return (node, False)


    def rand_next(self, curChord):
        nextOptions = curChord.nextChords
        return random.choice(nextOptions)



