
import numpy as np
import scipy.signal
import sys


def function(string):

    new_string = 'lvmBi'

    return string + new_string

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        string = str(arg)
        outputs += f'({arg}, {str(function(string))}) '

    print(f'Function input - output pairs: {outputs}')
