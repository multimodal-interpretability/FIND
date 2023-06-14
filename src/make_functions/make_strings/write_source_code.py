# main script
import pdb
import random
import string_functions as sf
import textwrap


def write_simple_function(params, func_name, f_name='function'):
    
    if False:
        pass
    else:
        # pdb.set_trace()
        # Now we're going to create a Python script file that represents this function
        code = f"""

        def {f_name}(string):
            """

        # For each type of function, we need to generate code accordingly
        if func_name == "get_string_length":
            code += f"""
            return len(string)
            """
        elif func_name == "convert_to_lowercase":
            code += f"""
            return string.lower()
            """
        elif func_name == "convert_to_uppercase":
            code += f"""
            return string.upper()
            """
        elif func_name == "capitalize_string":
            code += f"""
            return string.capitalize()
            """
        elif func_name == "title_case_string":
            code += f"""
            return string.title()
            """
        elif func_name == "reverse_string":
            code += f"""
            return string[::-1]
            """
        elif func_name == "extract_digits":
            code += f"""
            return ''.join(filter(str.isdigit, string))
            """
        elif func_name == "remove_whitespace":
            code += f"""
            return ''.join(string.split())
            """
        elif func_name == "get_first_character":
            code += f"""
            return string[0]
            """
        elif func_name == "get_last_character":
            code += f"""
            return string[-1]
            """
        elif func_name == "remove_duplicates":
            code += f"""
            return ''.join(sorted(set(string), key=string.index))
            """
        elif func_name == "reverse_words":
            code += f"""
            words = string.split()
            reversed_words = [word[::-1] for word in words]
            return ' '.join(reversed_words)
            """
        elif func_name == "count_vowels":
            code += f"""
            vowels = 'aeiouAEIOU'
            return sum(char in vowels for char in string)
            """
        elif func_name == "count_consonants":
            code += f"""
            consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
            return sum(char in consonants for char in string)
            """
        elif func_name == "string_strip":
            code += f"""
            return string.strip()
            """
        elif func_name == "string_lstrip":
            code += f"""
            return string.lstrip()
            """
        elif func_name == "duplicate_last_letter":
            code += f"""
            return string+string[-1]
            """


        elif func_name == "shift_last_letter":
            code += f"""
            if string == "" or not string[-1].isalpha():   # Empty string or last character not a letter
                return string
            elif string[-1] == 'z':   # wrap around from 'z' to 'a'
                return string[:-1] + 'a'
            elif string[-1] == 'Z':   # wrap around from 'Z' to 'A'
                return string[:-1] + 'A'
            else:   # shift forward one letter in the alphabet
                return string[:-1] + chr(ord(string[-1]) + 1)
            """
        elif func_name == "shift_first_letter":
            code += f"""
            if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
                return string
            elif string[0] == 'z':   # wrap around from 'z' to 'a'
                return 'a' + string[1:]
            elif string[0] == 'Z':   # wrap around from 'Z' to 'A'
                return 'A' + string[1:]
            else:   # shift forward one letter in the alphabet
                return chr(ord(string[0]) + 1) + string[1:]
            """
        elif func_name == "shift_last_letter_predecessor":
            code += f"""
            if string == "" or not string[-1].isalpha():  # Empty string or last character not a letter
                return string
            elif string[-1] == 'a':  # wrap around from 'a' to 'z'
                return string[:-1] + 'z'
            elif string[-1] == 'A':  # wrap around from 'A' to 'Z'
                return string[:-1] + 'Z'
            else:  # shift back one letter in the alphabet
                return string[:-1] + chr(ord(string[-1]) - 1)
            """
        elif func_name == "shift_first_letter_predecessor":
            code += f"""
            if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
                return string
            elif string[0] == 'a':  # wrap around from 'a' to 'z'
                return 'z' + string[1:]
            elif string[0] == 'A':  # wrap around from 'A' to 'Z'
                return 'Z' + string[1:]
            else:  # shift back one letter in the alphabet
                return chr(ord(string[0]) - 1) + string[1:]
            """
        elif func_name == "shift_last_letter_forward_two":
            code += f"""
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
            """
        elif func_name == "shift_first_letter_forward_two":
            code += f"""
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
            """
        elif func_name == "shift_last_letter_backward_two":
            code += f"""
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
            """
        elif func_name == "shift_first_letter_backward_two":
            code += f"""
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
            """
        

        elif func_name == "string_rstrip":
            code += f"""
            return string.rstrip()
            """
        elif func_name == "is_palindrome":
            code += f"""
            cleaned_string = string.lower().replace(" ", "")
            return cleaned_string == cleaned_string[::-1]
            """
        elif func_name == "is_numeric":
            code += f"""
            return string.isnumeric()
            """
        elif func_name == "is_alpha":
            code += f"""
            return string.isalpha()
            """
        elif func_name == "is_digit":
            code += f"""
            return string.isdigit()
            """
        elif func_name == "is_lower":
            code += f"""
            return string.islower()
            """
        elif func_name == "is_upper":
            code += f"""
            return string.isupper()
            """
        elif func_name == "is_title":
            code += f"""
            return string.istitle()
            """

        elif func_name == "add_number_to_string":
            code += f"""
            number = {params}

            result = ""
            for char in string:
                new_char = chr(ord(char) + number)
                result += new_char
            return result
            """
        elif func_name == "subtract_number_to_string":
            code += f"""
            number = {params}

            result = ""
            for char in string:
                new_char = chr(ord(char) - number)
                result += new_char
            return result
            """
        elif func_name == "insert_number":
            code += f"""
            number = {params}

            mid_index = len(string) // 2
            new_string = string[:mid_index] + str(number) + string[mid_index:]
            return new_string
            """
        elif func_name == "add_letter_if_needed":
            code += f"""
            letter = '{params}'

            if not string.endswith(letter):
                string += letter
            return string
            """
        elif func_name == "insert_letter":
            code += f"""
            letter = '{params}'

            mid_index = len(string) // 2
            new_string = string[:mid_index] + letter + string[mid_index:]
            return new_string
            """

        elif func_name == "split_string":
            # pdb.set_trace()
            code += f"""
            substring = '{params}'
            
            return string.split(substring)
            """

        elif func_name == "string_concatenate":
            code += f"""
            new_string = '{params}'

            return string + new_string
            """

        elif func_name == "count_substring":
            code += f"""
            substring = '{params}'

            return string.count(substring)
            """

        elif func_name == "find_string":
            code += f"""
            substring = '{params}'

            return string.find(substring)
            """

        elif func_name == "remove_substring":
            code += f"""
            substring = '{params}'

            return string.replace(substring, '')
            """

        elif func_name == "starts_with_substring":
            code += f"""
            substring = '{params}'

            return string.startswith(substring)
            """

        elif func_name == "ends_with_substring":
            code += f"""
            substring = '{params}'

            return string.endswith(substring)
            """

        elif func_name == "replace_substring":
            code += f"""
            old = '{params[0]}'
            new = '{params[1]}'

            return string.replace(old, new)
            """
        else:
            raise ValueError(f"Unknown function name: {func_name}")
        # import textwrap
        # code = textwrap.dedent(code)


    return code




