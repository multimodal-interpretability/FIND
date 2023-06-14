import pdb
import numpy as np
import scipy.signal
import random
import string as str
import json
import os

two_input_fun = ["string_concatenate", "count_substring", "find_string", "split_string", "remove_substring", "starts_with_substring", "ends_with_substring"]
three_input_fun = ["replace_substring"]


## single input
def get_string_length(string):
    return len(string)


def convert_to_lowercase(string):
    return string.lower()


def convert_to_uppercase(string):
    return string.upper()


def capitalize_string(string):
    return string.capitalize()


def title_case_string(string):
    return string.title()


def reverse_string(string):
    return string[::-1]


def extract_digits(string):
    return ''.join(filter(str.isdigit, string))


def remove_whitespace(string):
    return ''.join(string.split())


def get_first_character(string):
    return string[0]


def get_last_character(string):
    return string[-1]


def remove_duplicates(string):
    return ''.join(sorted(set(string), key=string.index))


def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(char in vowels for char in string)


def count_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(char in consonants for char in string)


def string_strip(string):
    return string.strip()


def string_lstrip(string):
    return string.lstrip()


def string_rstrip(string):
    return string.rstrip()


def is_palindrome(string):
    cleaned_string = string.lower().replace(" ", "")
    return cleaned_string == cleaned_string[::-1]


def is_numeric(string):
    return string.isnumeric()


def is_alpha(string):
    return string.isalpha()


def is_digit(string):
    return string.isdigit()

def is_lower(string):
    return string.islower()


def is_upper(string):
    return string.isupper()


def is_title(string):
    return string.istitle()


def add_number_to_string(string, number):
    result = ""
    for char in string:
        new_char = chr(ord(char) + number)
        result += new_char
    return result


def subtract_number_to_string(string, number):
    result = ""
    for char in string:
        new_char = chr(ord(char) - number)
        result += new_char
    return result


def insert_number(string, number):
    mid_index = len(string) // 2
    new_string = string[:mid_index] + str(number) + string[mid_index:]
    return new_string


def add_letter_if_needed(string, letter):
    if not string.endswith(letter):
        string += letter
    return string


def insert_letter(string, letter):
    mid_index = len(string) // 2
    new_string = string[:mid_index] + letter + string[mid_index:]
    return new_string


def split_string(string, substring=None):
    return string.split(substring)


def string_concatenate(string, new_string):
    return string + new_string


def count_substring(string, substring):
    return string.count(substring)


def find_string(string, substring):
    return string.find(substring)


def remove_substring(string, substring):
    return string.replace(substring, '')


def starts_with_substring(string, substring):
    return string.startswith(substring)


def ends_with_substring(string, substring):
    return string.endswith(substring)


def replace_substring(string, old, new):
    return string.replace(old, new)


def duplicate_last_letter(string):
    return string+string[-1]


def shift_last_letter(string):
    if string == "" or not string[-1].isalpha():   # Empty string or last character not a letter
        return string
    elif string[-1] == 'z':   # wrap around from 'z' to 'a'
        return string[:-1] + 'a'
    elif string[-1] == 'Z':   # wrap around from 'Z' to 'A'
        return string[:-1] + 'A'
    else:   # shift forward one letter in the alphabet
        return string[:-1] + chr(ord(string[-1]) + 1)

    
def shift_first_letter(string):
    if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
        return string
    elif string[0] == 'z':   # wrap around from 'z' to 'a'
        return 'a' + string[1:]
    elif string[0] == 'Z':   # wrap around from 'Z' to 'A'
        return 'A' + string[1:]
    else:   # shift forward one letter in the alphabet
        return chr(ord(string[0]) + 1) + string[1:]

    
def shift_last_letter_predecessor(string):
    if string == "" or not string[-1].isalpha():  # Empty string or last character not a letter
        return string
    elif string[-1] == 'a':  # wrap around from 'a' to 'z'
        return string[:-1] + 'z'
    elif string[-1] == 'A':  # wrap around from 'A' to 'Z'
        return string[:-1] + 'Z'
    else:  # shift back one letter in the alphabet
        return string[:-1] + chr(ord(string[-1]) - 1)

    
