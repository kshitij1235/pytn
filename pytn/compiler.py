# json_txt/compiler.py - version 1.4.6

from filemod import reader


def collab_words_in_list(data_list):
    """collab word into strings"""
    return ''.join(data_list)


def test1(filename):
    data=reader(filename)
    if data is None:
        print('x Test 1 Fail', 'red')
    else:
        return True

def test2(filename):
    from pytn.MainFiles import extract_values,extract_keys
    if len(extract_keys(filename)) == len(extract_values(filename)):
        return True

    print("X Test 3 Fail", 'red')
    print("Uneven values or number found in the values", 'red')
    return False

def compiles(data):
    if test1(data) == test2(data):
        return data