def write_function(params, func_name, dirname, corrupted=None, cparams=None, cname=None):
    code = """
    import numpy as np
    import scipy.signal
    import sys
    """
    code = textwrap.dedent(code)

    if ';' not in func_name:
        function_code = write_simple_function(params, func_name)
        function_code = textwrap.dedent(function_code)
        code += function_code
        new_code = ""
    else:
        params1, params2 = params
        func_name1, func_name2, func_name = func_name.split(';')
        code1 = write_simple_function(params1, func_name1, f_name='function1')
        code2 = write_simple_function(params2, func_name2, f_name='function2')
        
        code1 = textwrap.dedent(code1)
        code2 = textwrap.dedent(code2)
        code += code1 + code2


        if func_name == 'compose_1input_1input':
            new_code = f"""
            def function(string):
                return function1(function2(string))
            """
        
        elif func_name == 'compose_1input_2input':
            new_code = f"""
            def function(string1, string2):
                return function1(function2(string1, string2))
            """

        elif func_name == 'compose_1input_3input':
            new_code = f"""
            def function(string1, string2, string3):
                return function1(function2(string1, string2, string3))
            """

        elif func_name == 'compose_2input_1input':
            new_code = f"""
            def function(string1, string2):
                return function1(function2(string1), string2)
            """

        elif func_name == 'compose_2input_2input':
            new_code = f"""
            def function(string1, string2):
                return function1(function2(string1, string2), string2)
            """

        elif func_name == 'compose_2input_3input':
            new_code = f"""
            def function(string1, string2, string3):
                return function1(function2(string1, string2, string3), string2)
            """

        elif func_name == 'compose_3input_1input':
            new_code = f"""
            def function(string1, string2, string3):
                return function1(function2(string1), string2, string3)
            """

        elif func_name == 'compose_3input_2input':
            new_code = f"""
            def function(string1, string2, string3):
                return function1(function2(string1, string2), string2, string3)
            """

        elif func_name == 'compose_3input_3input':
            new_code = f"""
            def function(string1, string2, string3):
                return function1(function2(string1, string2, string3), string2, string3)
            """

        else:
            raise ValueError('Unknown function name')

    new_code = textwrap.dedent(new_code)

    run_code = """
    if __name__ == '__main__':
        outputs = ''
        for arg in sys.argv[1:]:
            string = str(arg)
            outputs += f'({arg}, {str(function(string))}) '

        print(f'Function input - output pairs: {outputs}')
    """


    code += new_code

    code += textwrap.dedent(run_code)

    with open(f"{dirname}/function_code.py", "w") as file:
        file.write(code)
    

    
    

        