def shift_first_letter_predecessor(string):
    if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
        return string
    elif string[0] == 'a':  # wrap around from 'a' to 'z'
        return 'z' + string[1:]
    elif string[0] == 'A':  # wrap around from 'A' to 'Z'
        return 'Z' + string[1:]
    else:  # shift back one letter in the alphabet
        return chr(ord(string[0]) - 1) + string[1:]


def shift_last_letter_forward_two(string):
    if string == "" or not string[-1].isalpha():
        return string
    elif string[-1] == 'y':  # wrap around from 'y' to 'a'
        return string[:-1] + 'a'
    elif string[-1] == 'z':  # wrap around from 'z' to 'b'
        return string[:-1] + 'b'
    elif string[-1] == 'Y':  # wrap around from 'Y' to 'A'
        return string[:-1] + 'A'
    elif string[-1] == 'Z':  # wrap around from 'Z' to 'B'
        return string[:-1] + 'B'
    else:
        return string[:-1] + chr(ord(string[-1]) + 2)


def shift_first_letter_forward_two(string):
    if string == "" or not string[0].isalpha():
        return string
    elif string[0] == 'y':  # wrap around from 'y' to 'a'
        return 'a' + string[1:]
    elif string[0] == 'z':  # wrap around from 'z' to 'b'
        return 'b' + string[1:]
    elif string[0] == 'Y':  # wrap around from 'Y' to 'A'
        return 'A' + string[1:]
    elif string[0] == 'Z':  # wrap around from 'Z' to 'B'
        return 'B' + string[1:]
    else:
        return chr(ord(string[0]) + 2) + string[1:]

    
def shift_last_letter_backward_two(string):
    if string == "" or not string[-1].isalpha():
        return string
    elif string[-1] == 'a':  # wrap around from 'a' to 'y'
        return string[:-1] + 'y'
    elif string[-1] == 'b':  # wrap around from 'b' to 'z'
        return string[:-1] + 'z'
    elif string[-1] == 'A':  # wrap around from 'A' to 'Y'
        return string[:-1] + 'Y'
    elif string[-1] == 'B':  # wrap around from 'B' to 'Z'
        return string[:-1] + 'Z'
    else:
        return string[:-1] + chr(ord(string[-1]) - 2)


def shift_first_letter_backward_two(string):
    if string == "" or not string[0].isalpha():
        return string
    elif string[0] == 'a':  # wrap around from 'a' to 'y'
        return 'y' + string[1:]
    elif string[0] == 'b':  # wrap around from 'b' to 'z'
        return 'z' + string[1:]
    elif string[0] == 'A':  # wrap around from 'A' to 'Y'
        return 'Y' + string[1:]
    elif string[0] == 'B':  # wrap around from 'B' to 'Z'
        return 'Z' + string[1:]
    else:
        return chr(ord(string[0]) - 2) + string[1:]


# Composition of functions
def compose_1input_1input(func1, func2, string):
    return func1(func2(string))

def compose_1input_2input(func1, func2, string1, string2):
    return func1(func2(string1, string2))

def compose_1input_3input(func1, func2, string1, string2, string3):
    return func1(func2(string1, string2, string3))

def compose_2input_1input(func1, func2, string1, string2):
    return func1(func2(string1), string2)

def compose_2input_2input(func1, func2, string1, string2):
    return func1(func2(string1, string2), string2)

def compose_2input_3input(func1, func2, string1, string2, string3):
    return func1(func2(string1, string2, string3), string2)

def compose_3input_1input(func1, func2, string1, string2, string3):
    return func1(func2(string1), string2, string3)

def compose_3input_2input(func1, func2, string1, string2, string3):
    return func1(func2(string1, string2), string2, string3)

def compose_3input_3input(func1, func2, string1, string2, string3):
    return func1(func2(string1, string2, string3), string2, string3)

def generate_random_string(length):
    letters = str.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


