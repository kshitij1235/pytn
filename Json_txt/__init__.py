
import filemod
import re



def number_detect(letter):
    try:
        int(letter)
        return True
    except:return False

def extract_data(filename):
    try:file = filemod.reader(filename)
    except:print("File Dont Exist")
    
    filtured_data = []
    joining_letters = ''
 
    word = []
    temp = re.findall(r'\d+', file)
    values= list(map(int, temp))
    print(values)

    final_dictonary= {}

    for letters in file:
        if letters == '\n' or letters == ' ' or letters == "{" or letters == "}":
            continue
        elif number_detect(letters):
            continue
        else:
            filtured_data.append(letters)

    for letters in filtured_data:
        if letters == ':':
            word.append(joining_letters)
            joining_letters = ''
            continue
        else:
            joining_letters = joining_letters+str(letters)
    
    try:
        for index in range(len(word)):
            final_dictonary[word[index]] = values[index]
    except:
        if len(word) > len(values):
            print("value not assigned to ", word[letters], "properly")
        else:print("Unknown ERROR")
    return final_dictonary

