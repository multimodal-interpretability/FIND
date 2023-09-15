
import numpy as np
import scipy.signal
import sys


def function(string):

    mapping_dict = {'a': 't', 'b': 'd', 'c': 'o', 'd': 'e', 'e': 'w', 'f': 'n', 'g': 'f', 'h': 'j', 'i': 'g', 'j': 'x', 'k': 'h', 'l': 'r', 'm': 'v', 'n': 'q', 'o': 'b', 'p': 'm', 'q': 's', 'r': 'k', 's': 'i', 't': 'a', 'u': 'c', 'v': 'y', 'w': 'u', 'x': 'l', 'y': 'z', 'z': 'p'}
    mapped_string = ""
    for char in string:
        mapped_char = mapping_dict.get(char.lower(), char)
        mapped_string += mapped_char
    return mapped_string

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
