# math_functions.py
import numpy as np
import scipy.signal
import random
from scipy.special import erf, factorial, gamma


compound_func_names = ["sum_two", "sum_three", "multiply_two", "convolution", "compose"]


# Simple functions

# Linear function
def linear(m, b, x):
    return m * x + b

# Polynomial
def polynomial(coeffs, x):
    degree = len(coeffs) - 1
    result = 0
    for i in range(degree+1):
        result += coeffs[i] * x**(degree-i)
    return result

#Rational 
def rational(num_coeff, denom_coeff, x):
    num = sum([a*x**i for i, a in enumerate(num_coeff)])
    denom = sum([b*x**i for i, b in enumerate(denom_coeff)])
    return (num) / (denom)

# Absolute
def absolute(a, b, x):
    return a * np.abs(x) + b

# Root function
def root(a, b, n, x):
    return a*(x ** (1.0 / n)) + b

# Reciprocal function 
def reciprocal(a, x):
    return 1/(a*x)

# Erf 
def error_func(x):
    return erf(x)

# Logarithm
def logarithm(a, b, base, x):
    return a* (np.log(x) / np.log(base)) + b


# Step function
def step(a, b, s, x):
    return a * np.heaviside(x, s) + b

# Rectangle function 
def rectangle(w, x):
    return np.where(np.abs(x) <= w/2, 1 ,0)

# ReLU
def relu(a, b, x, l):
    return a * np.where(x > 0, x, x * l) + b

# Sigmoid
def sigmoid(a, b,x, t):
    return a*(1 / (1 + np.exp(-x/t))) + b

# Tanh
def tanh(a, b, c, d, x):
    return a * np.tanh((2 * np.pi / b)*(x-c)) + d

# Sin
def sin(a, b, c, d, x):
    return a * np.sin((2 * np.pi / b)*(x-c)) + d

#Cosine
def cos(a, b, c, d, x):
    return a * np.cos((2 * np.pi / b)*(x-c)) + d

#Tangent
def tan(a, b, c, d, x):
    return a * np.tan((2 * np.pi / b)*(x-c)) + d

#Ceiling
def ceil(x):
    return np.ceil(x)

#Floor
def floor(x):
    return np.floor(x)

#Gaussian
def gaussian(mean, std, x):
    return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)

#Square wave
def square_wave(period, shift, x):
    value = np.sin((x-shift) * (2 * np.pi / period))
    return np.where(value>0, 1, -1)

# Unique functions
# Signum
def signum(x):
    return np.sign(x)

# Sum of two functions
def sum_two(func1, func2, x):
    return func1(x) + func2(x)

# Sum of three functions
def sum_three(func1, func2, func3, x):
    return func1(x) + func2(x) + func3(x)

# Multiply two functions
def multiply_two(func1, func2, x):
    return func1(x) * func2(x)

# Convolution
def convolution(func1, func2, x):
    y1 = func1(x)
    y2 = func2(x)
    return scipy.signal.convolve(y1, y2, mode='same')

# Composition of functions
def compose(func1, func2, x):
    return func1(func2(x))

# Interventions
# Interval function
def interval_smaller_function(func1, x, boundary, mean):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x > boundary, func1(x), np.random.normal(loc=mean, scale=0.1, size=x.shape))

def interval_larger_function(func1, x, boundary, mean):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where(x < boundary, func1(x), np.random.normal(loc=mean, scale=0.1, size=x.shape))

# Interval Exclude function
def interval_exclude_function(func1, x, a, b, mean):
    if type(x) == int or type(x) == float:
        x = np.array(x)
    return np.where((x > a) & (x < b),  np.random.normal(loc=mean, scale=0.1, size=x.shape), func1(x))

def constant_fct(a, x):
    return np.ones_like(x)*a

