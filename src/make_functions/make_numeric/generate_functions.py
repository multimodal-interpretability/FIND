import os
import math_functions as mf
import train_functions as tf
from write_source_code import write_function
import numpy as np
import json
from tqdm import tqdm
import shutil
from utils import print_functions, import_function, create_string, get_type, get_domain




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--num_functions', type=int, help='Number of functions to generate', default=5)
    parser.add_argument('--debug', action='store_true', help='Debug mode, prints the plots of the functions to a diretory', default=False)
    parser.add_argument('--dir', default='numeric_functions', help='Name of the output directory', type=str)
    parser.add_argument('--verbose', action='store_true', help='Print output and progress', default=False)
    parser.add_argument('--mlp', type=float, help='Percentage of functions to approximate with an MLP', default=0.15)

    args = parser.parse_args()
    debug = args.debug
    # Save all meta data in a json file
    data = []

    for i in tqdm(range(args.num_functions)):
        dirname = f'{args.dir}/f{i:05d}'
        os.makedirs(dirname, exist_ok=True)
        os.makedirs(os.path.join(f'{args.dir}', 'meta'), exist_ok=True)

        f, params, func_name = mf.sample()
        name = create_string(func_name, params)
        domain = get_domain(func_name)

        # get corrupted function
        corrupted, cparams, cname = mf.sample_corruption(f, domain)


        # train MLP approx
        x = np.linspace(domain[0], domain[1], 10000).reshape(-1, 1)
        x_test = np.linspace(domain[0], domain[1], 10000).reshape(-1, 1)
        if i <= int(args.mlp * args.num_functions) and args.mlp > 0:
            loss = tf.train_function(x, f, func_name, x_test, dirname, verbose=args.verbose)
        else:
            loss = 'not trained'

        # write source code
        noise_type, noise_params = write_function(params, func_name, dirname, corrupted, cparams, cname)
        f_module = dirname.replace('/', '.')+'.function_code'
        function = import_function(f_module, 'function')

        # copy load_mlp.py to function subdirectory
        shutil.copy('load_mlp.py', f'{dirname}/load_mlp.py')
        # save meta data
        func_dict = {'type': get_type(func_name), 'params': params, 'name': name,
                     'dir': dirname, 'approx_mse_error': loss, 'corruption_type': cname,
                        'corruption_params': {'std':cparams[0], 'boundary':cparams[1:]}, 'domain': domain,
                     'noise_type': noise_type, 'noise_params': noise_params, 'mse_loss': loss}

        if debug:
            func_dict = print_functions(dirname, func_name, f, function, corrupted, func_dict)

        data.append(func_dict)

    # Write the data to a JSON file
    with open(f"{args.dir}/meta/data.json", "w") as file:
        json.dump(data, file)
    if args.verbose:
        import pprint
        pprint.pprint(data)


