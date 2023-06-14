# main script
import pdb
import random
import math_functions as mf
import textwrap
import re


def write_simple_function(params, func_name, f_name='function'):
    code = f"""    
    def {f_name}(x):
        """

    # For each type of function, we need to generate code accordingly
    if func_name == "linear":
        code += f"""
        return {params[0]}*x + {params[1]}
        """
    elif func_name == "polynomial":
        degree = len(params) - 1
        terms = ["{}*x**{}".format(params[i], degree-i) for i in range(degree+1)]
        string = " + ".join(terms)
        code += f"""
        return {string}
        """
    elif func_name == "rational":
        code += f"""
        return ({' + '.join([f'{params[0][i]}*x**{i}' for i in range(len(params[0]))])}) / ({' + '.join([f'{params[1][i]}*x**{i}' for i in range(len(params[1]))])})
        """
    elif func_name == "root":
        code += f"""
        return {params[0]}*(x**(1.0 / {params[2]})) + {params[1]}
        """
    elif func_name == "reciprocal":
        code += f"""
        return 1 / ({params[0]} * x)
        """
    elif func_name == "error_func":
        code += f"""
        from math import erf
        return erf(x)
        """
    elif func_name == "square_wave":
        code += f"""
        x = np.sin((x - {params[1]}) * (2 * np.pi / {params[0]}))
        return np.where(x > 0, 1, -1)
        """
    elif func_name == "absolute":
        code += f"""
        return {params[0]}*np.abs(x)"""
    elif func_name == "topower":
        code += f"""
        return {params[0]}*({params[2]}**x) + {params[1]}
        """
    elif func_name == "logarithm":
        code += f"""
        return {params[0]}*(np.log(x) / np.log({params[2]})) + {params[1]}
        """
    elif func_name == "step":
        code += f"""
        return {params[0]}*np.heaviside(x, {params[2]})+ {params[1]}
        """
    elif func_name == "rectangle":
        code += f"""
        return np.where(abs(x) <= {params[0]}/2,1,0)
        """
    elif func_name == "signum":
        code += f"""
        return np.sign(x)
        """
    elif func_name == "relu":
        code += f"""
        return {params[0]} * np.where(x > 0, x, x * {params[2]}) + {params[1]}
        """
    elif func_name == "sigmoid":
        code += f"""
        return {params[0]} *(1 / (1 + np.exp(-x/{params[2]}))) + {params[1]}
        """
    elif func_name == "tanh":
        code += f"""
        return {params[0]} * np.tanh((2 * np.pi / {params[1]})*(x-{params[2]})) + {params[3]}
        """
    elif func_name == "gaussian":
        code += f"""

        return (1 / ({params[1]} * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - {params[0]}) / {params[1]}) ** 2)
        """
    elif func_name == "student_t":
        code += f"""
        from scipy.special import gamma
        return gamma(({params[0]}+1)/2) / (np.sqrt({params[0]}*np.pi) * gamma({params[0]}/2)) * (1 + x**2/{params[0]}) ** (-({params[0]}+1)/2)
        """
    elif func_name == "poisson":
        code += f"""
        from scipy.special import factorial
        return ({params[0]}**x * np.exp(-{params[0]})) / factorial(x)
        """
    elif func_name == "sin":
        code += f"""
        return {params[0]} * np.sin((2 * np.pi / {params[1]})*(x-{params[2]})) + {params[3]}
        """
    elif func_name == "cos":
        code += f"""
        return {params[0]} * np.cos((2 * np.pi / {params[1]})*(x-{params[2]})) + {params[3]}
        """
    elif func_name == "tan":
        code += f"""
        return {params[0]} * np.tan((2 * np.pi / {params[1]})*(x-{params[2]})) + {params[3]}
        """
    elif func_name == "constant":
        code += f"""
                return {params}* np.ones_like(x)
                """
    elif func_name == "ceil":
        code += f"""
                return np.ceil(x)
                """
    elif func_name == "floor":
        code += f"""
                return np.floor(x)
                    """
    elif func_name == "pow":
        code += f"""
        x = np.where(x < 0, 0, x) if {params[2]} % 1 != 0 else x
        return {params[0]}*np.power(x, {params[2]}) + {params[1]}
        """

    else:
        raise ValueError(f"Unknown function name: {func_name}")


    return code


def extract_function_call(string):
    # Use a regular expression to find the text between "return" and "\n"
    match = re.search(r'return (.*)\n', string)
    match1 = re.search(r'return (.*)', string)
    if match:
        result = match.group(1)
    elif match1:
        result = match1.group(1)
    return result

def wrtie_noised_function(code, dirname):
    start_code = """
    import numpy as np
    import scipy.signal
    import sys
    from scipy.special import gamma, factorial, erf

    """
    clean_function_code = extract_function_call(code)
    if random.random() < 0.33:
        noise_type = 'normal'
        add_code = f"""
        def function(x):
                return {clean_function_code} + np.random.normal(scale=1)\n"""
    elif random.random() < 0.66:
        noise_type = 'uniform'
        add_code = f"""
        def function(x):
                return {clean_function_code} + np.random.uniform(low=-1, high=1)\n"""
    else:
        noise_type = 'poisson'
        add_code = f"""
        def function(x):
                return {clean_function_code} + np.random.poisson(lam=1)\n"""
    code = textwrap.dedent(start_code)
    add_code = textwrap.dedent(add_code)
    code += add_code
    run_code = """
    if __name__ == '__main__':
        outputs = ''
        for arg in sys.argv[1:]:
            x = float(arg)
            try:
                out = function(x)
            except:
                out = 'None'
            outputs += f'({arg}, {out}) '
        print(f'Function input - output pairs: {outputs}')

    """
    code += textwrap.dedent(run_code)
    with open(f"{dirname}/noised_function_code.py", "w") as file:
        if code[0] == '\n':
            code = code[1:]
        file.write(code)
    return noise_type, 1
        