# Sampling function
def sample_single_f(corruption=False, base_func_names=None):
    func_dict = {"linear": linear, "polynomial": polynomial, "absolute": absolute, "root": root, "logarithm": logarithm,
                 "step": step, "signum": signum, "relu": relu,  "tanh": tanh, 'constant': constant_fct,
                 'sin': sin, 'cos': cos, 'tan': tan,  'ceil': ceil, 'floor': floor, 'reciprocal': reciprocal,
                 'gaussian': gaussian, 'rational': rational, 'error_func': error_func,
                 'rectangle': rectangle, 'square_wave':square_wave}
    if base_func_names is None:
        base_func_names = ["linear", "polynomial", "absolute", "root", "logarithm", "step", "signum", "relu",
                           "tanh", 'constant', 'sin', 'cos', 'tan', 'reciprocal', 'gaussian', 'rational',
                          'rectangle', 'square_wave']
    if corruption:
        base_func_names = ["linear",  'constant', 'polynomial']
    func_name = np.random.choice(base_func_names)
    func = func_dict[func_name]
    scale, bias = [round(i, 1) for i in [random.uniform(-30, 30) for _ in range(2)]]
    amplitude = round(np.random.choice(np.linspace(-10, 10, 100)), 1)
    phase_shift = round(np.random.choice(np.linspace(0.1, 2 * np.pi, 100)), 1)
    period = round(np.random.choice(np.linspace(0.1, 2 * np.pi, 100)), 1)
    if func_name == "linear":
        m = round(random.uniform(-10, 10),1)
        b = round(random.uniform(-10, 10),1)
        return lambda x: func(m, b, x), (m, b), func_name
    elif func_name == "polynomial":
        degree = random.randint(2, 5)  # Degree of the polynomial
        coeffs = [round(i, 1) for i in [random.uniform(-5, 5) for _ in range(degree + 1)]]
        return (lambda x: func(coeffs, x)), coeffs, func_name
    elif func_name == "rational":
        num_order = random.randint(0, 4)  # numerator order
        denom_order = random.randint(num_order + 1, 5)  # denominator order
        num_coeff = [round(i, 1) for i in [random.uniform(-10, 10) for _ in range(num_order+1)]]  # numerator coefficients
        denom_coeff = [round(i, 1) for i in [random.uniform(-10, 10) for _ in range(denom_order+1)]]  # denominator coefficients
        return lambda x: rational(num_coeff, denom_coeff, x), (num_coeff, denom_coeff), func_name
    elif func_name == "reciprocal":
        a = round(random.uniform(-10, 10), 1)
        return lambda x: reciprocal(a, x), (a,), func_name
    elif func_name == "root":
        n = random.randint(1, 2)
        return lambda x: func(scale, bias, n, x), (scale, bias, n), func_name
    elif func_name == "gaussian":
        mean = round(random.uniform(-50, 50),1) 
        std = round(random.uniform(1, 10),1)  
        return lambda x: gaussian(mean, std, x), (mean, std), func_name
    elif func_name == "absolute":
        return lambda x: func(scale, bias, x), (scale, bias), func_name
    elif func_name == "topower":
        a = round(np.random.choice(np.linspace(-2, 2, 100)),1)
        return lambda x: func(scale, bias, a, x), (scale, bias, a), func_name
    elif func_name == "logarithm":
        base = round(random.uniform(1, 10),1)
        return lambda x: func(scale, bias, base, x), (scale, bias, base), func_name
    elif func_name == "step":
        a = round(random.uniform(-100, 100),1)
        return lambda x: func(scale, bias, a, x), (scale, bias, a), func_name   
    elif func_name == "square_wave":
        period = round(random.uniform(1, 10),1)  # period of the wave, adjust these bounds as you like
        shift = round(random.uniform(-5, 5),1)  # phase shift, adjust these bounds as you like
        return lambda x: square_wave(period, shift, x), (period, shift), func_name
    elif func_name == "rectangle":
        w = round(random.uniform(1, 10),1)  # width of the rectangle, adjust these bounds as you like
        return lambda x: rectangle(w, x), (w,), func_name
    elif func_name == "signum":
        return func, None, func_name
    elif func_name == "relu":
        leak = round(random.uniform(0, 1),1)
        return lambda x: func(scale, bias, x, leak), (scale, bias, leak), func_name
    elif func_name == "sigmoid":
        temperature = 1
        return lambda x: func(scale, bias, x, temperature), (scale, bias, temperature), func_name
    elif func_name == "tanh":
        return lambda x: func(amplitude, phase_shift, period, bias, x), (amplitude, phase_shift, period, bias), func_name
    elif func_name == "sin":
        return lambda x: func(amplitude, phase_shift, period, bias, x), (amplitude, phase_shift, period, bias), func_name
    elif func_name == "cos":
        return lambda x: func(amplitude, phase_shift, period, bias, x), (amplitude, phase_shift, period, bias), func_name
    elif func_name == "tan":
        return lambda x: func(amplitude, phase_shift, period, bias, x), (amplitude, phase_shift, period, bias), func_name
    elif func_name == "constant":
        a = np.random.randint(-100, 100)
        return lambda x: func(a, x), (a), func_name
    elif func_name == "ceil":
        return func, None, func_name
    elif func_name == "floor":
        return func, None, func_name
    elif func_name == "pow":
        p = np.random.randint(2, 10)
        return lambda x: func(x, scale, bias, p), (scale, bias, p), func_name
    elif func_name == "error_func":
        return func, None, func_name
    else:
        print(func_name)
        raise NotImplementedError