# Sampling function
def sample_single_f(base_func_names=None, num_input=1, bool=True):
    if num_input==1:
        func_dict = {"get_string_length": get_string_length, "convert_to_lowercase": convert_to_lowercase, "convert_to_uppercase": convert_to_uppercase,
                    "capitalize_string": capitalize_string, "title_case_string": title_case_string, "reverse_string": reverse_string,
                    "remove_whitespace": remove_whitespace, "get_first_character": get_first_character,
                    "get_last_character": get_last_character, "remove_duplicates": remove_duplicates, "reverse_words": reverse_words,
                    "count_vowels": count_vowels, "count_consonants": count_consonants, 
                    "string_strip": string_strip, "string_lstrip": string_lstrip, "string_rstrip": string_rstrip,
                    "is_palindrome": is_palindrome, "is_alpha": is_alpha, "is_lower": is_lower, "is_upper": is_upper, "is_title": is_title,
                    "add_number_to_string": add_number_to_string, "subtract_number_to_string": subtract_number_to_string, "insert_number": insert_number,
                    "add_letter_if_needed": add_letter_if_needed, "insert_letter": insert_letter, "split_string": split_string,
                    "string_concatenate": string_concatenate, "count_substring": count_substring, "find_string": find_string, 
                    "remove_substring": remove_substring, "starts_with_substring": starts_with_substring, "ends_with_substring": ends_with_substring,
                    "replace_substring": replace_substring,
                    "duplicate_last_letter": duplicate_last_letter,
                    "shift_last_letter": shift_last_letter, 
                    "shift_first_letter": shift_first_letter, 
                    "shift_last_letter_predecessor": shift_last_letter_predecessor, 
                    "shift_first_letter_predecessor": shift_first_letter_predecessor, 
                    "shift_last_letter_forward_two": shift_last_letter_forward_two, 
                    "shift_first_letter_forward_two": shift_first_letter_forward_two, 
                    "shift_last_letter_backward_two": shift_last_letter_backward_two, 
                    "shift_first_letter_backward_two": shift_first_letter_backward_two}

        if base_func_names is None:
            if bool==True:
                base_func_names = ["convert_to_lowercase", "convert_to_uppercase", "capitalize_string", "reverse_string",
                                "remove_whitespace", 
                                # "get_first_character", "get_last_character", 
                                "remove_duplicates", "reverse_words",
                                "string_strip", "string_lstrip", "string_rstrip",
                                "add_number_to_string", "insert_number", "add_letter_if_needed", "insert_letter", 
                                "string_concatenate",  "remove_substring",  "duplicate_last_letter", "replace_substring",
                                "shift_last_letter", 
                                "shift_first_letter", 
                                "shift_last_letter_predecessor", 
                                "shift_first_letter_predecessor", 
                                "shift_last_letter_forward_two", 
                                "shift_first_letter_forward_two", 
                                "shift_last_letter_backward_two", 
                                "shift_first_letter_backward_two"]
            else:
                base_func_names = ["capitalize_string", "reverse_string",
                                "remove_whitespace", 
                                # "get_first_character", "get_last_character", 
                                "remove_duplicates", "reverse_words",
                                "string_strip", "string_lstrip", "string_rstrip",
                                "add_number_to_string", "insert_number", "add_letter_if_needed", "insert_letter",
                                "string_concatenate", "remove_substring", "duplicate_last_letter", "replace_substring"]
    
        func_name = np.random.choice(base_func_names)
        func = func_dict[func_name]


        if func_name in ["add_number_to_string", "subtract_number_to_string", "insert_number"]:
            number = random.randint(1, 10)
            return lambda string: func(string, number), (number), func_name
        
        elif func_name in ["add_letter_if_needed", "insert_letter"]:
            letter = random.choice(str.ascii_letters)
            return lambda string: func(string, letter), (letter), func_name
        
        elif func_name in ["split_string"]:
            # delimiters = str.ascii_lowercase + str.digits + "!@#$%^&*()_+{}[]|\\;:'\"<>,.?/~`"
            delimiters = [",", ";", ":", "|", "/", "\\", ".", "-", "_", " ", "\n", "\t"]
            character = random.choice(delimiters)
            return lambda string: func(string, character), (character), func_name

        elif func_name in ["string_concatenate"]:
            substring_len = random.randint(1, 5)
            substring = generate_random_string(substring_len)
            return lambda string: func(string, substring), (substring), func_name

        elif func_name in ["count_substring", "find_string", "remove_substring", "starts_with_substring", "ends_with_substring"]:
            # substring_len = random.randint(1, 5)
            substring_len = random.randint(1, 1)
            substring = generate_random_string(substring_len)
            return lambda string: func(string, substring), (substring), func_name

        elif func_name in ["replace_substring"]:
            # substring_len = random.randint(1, 5)
            substring_len = random.randint(1, 1)
            old = generate_random_string(substring_len)
            new = generate_random_string(substring_len)
            return lambda string: func(string, old, new), (old, new), func_name
        
        else:
            return lambda string: func(string), (), func_name
    


