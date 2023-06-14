# FIND interpretation benchmark
# Numeric Function Generator API

Welcome to the Numeric Function Generator API documentation. Our API allows developers to create custom mathematical functions programmatically for various applications such as data analysis, machine learning, algorithmic operations and more.

## Generating a function library
```python generate_functions.py --num_functions 100 --debug```
generates 100 randomly sampled math functions and saves them into a `numeric_functions` sub-directory. The `--debug` flag will plot each function to a file.
Each function will have a subdirectory folder:
```
numeric_functions/
numeric_functions/f00000/
numeric_functions/f00000/function_code.py
numeric_functions/f00000/mlp_approx_model.pt
numeric_functions/f00000/noised_function_code.py
numeric_functions/f00000/mlp_approx_plot.png	
numeric_functions/f00000/corrupted_function_code.py	
numeric_functions/f00000/plots
```
