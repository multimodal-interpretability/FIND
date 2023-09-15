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
    lengths = {
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
    }
    length = len(string)
    if str(length) in lengths:
        return lengths[str(length)]
    else:
        return 'unknown'


def get_digit_indexes(string):
    digit_indexes = []
    digit_names = {
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
    }
    
    for char in string:
        digit_indexes = []
        if char.isdigit():
            digit_indexes.append(digit_names[str(string.find(char))])
    return ' '.join(digit_indexes)


def get_alpha_indexes(string):
    alpha_indexes = []
    digit_names = {
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
    }
    
    for char in string:
        if char.isalpha():
            alpha_indexes.append(digit_names[str(string.find(char))])
    return ' '.join(alpha_indexes)


def convert_to_lowercase(string):
    return string.lower()


def convert_to_uppercase(string):
    return string.upper()


def capitalize_string(string):
    return string.capitalize()


def reverse_string(string):
    return string[::-1]


def reverse_string_first_half(string):
    first_half = string[:len(string)//2]
    last_half = string[len(string)//2:]
    return first_half[::-1] + last_half


def reverse_string_last_half(string):
    first_half = string[:len(string)//2]
    last_half = string[len(string)//2:]
    return first_half + last_half[::-1]


def extract_digits(string):
    digit_names = {
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
    }
    
    all_digits = []
    for char in string:
        if char.isdigit():
            all_digits.append(digit_names[char])
    return ' '.join(all_digits)


def remove_digits(string):
    new_string = ''
    for char in string:
        if not(char.isdigit()):
            new_string += char
    return new_string


def extract_uppers(string):
    new_string = ''
    for char in string:
        if char.isupper():
            new_string += char
    return new_string


def remove_uppers(string):
    new_string = ''
    for char in string:
        if not(char.isupper()):
            new_string += char
    return new_string


def add_whitespace(string):
    new_string = ''
    for char in string:
        new_string += char + ' '
    return new_string


def remove_whitespace (string):
    return ''.join(string.split())


def get_first_character(string):
    return string[0]


def get_last_character(string):
    return string[-1]


def get_mid_character(string):
    length = len(string)
    middle_index = length // 2
    if length % 2 == 0:
        return string[middle_index - 1 : middle_index + 1]
    else:
        return string[middle_index]


def remove_duplicates(string):
    return ''.join(sorted(set(string), key=string.index))


def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


def count_vowels(string):
    numbers = {
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
    }
    vowels = 'aeiouAEIOU'
    return numbers[str(sum(char in vowels for char in string))]

def reverse_vowels(string):
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

def capitalize_alternating_letters(string):
    capitalized_string = ""
    for i, char in enumerate(string):
        if i % 2 == 0:
            capitalized_string += char.upper()
        else:
            capitalized_string += char.lower()
    return capitalized_string

def replace_vowels_with_character(string, replacement_char):
    vowels = 'aeiouAEIOU'
    replaced_string = ""
    for char in string:
        if char in vowels:
            replaced_string += replacement_char
        else:
            replaced_string += char
    return replaced_string

def replace_vowels_with_first(string):
    replacement_char = string[0]
    vowels = 'aeiouAEIOU'
    replaced_string = ""
    for char in string:
        if char in vowels:
            replaced_string += replacement_char
        else:
            replaced_string += char
    return replaced_string


def replace_vowels_with_last(string):
    replacement_char = string[-1]
    vowels = 'aeiouAEIOU'
    replaced_string = ""
    for char in string:
        if char in vowels:
            replaced_string += replacement_char
        else:
            replaced_string += char
    return replaced_string


def replace_vowels_with_mid(string):
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

def replace_vowels_with_ind_of_count(string):
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


def count_consonants(string):
    numbers = {
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
    }
    consonants = 'abcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return numbers[str(sum([char in consonants for char in string]))]

def count_uppercase(string):
    uppercase_count = 0
    digit_names = {
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
    }
    for char in string:
        if char.isupper():
            uppercase_count += 1    
    return digit_names[str(uppercase_count)]

def count_lowercase(string):
    lowercase_count = 0
    digit_names = {
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
    }
    for char in string:
        if char.islower():
            lowercase_count += 1    
    return digit_names[str(lowercase_count)]
    
def count_character_repetitions(string, char):
    count = 0
    digit_names = {
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
    }
    for c in string:
        if c == char:
            count += 1
    return digit_names[str(count)]

def string_strip(string):
    return string.strip()


def string_lstrip(string):
    return string.lstrip()


def string_rstrip(string):
    return string.rstrip()


def add_number_to_string(string, number):
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

def advance_by_character_order(string, inx):
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


def substract_by_character_order(string, inx):
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


def add_len_to_string(string):
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

def add_number_to_middle(string, number):
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

def add_len_to_middle(string):
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

def add_order_to_inx(string):
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

def add_order_of_inx1_to_inx2(string, inx1, inx2):
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

def sub_order_to_inx(string):
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

def sub_order_of_inx1_to_inx2(string, inx1, inx2):
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

def subtract_number_to_string(string, number):
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

def subtract_middle_character(string, number):
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
    return ' '.join(string.split(substring))


def string_concatenate(string, new_string):
    return string + new_string


def count_substring(string, substring):
    digit_names = {
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
    }
    string_count = string.count(substring)
    return digit_names[str(string_count)]


def find_string(string, substring):
    digit_names = {
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
    }
    string_find = string.find(substring)
    return digit_names[str(string_find)]


def remove_substring(string, substring):
    return string.replace(substring, '')


def starts_with_substring(string, substring):
    return string.startswith(substring)


def ends_with_substring(string, substring):
    return string.endswith(substring)


def replace_substring(string, old, new):
    return string.replace(old, new)


def duplicate_first_letter(string):
    return string+string[0]
 

def duplicate_last_letter(string):
    return string+string[-1]


def duplicate_mid_letter(string):
    return string+string[len(string)//2]


def swap_first_last(string):
    if len(string)<2:
        return string    
    return string[-1]+string[1:-1]+string[0]


def swap_rand(string, ind1, ind2):
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


def map_string(string, mapping_dict):
    mapped_string = ""
    for char in string:
        mapped_char = mapping_dict.get(char.lower(), char)
        mapped_string += mapped_char
    return mapped_string

def get_first_character_ordinality(string):
    digit_names = {
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
    }
    first_character = string[0].lower()
    if not(first_character.isalpha()): return 'zero'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    order = alphabet.index(first_character) + 1
    return digit_names[str(order)]

def get_last_character_ordinality(string):
    digit_names = {
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
    }
    first_character = string[-1].lower()
    if not(first_character.isalpha()): return 'zero'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    order = alphabet.index(first_character) + 1
    return digit_names[str(order)]

def get_mid_character_ordinality(string):
    digit_names = {
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
    }
    first_character = string[len(string)//2].lower()
    if not(first_character.isalpha()): return 'zero'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    order = alphabet.index(first_character) + 1
    return digit_names[str(order)]


def shift_last_letter_rand(string, rand):
    if string == "" or not string[-1].isalpha():   # Empty string or last character not a letter
        return string
    elif string[-1] == 'z':   # wrap around from 'z' to 'a'
        return string[:-1] + 'a'
    elif string[-1] == 'Z':   # wrap around from 'Z' to 'A'
        return string[:-1] + 'A'
    else:   # shift forward one letter in the alphabet
        return string[:-1] + chr(ord(string[-1]) + rand)
    
def shift_first_letter_rand(string, rand):
    if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
        return string
    elif string[0] == 'z':   # wrap around from 'z' to 'a'
        return 'a' + string[1:]
    elif string[0] == 'Z':   # wrap around from 'Z' to 'A'
        return 'A' + string[1:]
    else:   # shift forward one letter in the alphabet
        return chr(ord(string[0]) + rand) + string[1:]
    

def shift_last_letter_predecessor_rand(string, rand):
    if string == "" or not string[-1].isalpha():  # Empty string or last character not a letter
        return string
    elif string[-1] == 'a':  # wrap around from 'a' to 'z'
        return string[:-1] + 'z'
    elif string[-1] == 'A':  # wrap around from 'A' to 'Z'
        return string[:-1] + 'Z'
    else:  # shift back one letter in the alphabet
        return string[:-1] + chr(ord(string[-1]) - rand)


def shift_first_letter_predecessor_rand(string, rand):
    if string == "" or not string[0].isalpha():  # Empty string or first character not a letter
        return string
    elif string[0] == 'a':  # wrap around from 'a' to 'z'
        return 'z' + string[1:]
    elif string[0] == 'A':  # wrap around from 'A' to 'Z'
        return 'Z' + string[1:]
    else:  # shift back one letter in the alphabet
        return chr(ord(string[0]) - rand) + string[1:]


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
def sample_single_f(base_func_names=None, num_input=1, not_composed=True):
    if num_input==1:
        func_dict = {"get_string_length": get_string_length, "get_digit_indexes": get_digit_indexes, "get_alpha_indexes": get_alpha_indexes, "convert_to_lowercase": convert_to_lowercase, "convert_to_uppercase": convert_to_uppercase,
                    "capitalize_string": capitalize_string, "reverse_string": reverse_string, "reverse_string_first_half": reverse_string_first_half, "reverse_string_last_half": reverse_string_last_half,
                    "extract_digits": extract_digits, "remove_digits": remove_digits, "extract_uppers": extract_uppers, "remove_upper": extract_uppers,
                    "remove_whitespace": remove_whitespace, "get_first_character": get_first_character,
                    "get_last_character": get_last_character, "get_mid_character": get_mid_character,
                    "remove_duplicates": remove_duplicates, "reverse_words": reverse_words, 
                    "count_vowels": count_vowels, "reverse_vowels": reverse_vowels, "capitalize_alternating_letters": capitalize_alternating_letters,
                    "replace_vowels_with_character": replace_vowels_with_character, "replace_vowels_with_first": replace_vowels_with_first, "replace_vowels_with_last": replace_vowels_with_last, "replace_vowels_with_mid": replace_vowels_with_mid, "replace_vowels_with_ind_of_count": replace_vowels_with_ind_of_count,
                    "count_consonants": count_consonants, "count_uppercase": count_uppercase, "count_lowercase": count_lowercase, "count_character_repetitions": count_character_repetitions,
                    "string_strip": string_strip, "string_lstrip": string_lstrip, "string_rstrip": string_rstrip,
                    "add_number_to_string": add_number_to_string, "advance_by_character_order": advance_by_character_order, "substract_by_character_order": substract_by_character_order,
                    "add_len_to_string": add_len_to_string, "add_number_to_middle": add_number_to_middle, "add_len_to_middle": add_len_to_middle,
                    "add_order_to_inx": add_order_to_inx, "add_order_of_inx1_to_inx2": add_order_of_inx1_to_inx2, "sub_order_to_inx": sub_order_to_inx, "sub_order_of_inx1_to_inx2": sub_order_of_inx1_to_inx2,
                    "subtract_number_to_string": subtract_number_to_string, "subtract_middle_character": subtract_middle_character,
                    "insert_number": insert_number,
                    "add_letter_if_needed": add_letter_if_needed, "insert_letter": insert_letter, "split_string": split_string,
                    "string_concatenate": string_concatenate, "count_substring": count_substring, "find_string": find_string, 
                    "remove_substring": remove_substring, "starts_with_substring": starts_with_substring, "ends_with_substring": ends_with_substring,
                    "replace_substring": replace_substring,
                    "duplicate_first_letter": duplicate_first_letter, "duplicate_last_letter": duplicate_last_letter, "duplicate_mid_letter": duplicate_mid_letter,
                    "swap_first_last": swap_first_last, "swap_rand": swap_rand,  "map_string":  map_string,
                    "get_first_character_ordinality": get_first_character_ordinality, "get_last_character_ordinality": get_last_character_ordinality, "get_mid_character_ordinality": get_mid_character_ordinality,
                    "shift_last_letter_rand": shift_last_letter_rand, 
                    "shift_first_letter_rand": shift_first_letter_rand, 
                    "shift_last_letter_predecessor_rand": shift_last_letter_predecessor_rand, 
                    "shift_first_letter_predecessor_rand": shift_first_letter_predecessor_rand, 
                    }

        if base_func_names is None:
            if not_composed:
                base_func_names = ["convert_to_lowercase", "convert_to_uppercase", "capitalize_string", "reverse_string", "reverse_string_first_half", "reverse_string_last_half",
                                   "extract_digits", "remove_digits", "extract_uppers",
                                    "remove_whitespace", "get_string_length", "get_digit_indexes", "get_alpha_indexes",
                                    "get_first_character", "get_last_character", "get_mid_character",
                                    "remove_duplicates", "reverse_words", "count_vowels", 
                                    "replace_vowels_with_character", "replace_vowels_with_first", "replace_vowels_with_last", "replace_vowels_with_mid", "replace_vowels_with_ind_of_count",
                                    "reverse_vowels", "capitalize_alternating_letters",
                                    "count_consonants", "count_uppercase", "count_lowercase", "count_character_repetitions",
                                    "string_strip", "string_lstrip", "string_rstrip",
                                    "add_number_to_string", "advance_by_character_order", "substract_by_character_order",
                                    "add_len_to_string", "add_number_to_middle", "add_len_to_middle",
                                    "add_order_to_inx", "add_order_of_inx1_to_inx2", "sub_order_to_inx", "sub_order_of_inx1_to_inx2",
                                    "subtract_number_to_string", "subtract_middle_character",
                                    "insert_number", "add_letter_if_needed", "insert_letter",  "split_string",
                                    "string_concatenate", "count_substring", "find_string", "remove_substring", "duplicate_first_letter", "duplicate_last_letter", "duplicate_mid_letter", 
                                    "swap_first_last", "swap_rand", "map_string",
                                    "get_first_character_ordinality", "get_last_character_ordinality", "get_mid_character_ordinality",
                                    "replace_substring",
                                    "shift_last_letter_rand", 
                                    "shift_first_letter_rand", 
                                    "shift_last_letter_predecessor_rand", 
                                    "shift_first_letter_predecessor_rand"]
            else:
                # functions included in as composed
                base_func_names = ["convert_to_lowercase",  "convert_to_uppercase", "capitalize_string", "reverse_string", "reverse_string_first_half", "reverse_string_last_half",
                                   "extract_digits", "remove_digits",  "remove_digits", "extract_uppers",
                                    "remove_whitespace", "get_string_length", "get_digit_indexes", "get_alpha_indexes",
                                    # "get_first_character", "get_last_character", 
                                    "remove_duplicates", "reverse_words", "count_vowels", 
                                    "replace_vowels_with_character", "replace_vowels_with_first", "replace_vowels_with_last", "replace_vowels_with_mid", "replace_vowels_with_ind_of_count",
                                    "reverse_vowels", "capitalize_alternating_letters",
                                    "count_consonants", "count_uppercase", "count_lowercase", "count_character_repetitions",
                                    "string_strip", "string_lstrip", "string_rstrip",
                                    "add_number_to_string", "advance_by_character_order", "substract_by_character_order",
                                    "add_len_to_string", "add_number_to_middle", "add_len_to_middle",
                                    "add_order_to_inx", "add_order_of_inx1_to_inx2", "sub_order_to_inx", "sub_order_of_inx1_to_inx2",
                                    "subtract_number_to_string", "subtract_middle_character",
                                    "insert_number", "add_letter_if_needed", "insert_letter",  "split_string",
                                    "string_concatenate",  "count_substring", "find_string", "remove_substring",  "duplicate_first_letter", "duplicate_last_letter", "duplicate_mid_letter",  
                                    "swap_first_last", "swap_rand",
                                    "get_first_character_ordinality", "get_last_character_ordinality", "get_mid_character_ordinality",
                                    "replace_substring", 
                                    "shift_last_letter_rand", 
                                    "shift_first_letter_rand", 
                                    "shift_last_letter_predecessor_rand", 
                                    "shift_first_letter_predecessor_rand"]
        
        func_name = np.random.choice(base_func_names)
        func = func_dict[func_name]


        if func_name in ["add_number_to_string", "subtract_number_to_string", "insert_number", "add_number_to_middle", "subtract_middle_character", "advance_by_character_order", "substract_by_character_order"]:
            number = random.randint(1, 9)
            return lambda string: func(string, number), (number), func_name
        
        elif func_name in ["add_letter_if_needed", "insert_letter", "count_character_repetitions"]:
            letter = random.choice(str.ascii_letters)
            return lambda string: func(string, letter), (letter), func_name
        
        elif func_name in ["split_string"]:
            character = random.choice(str.ascii_letters)
            return lambda string: func(string, character), (character), func_name

        elif func_name in ["string_concatenate"]:
            substring_len = random.randint(1, 5)
            substring = generate_random_string(substring_len)
            return lambda string: func(string, substring), (substring), func_name

        elif func_name in ["count_substring", "find_string", "remove_substring", "starts_with_substring", "ends_with_substring","replace_vowels_with_character"]:
            # substring_len = random.randint(1, 5)
            substring_len = random.randint(1, 1)
            substring = generate_random_string(substring_len)
            return lambda string: func(string, substring), (substring), func_name

        elif func_name in ["replace_substring"]:
            # substring_len = random.randint(1, 5)
            substring_len = random.randint(1, 1)
            while 1:
                old = generate_random_string(substring_len)
                new = generate_random_string(substring_len)
                if old!=new:
                    break
            return lambda string: func(string, old, new), (old, new), func_name

        elif func_name in ["swap_rand","add_order_of_inx1_to_inx2","sub_order_of_inx1_to_inx2"]:
            while 1:
                inx1 = random.randint(0, 9)
                inx2 = random.randint(0, 9)
                if inx1!=inx2:
                    break
            return lambda string: func(string, inx1, inx2), (inx1, inx2), func_name

        elif func_name in ["map_string"]:        
            characters = "abcdefghijklmnopqrstuvwxyz"
            shuffled_characters = list(characters)
            random.shuffle(shuffled_characters)
            mapping_dict = {}
            for i in range(len(characters)):
                mapping_dict[characters[i]] = shuffled_characters[i]
            return lambda string: func(string, mapping_dict), (mapping_dict), func_name


        elif func_name in ["shift_last_letter_rand", "shift_first_letter_rand", "shift_last_letter_predecessor_rand", "shift_first_letter_predecessor_rand"]:
            rand = random.randint(0, 25)
            return lambda string: func(string, rand), (rand), func_name

        else:
            return lambda string: func(string), (), func_name
    


def sample_compose(compound_func_names=None, single_func_names1=None, single_func_names2=None):
    func_dict = {"compose_1input_1input": compose_1input_1input, "compose_1input_2input": compose_1input_2input, "compose_1input_3input": compose_1input_3input,
                "compose_2input_1input": compose_2input_1input, "compose_2input_2input": compose_2input_2input, "compose_2input_3input": compose_2input_3input,
                "compose_3input_1input": compose_3input_1input, "compose_3input_2input": compose_3input_2input, "compose_3input_3input": compose_3input_3input}
    
    func2_avoid_dict = {"convert_to_lowercase":["convert_to_lowercase","convert_to_uppercase", "extract_uppers", "count_uppercase"],
                        "convert_to_uppercase":["convert_to_uppercase","convert_to_lowercase", "count_lowercase"], 
                        "capitalize_string":["capitalize_string"], 
                        "reverse_string":["reverse_string"], 
                        "reverse_string_first_half":["reverse_string_first_half"], 
                        "reverse_string_last_half":["reverse_string_last_half"],
                        "extract_digits":["extract_digits","get_alpha_indexes", "get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes",
                                            "count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip",
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","count_character_repetitions"], 
                        "remove_digits":["remove_digits","get_digit_indexes","extract_digits"],  
                        "extract_uppers":["extract_uppers","count_lowercase"],
                        "remove_whitespace":["remove_whitespace","string_strip","string_lstrip","string_rstrip"], 
                        "get_string_length":["get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes",
                                             "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                             "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip",
                                             "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                             "find_string","map_string","count_substring","count_character_repetitions"], 
                        "get_digit_indexes":["get_digit_indexes","get_string_length","convert_to_lowercase","extract_digits","remove_digits",
                                             "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                             "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip",
                                             "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                             "find_string","map_string","count_substring","count_character_repetitions"], 
                        "get_alpha_indexes":["extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes",
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","count_character_repetitions"],
                        "get_first_character":["get_first_character","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes",
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","split_string","remove_substring","count_character_repetitions"], 
                        "get_last_character":["get_last_character","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes",
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","split_string","remove_substring","count_character_repetitions"], 
                        "get_mid_character":["get_mid_character","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes",
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","split_string","remove_substring","count_character_repetitions"], 
                        "remove_duplicates":["remove_duplicates"], 
                        "reverse_words":["reverse_words"], 
                        "count_vowels":["replace_vowels_with_character","extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes"
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","count_character_repetitions"], 
                        "replace_vowels_with_character":["replace_vowels_with_character","replace_vowels_with_first","replace_vowels_with_last","replace_vowels_with_mid","replace_vowels_with_ind_of_count","reverse_vowels","count_vowels"], 
                        "replace_vowels_with_first":["replace_vowels_with_character","replace_vowels_with_first","replace_vowels_with_last","replace_vowels_with_mid","replace_vowels_with_ind_of_count","reverse_vowels","count_vowels"], 
                        "replace_vowels_with_last":["replace_vowels_with_character","replace_vowels_with_first","replace_vowels_with_last","replace_vowels_with_mid","replace_vowels_with_ind_of_count","reverse_vowels","count_vowels"], 
                        "replace_vowels_with_mid":["replace_vowels_with_character","replace_vowels_with_first","replace_vowels_with_last","replace_vowels_with_mid","replace_vowels_with_ind_of_count","reverse_vowels","count_vowels"], 
                        "replace_vowels_with_ind_of_count":["replace_vowels_with_character","replace_vowels_with_first","replace_vowels_with_last","replace_vowels_with_mid","replace_vowels_with_ind_of_count","reverse_vowels","count_vowels"], 
                        "reverse_vowels":["reverse_vowels"], 
                        "capitalize_alternating_letters":["capitalize_alternating_letters"],
                        "count_consonants":["replace_vowels_with_character","extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes"
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","count_character_repetitions"], 
                        "count_uppercase":["replace_vowels_with_character","extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes"
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","count_character_repetitions"], 
                        "count_lowercase":["replace_vowels_with_character","extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes"
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring","count_character_repetitions"], 
                        "count_character_repetitions":["count_character_repetitions","replace_vowels_with_character","extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes"
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_substring"],
                        "string_strip":["remove_whitespace","string_strip","string_lstrip","string_rstrip"], 
                        "string_lstrip":["remove_whitespace","string_strip","string_lstrip","string_rstrip"], 
                        "string_rstrip":["remove_whitespace","string_strip","string_lstrip","string_rstrip"], 
                        "add_number_to_string":["add_number_to_string"], 
                        "advance_by_character_order":["advance_by_character_order"], 
                        "substract_by_character_order":["substract_by_character_order"],
                        "add_len_to_string":["add_len_to_string"], 
                        "add_number_to_middle":["add_number_to_middle"], 
                        "add_len_to_middle":["add_len_to_middle"],
                        "add_order_to_inx":["add_order_to_inx"], 
                        "add_order_of_inx1_to_inx2":["add_order_of_inx1_to_inx2"], 
                        "sub_order_to_inx":["sub_order_to_inx"], 
                        "sub_order_of_inx1_to_inx2":["sub_order_of_inx1_to_inx2"],
                        "subtract_number_to_string":["subtract_number_to_string"], 
                        "subtract_middle_character":["subtract_middle_character"],
                        "insert_number":["insert_number"], 
                        "add_letter_if_needed":["add_letter_if_needed"], 
                        "insert_letter":["insert_letter"],  
                        "split_string":["split_string"],
                        "string_concatenate":["string_concatenate"], 
                        "count_substring":["count_substring","replace_vowels_with_character","extract_digits","get_string_length","convert_to_lowercase","extract_digits","remove_digits","get_digit_indexes"
                                            "get_alpha_indexes","count_vowels","replace_vowels_with_ind_of_count",
                                            "count_consonants","count_uppercase","count_lowercase","string_strip","string_lstrip","string_rstrip"
                                            "add_order_to_inx","add_order_of_inx1_to_inx2","sub_order_to_inx","sub_order_of_inx1_to_inx2",
                                            "find_string","map_string","count_character_repetitions"], 
                        "find_string":["find_string"], 
                        "remove_substring":["remove_substring"], 
                        "duplicate_first_letter":["duplicate_first_letter"], 
                        "duplicate_last_letter":["duplicate_last_letter"], 
                        "duplicate_mid_letter":["duplicate_mid_letter"], 
                        "swap_first_last":["swap_first_last"], 
                        "swap_rand":["swap_rand"], 
                        "map_string":["map_string"],
                        "get_first_character_ordinality":["get_first_character_ordinality"], 
                        "get_last_character_ordinality":["get_last_character_ordinality"], 
                        "get_mid_character_ordinality":["get_mid_character_ordinality"],
                        "replace_substring":["replace_substring"],
                        "shift_last_letter_rand":["shift_last_letter_rand"], 
                        "shift_first_letter_rand":["shift_first_letter_rand"], 
                        "shift_last_letter_predecessor_rand":["shift_last_letter_predecessor_rand"], 
                        "shift_first_letter_predecessor_rand":["shift_first_letter_predecessor_rand"]
                        }

    func_name = np.random.choice(compound_func_names)
    func = func_dict[func_name]
    
    if func_name == 'compose_1input_1input':
        func1, params1, name1 = sample_single_f(base_func_names=single_func_names1)

        while 1:
            func2, params2, name2 = sample_single_f(base_func_names=single_func_names2, not_composed=False)
            if not(name2 in func2_avoid_dict[name1]):
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
    
   
def sample_fun(args, is_composed=None):
    # pdb.set_trace()
    if is_composed is None:
        if (random.random() < args.ratio):
            f, params, f_name = sample_single_f(num_input=1)
        else:
            f, params, f_name = sample_compose(compound_func_names=["compose_1input_1input"])
    else:
        if not(is_composed):
            f, params, f_name = sample_single_f(num_input=1)
        else:
            f, params, f_name = sample_compose(compound_func_names=["compose_1input_1input"])
    return f, params, f_name


def sample(args):

    file_path = "%s/check_list.json"%args.dir
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            current_funs = json.load(file)
    else:
        current_funs = []
    
    ## sample a new function
    
    if random.random() > args.ratio:
    # if 'compose' in f_name:
        while 1:
            f, params, f_name = sample_fun(args,is_composed=True)
            # assert len(params)==2
            fun1_exist = check_exist(params[0], f_name, current_funs)
            fun2_exist = check_exist(params[1], f_name, current_funs)
            if not (fun1_exist and fun2_exist):
                break
    else:
        while 1:    
            f, params, f_name = sample_fun(args,is_composed=False)
            fun_exist = check_exist(params, f_name, current_funs)
            if not fun_exist:
                break
    
    current_funs.append((f_name, params))
    with open(file_path, "w") as file:
        json.dump(current_funs, file, indent=3)

    return f, params, f_name


    
if __name__ == '__main__':
    for i in range(10):
        f, f_name = sample()
        print(f_name)