def sample_f(compound_func_names=None, single_func_names1=None, single_func_names2=None):
    func_dict = {"compose_1input_1input": compose_1input_1input, "compose_1input_2input": compose_1input_2input, "compose_1input_3input": compose_1input_3input,
                "compose_2input_1input": compose_2input_1input, "compose_2input_2input": compose_2input_2input, "compose_2input_3input": compose_2input_3input,
                "compose_3input_1input": compose_3input_1input, "compose_3input_2input": compose_3input_2input, "compose_3input_3input": compose_3input_3input}
    
    func_name = np.random.choice(compound_func_names)
    func = func_dict[func_name]
    
    if func_name == 'compose_1input_1input':
        func1, params1, name1 = sample_single_f(base_func_names=single_func_names1)

        while 1:
            func2, params2, name2 = sample_single_f(base_func_names=single_func_names2, bool=False)
            if name1!=name2:
                break
            # pdb.set_trace()

        func_name = f'{name1};{name2};{func_name}'
        return lambda string: func(func1, func2, string), [params1, params2], func_name


def check_exist(params, f_name, current_funs):
    # print(params, f_name)
    
    if isinstance(params, tuple):
        if len(params)==0:
            same_fun = [fun for fun in current_funs if f_name==fun[0]]
            if len(same_fun)>0:
                return 1
        elif len(params)==1:
            similar_fun = [fun for fun in current_funs if f_name==fun[0]]
            same_fun = [fun for fun in similar_fun if params[0]==fun[1][0]]
            if len(same_fun)>0:
                return 1
        elif len(params)==2:
            similar_fun = [fun for fun in current_funs if f_name==fun[0]]
            same_fun = [fun for fun in similar_fun if params[0]==fun[1][0] and params[1]==fun[1][1]]
            if len(same_fun)>0:
                return 1
        else:
            pdb.set_trace()

    else:
        similar_fun = [fun for fun in current_funs if f_name==fun[0]]
        same_fun = [fun for fun in similar_fun if fun[1]==params]
        if len(same_fun)>0:
            return 1
    
   
def sample_fun(args):
    # pdb.set_trace()
    if random.random() < args.ratio:
        f, params, f_name = sample_single_f(num_input=1)
    else:
        f, params, f_name = sample_f(compound_func_names=["compose_1input_1input"])
    
    return f, params, f_name


def sample(args):

    file_path = "%s/check_list.json"%args.dir
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            current_funs = json.load(file)
    else:
        current_funs = []
    
    ## sample a new function
    f, params, f_name = sample_fun(args)

    
    while 1:
        if 'compose' in f_name:
            assert len(params)==2

            fun1_exist = check_exist(params[0], f_name, current_funs)
            fun2_exist = check_exist(params[1], f_name, current_funs)
            if not (fun1_exist and fun2_exist):
                break
        else:
            fun_exist = check_exist(params, f_name, current_funs)
            if not fun_exist:
                break

        f, params, f_name = sample_fun(args)
        
        
    current_funs.append((f_name, params))
    with open(file_path, "w") as file:
        json.dump(current_funs, file, indent=3)

    return f, params, f_name


    
if __name__ == '__main__':
    for i in range(10):
        f, f_name = sample()
        print(f_name)