def write_corrupted_function(code, corrupted, cparams, cname, dirname):
    start_code = """
    import numpy as np
    import scipy.signal
    import sys
    from scipy.special import gamma, factorial, erf

    """
    clean_function_code = extract_function_call(code)

    std = cparams[0]
    if cname == 'interval_smaller':
        corrupted_code = f'return np.where(x > {cparams[1]}, {clean_function_code}, np.random.normal(loc={std},scale=0.1, size=x.shape))\n'
    elif cname == 'interval_larger':
        corrupted_code = f'return np.where(x < {cparams[1]}, {clean_function_code}, np.random.normal(loc={std}, scale=0.1,size=x.shape))\n'
    elif cname == 'interval_inside':
        corrupted_code = f'return np.where((x > {cparams[1]}) & (x < {cparams[2]}), np.random.normal(loc={std},scale=0.1, size=x.shape), {clean_function_code})\n'
    else:
        raise ValueError(f"Unknown corrupted function name: {cname}")
    # Add the interval function to the code
    new_code1 = f"""
    def function(x):
        if type(x) == int or type(x) == float:
            x = np.array(x)
        {corrupted_code}
    """

    code = textwrap.dedent(start_code)
    new_code1 = textwrap.dedent(new_code1)

    run_code = """
    if __name__ == '__main__':
        outputs = ''
        for arg in sys.argv[1:]:
            x = float(arg)
            try:
                out = function(x)
            except:
                out = 'None'
            outputs += f'({arg}, {out}) '
        print(f'Function input - output pairs: {outputs}')


    """
    code += new_code1
    code += textwrap.dedent(run_code)
    with open(f"{dirname}/corrupted_function_code.py", "w") as file:
        if code[0] == '\n':
            code = code[1:]
        file.write(code)



def write_function(params, func_name, dirname, corrupted=None, cparams=None, cname=None):
    start_code = """
    import numpy as np
    import scipy.signal
    import sys
    from scipy.special import gamma, factorial, erf
    
    """
    if ';' not in func_name:
        code = write_simple_function(params, func_name)
    else:
        if 'sum_three' in func_name:
            params1, params2, params3 = params
            func_name1, func_name2, func_name3 = func_name.split(';')[:3]
            code1 = write_simple_function(params1, func_name1, f_name='function1')
            code2 = write_simple_function(params2, func_name2, f_name='function2')
            code3 = write_simple_function(params3, func_name3, f_name='function3')
            clean_function_code1 = extract_function_call(code1)
            clean_function_code2 = extract_function_call(code2)
            clean_function_code3 = extract_function_call(code3)
            code = f"""
            def function(x):
                return {clean_function_code1} + {clean_function_code2} + {clean_function_code3}
            """
        else:
            params1, params2 = params
            func_name1, func_name2, func_name = func_name.split(';')
            code1 = write_simple_function(params1, func_name1, f_name='function1')
            code2 = write_simple_function(params2, func_name2, f_name='function2')
            clean_function_code1 = extract_function_call(code1)
            clean_function_code2 = extract_function_call(code2)
            if func_name == 'sum_two':
                code = f"""
                def function(x):
                    return {clean_function_code1} + {clean_function_code2} 
                """
            elif func_name == 'multiply_two':
                code = f"""
                def function(x):
                    return ({clean_function_code1}) * ({clean_function_code2})
                """
            elif func_name == 'convolution':
                raise NameError('Not implemented yet')
            elif func_name == 'compose':
                clean_function_code1 = clean_function_code1.replace('exp', 'PLACEHOLDER')
                clean_function_code1 = clean_function_code1.replace('x', clean_function_code2)
                clean_function_code1 = clean_function_code1.replace('PLACEHOLDER', 'exp')
                code = f"""
                def function(x):
                    return {clean_function_code1}
                """
            else:
                raise ValueError('Unknown function name')

    start_code = textwrap.dedent(start_code)
    code = textwrap.dedent(code)
    run_code = """
    if __name__ == '__main__':
        outputs = ''
        for arg in sys.argv[1:]:
            x = float(arg)
            try:
                out = function(x)
            except:
                out = 'None'
            outputs += f'({arg}, {out}) '
        print(f'Function input - output pairs: {outputs}')


    """
    start_code += code

    noise_type, noise_params = wrtie_noised_function(code, dirname)

    if corrupted and cparams and cname:
        write_corrupted_function(code, corrupted, cparams, cname, dirname)

    start_code += textwrap.dedent(run_code)
    with open(f"{dirname}/function_code.py", "w") as file:
        if start_code[0] == '\n':
            start_code = start_code[1:]
        file.write(start_code)
    return noise_type, noise_params

        

