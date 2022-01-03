# version 1.4.5
# MIT License
# Copyright (c) 2021 Kshitij

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Extracting keys and values out of txt file and convert it into dic"""
from json_txt.MainFiles import extract_keys, extract_values


def extract_data(data):
    """create a dictonary"""

    from json_txt.MainFiles import extract_keys, extract_values
    keys = extract_keys(data)
    values = extract_values(data)
    return {keys[index]: values[index] for index in range(len(keys))}


def load_txt(data):
    """compiling the text file"""

    try:
        from json_txt.compiler import compiles
        return list(compiles(data))
    except FileNotFoundError:
        pass


def edit_data(filename, key, value):
    from filemod import writer, reader
    from json_txt.SupportFuncs import number_detect
    if number_detect(value) == False:
        value = '"'+value+'"'
    data = reader(filename)
    keys = extract_keys(list(data))
    values = extract_values(list(data))
    print("keys ", keys)
    print(values)
    temp = keys.index(key)
    values.pop(temp)
    values.insert(temp, value)
    writing_file = '{ \n'
    for size in range(len(keys)):
        writing_file = writing_file+str(keys[size])+":"+str(values[size])+"\n"
    writing_file = writing_file+"\n"+"}"
    writer(filename, writing_file, "w")
    return True


def add_data(filename, newkeys, newvalues):
    """append data into txt file"""
    from filemod import reader, writer
    from json_txt.SupportFuncs import number_detect
    if number_detect(newvalues) == False:
        newvalues = '"'+newvalues+'"'
    data = reader(filename)
    keys = extract_keys(data)
    values = extract_values(data)
    keys.append(newkeys)
    values.append(newvalues)
    write_file = "{ \n"
    for size in range(len(keys)):
        write_file = write_file+str(keys[size])+":"+str(values[size])+"\n"
    write_file = write_file+"\n"+"}"
    writer(filename, write_file, "w")
    return True
