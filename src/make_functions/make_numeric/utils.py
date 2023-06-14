import time
import matplotlib.pyplot as plt
import importlib
import os
import numpy as np

def get_test_domain(str):
    if 'log' in str:
        return [1, 100]
    elif 'root' in str:
        return [0, 100]
    else:
        return [-100, 100]

def get_type(str):
    if ';' not in str:
        return "simple"
    else:
        if 'compose' in str:
            return "compose"
        else:
            return str.split(';')[0]

def get_domain(str):
    if 'log' in str:
        return [1, 1000]
    elif 'root' in str:
        return [0, 1000]
    else:
        return [-1000, 1000]


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # get the current time
        result = func(*args, **kwargs)  # call the original function
        end_time = time.time()  # get the current time again
        print(f"Time elapsed for {func.__name__}: {end_time - start_time} seconds.")
        return result  # return the result of the original function
    return wrapper

def import_function(module_name, func_name):
    module = importlib.import_module(module_name)
    function = getattr(module, func_name)
    return function

def create_string(func_name, params):
    if type(params) != list:
        params = [params]
    param_str = ', '.join(str(p) for p in params) if params else ''
    return f"{func_name}({param_str})"

def print_functions(dirname, func_name, f, function, corrupted, func_dict=None):
    # check if the code is correct
    corrupted_function = import_function(dirname.replace('/', '.') + '.corrupted_function_code',
                                         'function')
    noised_function = import_function(dirname.replace('/', '.') + '.noised_function_code', 'function')
    os.makedirs(f'{dirname}/plots/', exist_ok=True)
    domain = get_test_domain(func_name)
    x = np.linspace(domain[0], domain[1], 1000).reshape(-1, 1)
    y = f(x)
    plt.plot(x, y)
    plt.savefig(f'{dirname}/plots/function.png')
    plt.close()
    y1 = function(x)
    plt.plot(x, y1)
    plt.savefig(f'{dirname}/plots/function_from_code.png')
    plt.close()
    if func_dict is not None:
        func_dict['error_code_generated'] = np.mean(y1 - y)
    yc = corrupted(x)
    plt.plot(x, yc)
    plt.savefig(f'{dirname}/plots/corrupted.png')
    plt.close()
    yc1 = corrupted_function(x)
    plt.plot(x, yc1)
    plt.savefig(f'{dirname}/plots/corrupted_from_code.png')
    plt.close()

    yc = noised_function(x)
    plt.plot(x, yc)
    plt.plot(x, yc)
    plt.savefig(f'{dirname}/plots/noised.png')
    plt.close()
    if func_dict is not None:
        func_dict['error_corrupted_code_generated'] = np.mean(y1 - y)
        return func_dict