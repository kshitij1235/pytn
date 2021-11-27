# json_txt/SupportFuncs.py - version 1.4.4


def number_detect(letter):
    """Detect the nature of letter is number or not"""

    try:
        int(letter)
        return True
    except:
        return False

def number_string(data):
    """Detect the nature of letter is number or not"""
    try:
        return int(data)
    except:
        return str(data)


def generate_array(data):
    """generate string arrays to real arrays"""
    array_temp = []
    array = []
    for array_elements in data:
        if array_elements in ["["]:
            continue
        elif array_elements in [",", "]"]:
            if number_detect(collab_words_in_list(array_temp)):
                array.append(int(collab_words_in_list(array_temp)))
            else:
                array.append(collab_words_in_list(array_temp))
            array_temp.clear()
        else:
            array_temp.append(array_elements)
    return array


def collab_words_in_list(list):
    """collab word into strings"""
    return ''.join(list)


def allot_values(temp, values):
    if temp[0] == "[":
        values.append(list(generate_array(temp)))
    elif collab_words_in_list(temp)=="True":
        values.append(True)
    elif collab_words_in_list(temp)=="False":
        values.append(False)
    else:
        values.append(number_string(collab_words_in_list(temp)))
    temp.clear()
    return values
