
import numpy as np
import scipy.signal
import sys


def function1(string):

    import random
    length = len(string)
    inx = random.randint(0, length-1)
    number = inx

    inx_char = string[inx]

    if inx_char.isalpha():
        if inx_char.islower():
            new_char = chr((ord(inx_char) - ord('a') + number) % 26 + ord('a'))
        else:
            new_char = chr((ord(inx_char) - ord('A') + number) % 26 + ord('A'))
        result = string[:inx] + new_char + string[inx + 1:]
    else:
        result = string
    return result            


def function2(string):

    if len(string)<2:
        return string    
    return string[-1]+string[1:-1]+string[0]

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
