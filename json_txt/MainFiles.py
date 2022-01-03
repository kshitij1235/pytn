# json_txt/MainFile.py - version 1.4.5

from json_txt.SupportFuncs import collab_words_in_list, allot_values


def extract_keys(txt_file_data):
    """
    extract keys from file
    1)this takes list or some times even file works. 
    2)finds for each specific line where '\n' is present(this means new line)
    3)and append every thing before ':' and append it in a list
    """

    characters = list(txt_file_data)
    temp = []
    keys = []
    for index in range(len(characters)):
        if characters[index] == "\n":
            for value_index in range(index, len(characters)):
                if characters[value_index] == ":":
                    keys.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                elif characters[value_index] not in [":", "\n", " ","}","{"]:
                    temp.append(characters[value_index])
    return keys


def extract_values(txt_file_data):
    """extract values from file"""

    temp = []
    values = []
    for index in range(len(txt_file_data)):
        if txt_file_data[index] == ":":
            for index in range(index, len(txt_file_data)):
                if txt_file_data[index] == "\n":
                    values.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                elif txt_file_data[index] not in [":", "'", " ", '"',"}"]:
                    temp.append(txt_file_data[index])
    values=allot_values(values)
    return values
