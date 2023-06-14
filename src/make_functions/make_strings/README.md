# FIND interpretation benchmark
# Strings Function Generator API

Welcome to the Strings Function Generator API documentation. Our API allows developers to create custom functions that operate on strings for various applications such as data analysis, machine learning, algorithmic operations and more.

## Generating a function library
```python generate_string_functions.py --num_string_functions 100```
generates 100 randomly sampled strings functions and saves them into the `string_functions` sub-directory. The `--debug` flag will plot each function to a file.
Each function will have a subdirectory in the `dir` folder:
```
string_functions/
string_functions/f00000/function_code.py
string_functions/f00001/function_code.py
...
```
