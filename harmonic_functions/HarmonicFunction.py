import abc


class HarmonicFunction(abc.ABC):

    @abc.abstractmethod
    def getFirst(self):
        pass

    @abc.abstractmethod
    def getNext(self, currentChord, probability = 1.0):
        pass

    @abc.abstractmethod
    def getLast(self, prev):
        pass

    @property
    def chord(self):
        pass
