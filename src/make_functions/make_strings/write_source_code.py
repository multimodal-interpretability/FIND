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
            lengths ={{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            length = len(string)
            if str(length) in lengths:
                return lengths[str(length)]
            else:
                return 'unknown'
            """
        elif func_name == "get_digit_indexes":
            code += f"""
            digit_indexes = []
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            
            for char in string:
                digit_indexes = []
                if char.isdigit():
                    digit_indexes.append(digit_names[str(string.find(char))])
            return ' '.join(digit_indexes)
            """
        
        elif func_name == "get_alpha_indexes":
            code += f"""
            alpha_indexes = []
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}

            for char in string:
                if char.isalpha():
                    alpha_indexes.append(digit_names[str(string.find(char))])
            return ' '.join(alpha_indexes)
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
        elif func_name == "reverse_string":
            code += f"""
            return string[::-1]
            """
        elif func_name == "reverse_string_first_half":
            code += f"""
            first_half = string[:len(string)//2]
            last_half = string[len(string)//2:]
            return first_half[::-1] + last_half
            """
        elif func_name == "reverse_string_last_half":
            code += f"""
            first_half = string[:len(string)//2]
            last_half = string[len(string)//2:]
            return first_half + last_half[::-1]
            """
        elif func_name == "extract_digits":
            code += f"""
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine'
            }}
            all_digits = []
            for char in string:
                if char.isdigit():
                    all_digits.append(digit_names[char])
            return ' '.join(all_digits)
            """
        elif func_name == "remove_digits":
            code += f"""
            new_string = ''
            for char in string:
                if not(char.isdigit()):
                    new_string += char
            return new_string
            """
        elif func_name == "extract_uppers":
            code += f"""
            new_string = ''
            for char in string:
                if char.isupper():
                    new_string += char
            return new_string
            """
        elif func_name == "remove_uppers":
            code += f"""
            new_string = ''
            for char in string:
                if not(char.isupper()):
                    new_string += char
            return new_string
            """
        elif func_name == "add_whitespace":
            code += f"""
            new_string = ''
            for char in string:
                new_string += char + ' '
            return new_string
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
        elif func_name == "get_mid_character":
            code += f"""
            length = len(string)
            middle_index = length // 2
            if length % 2 == 0:
                return string[middle_index - 1 : middle_index + 1]
            else:
                return string[middle_index]
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
            numbers = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            vowels = 'aeiouAEIOU'
            return numbers[str(sum(char in vowels for char in string))]
            """
        elif func_name == "reverse_vowels":
            code += f"""
            vowels = 'aeiouAEIOU'
            string = list(string)
            i, j = 0, len(string) - 1

            while i < j:
                if string[i] in vowels and string[j] in vowels:
                    string[i], string[j] = string[j], string[i]
                    i += 1
                    j -= 1
                elif string[i] not in vowels:
                    i += 1
                elif string[j] not in vowels:
                    j -= 1
            
            return ''.join(string)
            """
        elif func_name == "capitalize_alternating_letters":
            code += f"""
            capitalized_string = ""
            for i, char in enumerate(string):
                if i % 2 == 0:
                    capitalized_string += char.upper()
                else:
                    capitalized_string += char.lower()
            return capitalized_string
            """
        elif func_name == "replace_vowels_with_character":
            code += f"""
            replacement_char = "{params}"
            vowels = 'aeiouAEIOU'
            replaced_string = ""
            for char in string:
                if char in vowels:
                    replaced_string += replacement_char
                else:
                    replaced_string += char
            return replaced_string
            """
        elif func_name == "replace_vowels_with_first":
            code += f"""
            replacement_char = string[0]
            vowels = 'aeiouAEIOU'
            replaced_string = ""
            for char in string:
                if char in vowels:
                    replaced_string += replacement_char
                else:
                    replaced_string += char
            return replaced_string
            """
        elif func_name == "replace_vowels_with_last":
            code += f"""
            replacement_char = string[-1]
            vowels = 'aeiouAEIOU'
            replaced_string = ""
            for char in string:
                if char in vowels:
                    replaced_string += replacement_char
                else:
                    replaced_string += char
            return replaced_string
            """
        elif func_name == "replace_vowels_with_mid":
            code += f"""
            if len(string)<2:
                return string
            replacement_char = string[len(string)//2]
            vowels = 'aeiouAEIOU'
            replaced_string = ""
            for char in string:
                if char in vowels:
                    replaced_string += replacement_char
                else:
                    replaced_string += char
            return replaced_string
            """
        elif func_name == "replace_vowels_with_ind_of_count":
            code += f"""
            vowels = 'aeiouAEIOU'
            replaced_string = ""
            count = 0
            for char in string:
                if char in vowels:
                    count+=1
            replacement_char = string[count-1]
            for char in string:
                if char in vowels:   
                    replaced_string += replacement_char
                else:
                    replaced_string += char
            return replaced_string
            """
        elif func_name == "count_consonants":
            code += f"""
            numbers = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            consonants = 'abcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
            return numbers[str(sum([char in consonants for char in string]))]
            """
        elif func_name == "count_uppercase":
            code += f"""
            uppercase_count = 0
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            for char in string:
                if char.isupper():
                    uppercase_count += 1    
            return digit_names[str(uppercase_count)]
            """
        elif func_name == "count_lowercase":
            code += f"""
            uppercase_count = 0
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            for char in string:
                if char.islower():
                    uppercase_count += 1    
            return digit_names[str(uppercase_count)]
            """
        elif func_name == "count_character_repetitions":
            code += f"""
            char = '{params}'
            count = 0
            digit_names = {{
            '0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve',
            '13': 'thirteen',
            '14': 'fourteen',
            '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen',
            '18': 'eighteen',
            '19': 'nineteen',
            '20': 'twenty',
            '21': 'twenty-one',
            '22': 'twenty-two',
            '23': 'twenty-three',
            '24': 'twenty-four',
            '25': 'twenty-five',
            '26': 'twenty-six',
            '27': 'twenty-seven',
            '28': 'twenty-eight',
            '29': 'twenty-nine',
            '30': 'thirty'
            }}
            for c in string:
                if c == char:
                    count += 1
            return digit_names[str(count)]
            """
        elif func_name == "string_strip":
            code += f"""
            return string.strip()
            """
        elif func_name == "string_lstrip":
            code += f"""
            return string.lstrip()
            """
        elif func_name == "string_rstrip":
            code += f"""
            return string.rstrip()
            """
                    
        elif func_name == "advance_by_character_order":
            code += f"""
            inx = {params}
            if len(string)<inx+1: 
                return string
            char_inx = string[inx].lower()
            order = ord(char_inx) - ord('a')

            advanced_string = ""
            for char in string:
                if char.isalpha():
                    new_char = chr((ord(char.lower()) - ord('a') + order) % 26 + ord('a'))
                else:
                    new_char = char
                advanced_string += new_char
            return advanced_string
            """
            
        elif func_name == "substract_by_character_order":
            code += f"""
            inx = {params}
            if len(string)<inx+1: 
                return string
            char_inx = string[inx].lower()
            order = ord(char_inx) - ord('a')

            advanced_string = ""
            for char in string:
                if char.isalpha():
                    new_char = chr((ord(char.lower()) - ord('a') - order) % 26 + ord('a'))
                else:
                    new_char = char
                advanced_string += new_char
            return advanced_string
            """
            
        elif func_name == "add_len_to_string":
            code += f"""
            result = ""
            number = len(string)
            for char in string:
                if char.isalpha():
                    if char.islower():
                        new_char = chr((ord(char) - ord('a') + number) % 26 + ord('a'))
                    else:
                        new_char = chr((ord(char) - ord('A') + number) % 26 + ord('A'))
                    result += new_char
                else:
                    result += char
            return result
            """

        elif func_name == "add_number_to_middle":
            code += f"""
            number = {params}
            length = len(string)
            if length % 2 == 0 or length < 3:
                return string

            middle_index = length // 2
            middle_char = string[middle_index]

            if middle_char.isalpha():
                if middle_char.islower():
                    new_middle_char = chr((ord(middle_char) - ord('a') + number) % 26 + ord('a'))
                else:
                    new_middle_char = chr((ord(middle_char) - ord('A') + number) % 26 + ord('A'))
                result = string[:middle_index] + new_middle_char + string[middle_index + 1:]
            else:
                result = string
            return result
            """

        elif func_name == "add_len_to_middle":
            code += f"""
            length = len(string)
            number = length
            if length % 2 == 0 or length < 3:
                return string

            middle_index = length // 2
            middle_char = string[middle_index]

            if middle_char.isalpha():
                if middle_char.islower():
                    new_middle_char = chr((ord(middle_char) - ord('a') + number) % 26 + ord('a'))
                else:
                    new_middle_char = chr((ord(middle_char) - ord('A') + number) % 26 + ord('A'))
                result = string[:middle_index] + new_middle_char + string[middle_index + 1:]
            else:
                result = string
            return result
            """

        elif func_name == "add_order_to_inx":
            code += f"""
            import random
            if len(string)<2:
                return string
            length = len(string)
            inx = random.randint(0, length-1)
            number = inx

            inx_char = string[inx]

            if inx_char.isalpha():
                if inx_char.islower():
                    new_char = chr((ord(inx_char) - ord('a') + number) % 26 + ord('a'))
                else:
                    new_char = chr((ord(inx_char) - ord('A') + number) % 26 + ord('A'))
                result = string[:inx] + new_char + string[inx + 1:]
            else:
                result = string
            return result            
            """

        elif func_name == "add_order_of_inx1_to_inx2":
            code += f"""
            inx1 = {params[0]}
            inx2 = {params[1]}
            length = len(string)
            if (length< inx1+1) or (length< inx2+1):
                return string
            number = inx1

            inx_char = string[inx2]

            if inx_char.isalpha():
                if inx_char.islower():
                    new_char = chr((ord(inx_char) - ord('a') + number) % 26 + ord('a'))
                else:
                    new_char = chr((ord(inx_char) - ord('A') + number) % 26 + ord('A'))
                result = string[:inx2] + new_char + string[inx2 + 1:]
            else:
                result = string
            return result            
            """

        elif func_name == "sub_order_to_inx":
            code += f"""
            import random
            if len(string)<2:
                return string
            length = len(string)
            inx = random.randint(0, length-1)
            number = inx

            inx_char = string[inx]

            if inx_char.isalpha():
                if inx_char.islower():
                    new_char = chr((ord(inx_char) - ord('a') - number) % 26 + ord('a'))
                else:
                    new_char = chr((ord(inx_char) - ord('A') - number) % 26 + ord('A'))
                result = string[:inx] + new_char + string[inx + 1:]
            else:
                result = string
            return result
            """

        elif func_name == "sub_order_of_inx1_to_inx2":
            code += f"""
            inx1 = {params[0]}
            inx2 = {params[1]}
            length = len(string)
            if (length< inx1+1) or (length< inx2+1):
                return string
            number = inx1

            inx_char = string[inx2]

            if inx_char.isalpha():
                if inx_char.islower():
                    new_char = chr((ord(inx_char) - ord('a') + number) % 26 + ord('a'))
                else:
                    new_char = chr((ord(inx_char) - ord('A') + number) % 26 + ord('A'))
                result = string[:inx2] + new_char + string[inx2 + 1:]
            else:
                result = string

            return result            
            """

        elif func_name == "subtract_number_to_string":
            code += f"""
            number = {params}
            result = ""
            for char in string:
                if char.isalpha():
                    if char.islower():
                        new_char = chr((ord(char) - ord('a') - number) % 26 + ord('a'))
                    else:
                        new_char = chr((ord(char) - ord('A') - number) % 26 + ord('A'))
                    result += new_char
                else:
                    result += char
            return result            
            """


        elif func_name == "subtract_middle_character":
            code += f"""
            number = {params}
            length = len(string)
            if length % 2 == 0 or length < 3:
                return string

            middle_index = length // 2
            middle_char = string[middle_index]

            if middle_char.isalpha():
                if middle_char.islower():
                    new_middle_char = chr((ord(middle_char) - ord('a') - number) % 26 + ord('a'))
                else:
                    new_middle_char = chr((ord(middle_char) - ord('A') - number) % 26 + ord('A'))
                result = string[:middle_index] + new_middle_char + string[middle_index + 1:]
            else:
                result = string
            return result            
            """
        
        elif func_name == "duplicate_first_letter":
            code += f"""
            return string+string[0]
            """

        elif func_name == "duplicate_last_letter":
            code += f"""
            return string+string[-1]
            """

        elif func_name == "duplicate_mid_letter":
            code += f"""
            return string+string[len(string)//2]
            """

        elif func_name == "swap_first_last":
            code += f"""
            if len(string)<2:
                return string    
            return string[-1]+string[1:-1]+string[0]
            """
            
        elif func_name == "swap_rand":
            code += f"""
            ind1 = {params[0]}
            ind2 = {params[1]}
            if len(string)-1<ind1 or len(string)-1<ind2:
                return string 
            new_string = ''
            for ind in range(len(string)):
                if ind == ind1:
                    new_string+=string[ind2]
                elif ind == ind2:
                    new_string+=string[ind1]
                else:
                    new_string+=string[ind]
            return new_string
            """

        elif func_name == "map_string":
            code += f"""
            mapping_dict = {params}
            mapped_string = ""
            for char in string:
                mapped_char = mapping_dict.get(char.lower(), char)
                mapped_string += mapped_char
            return mapped_string
            """

        elif func_name == "get_first_character_ordinality":
            code += f"""
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
            }}
            first_character = string[0].lower()
            if not(first_character.isalpha()): return 'zero'
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            order = alphabet.index(first_character) + 1
            return digit_names[str(order)]
            """

        elif func_name == "get_last_character_ordinality":
            code += f"""
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
            }}
            first_character = string[-1].lower()
            if not(first_character.isalpha()): return 'zero'
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            order = alphabet.index(first_character) + 1
            return digit_names[str(order)]
            """
        
        elif func_name == "get_mid_character_ordinality":
            code += f"""
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
            }}
            first_character = string[len(string)//2].lower()
            if not(first_character.isalpha()): return 'zero'
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            order = alphabet.index(first_character) + 1
            return digit_names[str(order)]
            """

        elif func_name == "shift_last_letter_rand":
            code += f"""
            rand = {params}
            if string == "" or not string[-1].isalpha():   # Empty string or last character not a letter
                return string
            elif string[-1] == 'z':   # wrap around from 'z' to 'a'
                return string[:-1] + 'a'
            elif string[-1] == 'Z':   # wrap around from 'Z' to 'A'
                return string[:-1] + 'A'
            else:   # shift forward one letter in the alphabet
                return string[:-1] + chr(ord(string[-1]) + rand)
            """
        
        elif func_name == "shift_first_letter_rand":
            code += f"""
            rand = {params}
            if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
                return string
            elif string[0] == 'z':   # wrap around from 'z' to 'a'
                return 'a' + string[1:]
            elif string[0] == 'Z':   # wrap around from 'Z' to 'A'
                return 'A' + string[1:]
            else:   # shift forward one letter in the alphabet
                return chr(ord(string[0]) + rand) + string[1:]
            """

        elif func_name == "shift_last_letter_predecessor_rand":
            code += f"""
            rand = {params}
            if string == "" or not string[-1].isalpha():  # Empty string or last character not a letter
                return string
            elif string[-1] == 'a':  # wrap around from 'a' to 'z'
                return string[:-1] + 'z'
            elif string[-1] == 'A':  # wrap around from 'A' to 'Z'
                return string[:-1] + 'Z'
            else:  # shift back one letter in the alphabet
                return string[:-1] + chr(ord(string[-1]) - rand)
            """
        elif func_name == "shift_first_letter_predecessor_rand":
            code += f"""
            rand = {params}
            if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
                return string
            elif string[0] == 'a':  # wrap around from 'a' to 'z'
                return 'z' + string[1:]
            elif string[0] == 'A':  # wrap around from 'A' to 'Z'
                return 'Z' + string[1:]
            else:  # shift back one letter in the alphabet
                return chr(ord(string[0]) - rand) + string[1:]
            """

        # elif func_name == "is_palindrome":
        #     code += f"""
        #     cleaned_string = string.lower().replace(" ", "")
        #     return cleaned_string == cleaned_string[::-1]
        #     """
        # elif func_name == "is_numeric":
        #     code += f"""
        #     return string.isnumeric()
        #     """
        # elif func_name == "is_alpha":
        #     code += f"""
        #     return string.isalpha()
        #     """
        # elif func_name == "is_digit":
        #     code += f"""
        #     return string.isdigit()
        #     """
        # elif func_name == "is_lower":
        #     code += f"""
        #     return string.islower()
        #     """
        # elif func_name == "is_upper":
        #     code += f"""
        #     return string.isupper()
        #     """
        # elif func_name == "is_title":
        #     code += f"""
        #     return string.istitle()
        #     """

        elif func_name == "add_number_to_string":
            code += f"""
            number = {params}
            result = ""
            for char in string:
                if char.isalpha():
                    if char.islower():
                        new_char = chr((ord(char) - ord('a') + number) % 26 + ord('a'))
                    else:
                        new_char = chr((ord(char) - ord('A') + number) % 26 + ord('A'))
                    result += new_char
                else:
                    result += char
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
            return ' '.join(string.split(substring))    
            """

        elif func_name == "string_concatenate":
            code += f"""
            new_string = '{params}'

            return string + new_string
            """

        elif func_name == "count_substring":
            code += f"""
            substring = '{params}'
            digit_names = {{
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            string_count = string.count(substring)
            return digit_names[str(string_count)]
            """
        elif func_name == "find_string":
            code += f"""
            substring = '{params}'
            digit_names = {{
                '-1': 'none',
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen',
                '20': 'twenty',
                '21': 'twenty-one',
                '22': 'twenty-two',
                '23': 'twenty-three',
                '24': 'twenty-four',
                '25': 'twenty-five',
                '26': 'twenty-six',
                '27': 'twenty-seven',
                '28': 'twenty-eight',
                '29': 'twenty-nine',
                '30': 'thirty'
            }}
            string_find = string.find(substring)
            return digit_names[str(string_find)]
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

        # elif func_name == "name":
        #     code += f"""
        #     """

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
    

    
    

        

