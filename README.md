## pytn

With the help of pytn you can use your txt file as a json file in a very simple way

pytn stands for - python text notation

## Dependencies 

- filemod `pip install filemod` 

### Installation and Usage

1. use `pip install pytn`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Import the package: ``import pytn``

# Updates

- Improved speed 
- String is better and can recognized spaces between text better
- major bugs solved
- now you can remove keys and values 

### Functions in the module 

- First load the data of the file using load_txt method you need to load 
data every time you make changes to it as it is using txt as its main source
`load_txt(filename)`

- extract_keys method helps you extract all the keys from the txt file , and returns them all in the list
`extract_keys(data).`

- extract_values method helps you extract all the values from the specific keys in sequence from the txt file , and returns them in the list.
`extract_keys(data).`

- extract_data method helps you extract all the key value pairs from the txt file to dict
`extract_data(filename)`

- edit_data method helps you edit key's value pair , it takes filename ,key, and a value to change.
`edit_data(filename,key,value_to_change)` 

- remove_data method helps you remove keys and values pair 
`remove_value(filename,key)` 




## Run Locally

Clone the project

```bash
  git clone https://github.com/kshitij1235/pytn/tree/main/dist
```

Install

```bash
  pip install pytn
```

## List of Functions

| functions | processs| args|
| ----------|---------|-----|
|load_txt|loads the txt data|filename|
|extract_keys|extract key from data|filename|
|extract_values|extract values from data|filename|
|extract_data|Extracts key value pair|filename|
|edit_data|Edit certain key values|filename,key,value_to_change|
|add_data|Help add data to the txt| filename,new key , new value|
|remove_data|remove key value pair|filename,key|

## Usage/Examples

### way to write your txt

```txt
{
settings: active is on
values:244
meta:[23,52,53,work]
unit_test=True
}

Rules : 
1) Dont make any sub tree to write your data do it under one tree/{}.
2)dont use ] or [ inside arrays.
4)strictly use : or = when assigning values.
```

### code

```python
from pytn import *

###printing basic dictornary 
file="main.txt"
print(extract_data(file)) #printing key value pairs


####extracting keys and values separately
print(extract_keys(file)) #printing the updated key values
print(extract_values(file)) #printing the updated values values

```


### Output

```javascript

{'settings': 'active is on', 'values': 244, 'meta': [23, 52, 53, 'work'],'unit_test':True}
['settings', 'values', 'meta','unit_test']
['active is on', 244, [23, 52, 53, 'work'],True]
```

## Badges


[![GNU License]([https://img.shields.io/apm/l/atomic-design-ui.svg?](https://img.shields.io/badge/License-GNU%20Affero%20General%20Public%20License-orange))](https://github.com/kshitij1235/pytn/blob/main/LICENSE)



  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)
- [website](https://sites.google.com/view/pytn)

  
