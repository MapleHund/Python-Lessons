import random

class dice:
    # simulation of rolling dice

    # initialize and define attributes
    def __init__(self, rolls=1, sides=6):
        # if values are passed, assign them to self
        if rolls != 1: self.rolls = rolls
        else: self.rolls = rolls
        if sides != 6: self.sides = sides
        else: self.sides = sides


    def roll_die(self):

        results = []
        for i in range(0,self.rolls):
            results.append(random.randint(1,self.sides))
        
        return results
