from typing import List

def findDuplicate1(input: List[int]) -> int:
    '''
    Finds the duplicate integer of a list with domain [1, N]
        using list slicing.

    Inputs:
        input [list]: list with domain [1, N].
    
    Return [int]: the duplicate integer.
    '''
    for idx, num in enumerate(input):
        if num in input[idx + 1:]:
            return num

def findDuplicate2(input: List[int]) -> int:
    '''
    Finds the duplicate integer of a list with domain [1, N]
        by sorting the original list.

    Inputs:
        input [list]: list with domain [1, N].
    
    Return [int]: the duplicate integer.
    '''
    input.sort()

    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            return input[i]
