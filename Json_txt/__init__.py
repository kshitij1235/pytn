import filemod
import re

def load_txt(filename):
    """loads the latest copy of the txt"""
    return filemod.reader(filename)

def number_detect(letter):
    """Detect the nature of letter is 
    number or not"""
    try:
        int(letter)
        return True
    except:
        return False

def extract_values(data):
    """extract the value from txt"""
    temp = re.findall(r'\d+', data)
    return list(map(int, temp))


def extract_keys(data):
    """extract keys from txt"""
    filtured_data = []
    joining_letters = ''
    word = []
    for letters in data:
        if number_detect(letters):
            continue
        elif letters not in ['\n', ' ', "{", "}"]:
            filtured_data.append(letters)

    for letters in filtured_data:
        if letters == ':':
            word.append(joining_letters)
            joining_letters = ''
            continue
        else:
            joining_letters += str(letters)
    return word


def extract_data(filename):
    """return a dict of key values from the
    txt"""

    try:
        file = filemod.reader(filename)
    except FileNotFoundError as e:print(e)

    word = extract_keys(filename)
    values = extract_values(filename)

    final_dictonary = {}

    try:
        for index in range(len(word)):
            final_dictonary[word[index]] = values[index]
    except ValueError:
        if len(word) > len(values) or len(word)<len(values):
            print("value not assigned to properly")
        else:
            print("Unknown ERROR")
    return final_dictonary


def edit_data(filename,key, value_to_change):

    """change the data for the txt"""
    file=filemod.reader(filename)
    key_=extract_keys(file)
    values_=extract_values(file)
    for i in range(len(key_)):
        if key == key_[i]:
            values_.pop(i)
            values_.insert(i,value_to_change)
    data=''
    data="{ \n"
    for i in range(len(key_)):
        data=data+str(key_[i])+":"+str(values_[i])+"\n"
    data += "}"
    filemod.writer(filename,data,"w")
