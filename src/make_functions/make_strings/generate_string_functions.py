import os
import pdb

import string_functions as sf
from write_source_code import write_function
import numpy as np
import importlib
import json
import matplotlib.pyplot as plt
from tqdm import tqdm




def create_string(func_name, params):
    if type(params) != list:
        params = [params]
    param_str = ', '.join(str(p) for p in params) if params else ''
    return f"{func_name}({param_str})"

def get_type(str):
    if ';' not in str:
        return "simple"
    else:
        if 'compose' in str:
            return "compose"
        else:
            return str.split(';')[0]


def import_function(module_name, func_name):
    module = importlib.import_module(module_name)
    function = getattr(module, func_name)
    return function

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--num_string_functions', type=int, help='Number of functions to generate', default=1000)
    parser.add_argument('--dir', type=str, default='string_functions')
    parser.add_argument('--ratio', type=float, default=0.3)
    args = parser.parse_args()
    
    # args.dir = '%s/composed_fun_%.2f' %(args.dir, args.ratio)

    # Save all meta data in a json file
    data = []
    for i in tqdm(range(args.num_string_functions)):
        dirname = f'{args.dir}/f{i:05d}'
        os.makedirs(dirname, exist_ok=True)

        f, params, func_name = sf.sample(args)
        name = create_string(func_name, params)

        
        # write source code
        write_function(params, func_name, dirname)

        # save meta data
        func_dict = {'type': get_type(func_name), 'params': params, 'name': name, 'dir': dirname}
        

        print('----------------------------------------------------------')
        print(func_dict)
        
        data.append(func_dict)
        
    # Write the data to a JSON file
    with open(f"{args.dir}/data.json", "w") as file:
        json.dump(data, file)