def generate_noise(y, noise_type, noise_scale):
    if noise_type is None:
        return 0
    elif noise_type == 'gaussian':
        return np.random.normal(scale=noise_scale, size=len(y))
    elif noise_type == 'uniform':
        return np.random.uniform(low=-noise_scale, high=noise_scale, size=len(y))
    elif noise_type == 'poisson':
        return np.random.poisson(lam=noise_scale, size=len(y))

def sample_corruption(f_to_corrupt, domain):
    """
    Samples a corruption function and returns the corrupted function
    Only corrupts a function by changing an interval of the function,
    on which the corruption function is applied. The interval length is between 5 and 25.
    :param f_to_corrupt:
    :return: corrupted function, parameters of corruption function, name of corruption function
    """
    cparams = []
    mean_val = np.mean(f_to_corrupt(np.linspace(domain[0], domain[1], 100)))
    std = mean_val
    cparams.append(std)
    a = round(random.uniform(max(domain[0], -100), 100),1)
    cparams.append(a)


    if np.random.choice([True, False]):
        if np.random.choice([True, False]):
            corrupted = lambda x: interval_smaller_function(f_to_corrupt, x, a, std)
            cname = f'interval_smaller'
        else:
            corrupted = lambda x: interval_larger_function(f_to_corrupt, x, a, std)
            cname = f'interval_larger'
    else:
        b = random.uniform(a + 5, a + 25)
        cparams.append(b)
        corrupted = lambda x: interval_exclude_function(f_to_corrupt, x, a, b, std)
        cname = f'interval_inside'
    return corrupted, cparams, cname




def sample_f(compound_func_names=None, single_func_names1=None, single_func_names2=None):
    func_dict = {"sum_two": sum_two, "sum_three": sum_three, "multiply_two": multiply_two, "convolution": convolution,
                 "compose": compose}
    if compound_func_names is None:
        compound_functions = [sum_two, sum_three, multiply_two, convolution, compose]

    func_name = np.random.choice(compound_func_names)
    func = func_dict[func_name]
    func1, params1, name1 = sample_single_f(base_func_names=single_func_names1)
    func2, params2, name2 = sample_single_f(base_func_names=single_func_names2)

    if func_name == "sum_three":
        func3, params3, name3 = sample_single_f()
        func_name = f'{name1};{name2};{name3};{func_name}'
        return lambda x: func(func1, func2, func3, x), [params1, params2, params3], func_name
    else:
        if func_name == "compose" and name2 == "factorial":
            func_name = "sum_two"
            func = sum_two
        func_name = f'{name1};{name2};{func_name}'
        return lambda x: func(func1, func2, x), [params1, params2], func_name



def sample(p_simple=0.85):
    basic = ["linear", "polynomial", "absolute", "root", "logarithm", "step", "relu",
     "tanh", 'constant',  'sin', 'cos', 'reciprocal', 'gaussian', 'rational',
             'rectangle', 'square_wave']
    if random.random() < p_simple:
        f, params, f_name = sample_single_f(base_func_names=basic)
        return f, params, f_name
    else:
        compose_only = ["linear", "polynomial", "step", "relu",  'constant',
                        "ceil", "floor",'rectangle', 'square_wave']
        f, params, f_name = sample_f(compound_func_names=["multiply_two", "sum_two"],
                                     single_func_names1=compose_only,
                                     single_func_names2=compose_only)
        return f, params, f_name


if __name__ == '__main__':
    for i in range(1000):
        f, paramm, f_name = sample()
        print(f_name)
