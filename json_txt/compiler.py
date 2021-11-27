import json_txt


# json_txt/compiler.py - version 1.4.4

import filemod
from termcolor import colored


def collab_words_in_list(data_list):
    """collab word into strings"""
    return ''.join(data_list)


def test1(data):
    if data is None:
        print(colored('x Test 1 Fail', 'red'))
    else:
        print(colored('✓ Test 1 pass', 'green'))
        return True


def test2(data):
    if data[0:1] == "{" and data[len(data)-1] == "}":
        print(colored("✓ Test 2 pass", 'green'))
        return True
    elif data[0:1] != "{":
        print(colored('missing { ', 'red'))
        print(colored('x Test 2 Fail', 'red'))
    else:
        print(colored('x Test 2 Fail', 'red'))
        print(colored('missing } never closed', 'red'))


def test3(data):
    from json_txt.MainFiles import extract_values,extract_keys
    if len(extract_keys(data)) == len(extract_values(data)) == data.count(":"):
        print(colored("✓ Test 3 pass", 'green'))
        return True

    print(colored("X Test 3 Fail", 'red'))
    print(colored("Uneven values or number found in the values", 'red'))


def compiles(data):
    data = filemod.reader(data)
    if test1(data) == test2(data) == test3(data):
        print(colored("All Test Passed", 'green'))
    return data
