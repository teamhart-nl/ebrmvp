import random

from Pattern import Pattern

class PatternStore:

    def __init__(self):
        # TODO: make this dict of Pattern objects
        self.patterns = {n : Pattern(value=n) for n in range(10)}

    def getRandomPattern(self):
        return random.choice(list(self.patterns.keys()))

    def getPatternRepresenation(self, pattern_id):
        return self.patterns[pattern_id]


    '''
    Send result back
    '''
    def addResult(self, correct : bool):
        raise NotImplementedError    