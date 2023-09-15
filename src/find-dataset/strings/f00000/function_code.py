
import numpy as np
import scipy.signal
import sys


def function1(string):

    inx = 5
    if len(string)<inx+1: 
        return string
    char_inx = string[inx].lower()
    order = ord(char_inx) - ord('a')

    advanced_string = ""
    for char in string:
        if char.isalpha():
            new_char = chr((ord(char.lower()) - ord('a') + order) % 26 + ord('a'))
        else:
            new_char = char
        advanced_string += new_char
    return advanced_string


def function2(string):

    lengths ={
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '21': 'twenty-one',
        '22': 'twenty-two',
        '23': 'twenty-three',
        '24': 'twenty-four',
        '25': 'twenty-five',
        '26': 'twenty-six',
        '27': 'twenty-seven',
        '28': 'twenty-eight',
        '29': 'twenty-nine',
        '30': 'thirty'
    }
    length = len(string)
    if str(length) in lengths:
        return lengths[str(length)]
    else:
        return 'unknown'

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
