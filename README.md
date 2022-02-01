## json txt

With the help of json txt you can use your txt file as a json file in a very simple way

## Dependencies 
- re
- filemod `pip install filemod` 
- colored `pip install colored`

### Installation and Usage

1. use `pip install json_txt`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Import the package: ``import json_txt``

# Updates

- you no longer need to use brackets to write values in.
- some bugs are been solved and optimizations are made the library
- now "=" sign can be use in place of ":" is all your choise

### Functions in the module 

- First load the data of the file using load_txt method you need to load 
data every time you make changes to it as it is using txt as its main source
`json_txt.load_txt(filename)`

- extract_keys method helps you extract all the keys from the txt file , and returns them all in the list
`json_txt.extract_keys(data).`

- extract_values method helps you extract all the values from the specific keys in sequence from the txt file , and returns them in the list.
`json_txt.extract_keys(data).`

- extract_data method helps you extract all the key value pairs from the txt file to dict
`json_txt.extract_data(filename)`

- edit_data method helps you edit key's value pair , it takes filename ,key, and a value to change.
`jason_txt.edit_data(filename,key,value_to_change)` 

- Helps you detect weather the var is int or not returs bool
`json_txt.number_detect(letter)`

- Helps you convert text array to the real array
eg - 
"[23,23,353]"-> [23,23,353]. 
`json_txt.generate_array(data)`




## Run Locally

Clone the project

```bash
  git clone https://github.com/kshitij1235/Json_txt/tree/main/dist
```

Install

```bash
  pip install json_txt
```

## List of Functions

| functions | processs| args|
| ----------|---------|-----|
|load_txt|loads the txt data|filename|
|extract_keys|extract key from data|data|
|extract_values|extract values from data|data|
|extract_data|Extracts key value pair|filename|
|edit_data|Edit certain key values|filename,key,value_to_change|
|add_data|Help add data to the txt| filename,new key , new value|
|generate_array|converts string array to real array |data *(portion of the aray in string)*|

## Usage/Examples

### way to write your txt

```txt

settings: active
values:244
meta:[23,52,53,work]
unit_test=True


Rules : 
1) Dont make any sub tree to write your data do it under one tree/{}.
2)dont use ] or [ inside arrays.
4)strictly use : or = when assigning values.
```

### code

```python
import json_txt

###printing basic dictornary 
file=json_txt.load_txt("main.txt") #load the txt file
print(json_txt.extract_data(file)) #printing key value pairs


####extracting keys and values separately
print(json_txt.extract_keys(file)) #printing the updated key values
print(json_txt.extract_values(file)) #printing the updated values values

```


### Output

```javascript
{'settings': 'active', 'values': 244, 'meta': [23, 52, 53, 'work'],'unit_test':True}
['settings', 'values', 'meta','unit_test']
['active', 244, [23, 52, 53, 'work'],True]
```

## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/kshitij1235/Json_txt/blob/main/LICENSE)



  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)
- [website](https://sites.google.com/view/jsontxt)

  
