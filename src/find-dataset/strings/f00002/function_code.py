
import numpy as np
import scipy.signal
import sys


def function1(string):

    rand = 6
    if string == "" or not string[-1].isalpha():  # Empty string or last character not a letter
        return string
    elif string[-1] == 'a':  # wrap around from 'a' to 'z'
        return string[:-1] + 'z'
    elif string[-1] == 'A':  # wrap around from 'A' to 'Z'
        return string[:-1] + 'Z'
    else:  # shift back one letter in the alphabet
        return string[:-1] + chr(ord(string[-1]) - rand)


def function2(string):

    digit_names = {
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
    }
    first_character = string[0].lower()
    if not(first_character.isalpha()): return 'zero'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    order = alphabet.index(first_character) + 1
    return digit_names[str(order)]

def function(string):
    return function1(function2(string))

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
