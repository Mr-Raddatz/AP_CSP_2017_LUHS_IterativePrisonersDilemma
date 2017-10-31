import numpy as np
import random

def diceroll(n):
    ''' returns a random roll of n six sided dice
    n is a positive int
    
    returns an int
    '''
    total = 0 # Initialize the accumulator for the total roll
    for die in range(n):
        total += random.randint(1, 6)
    return total

 
def test_diceroll(roller):
    ''' Provides a unit test of a function roller(n) that is supposed
    to roll n six-sided dice
    '''
    def tester(n):
        ''' tests roller with n dice
        '''
        works = True # one way flag; False indicates a problem
        total = 0                
        for i in range(1000):
            roll = roller(n)
            if (roll<n) or (roll>6*n):
                print "Roll with "+n+" dice was "+roll
                works = False
            total += roll
        if not (3000*n<total<4000*n):
            print "1000 rolls with "+n+"totaled "+total
            works = False
        return works
    
    ####
    # Run two tests
    ###
    correct = True
    correct = correct and tester(1)
    correct = correct and tester(100)
    return correct
    
if __name__=="__main__":
    test_diceroll(diceroll)