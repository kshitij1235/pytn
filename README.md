## json txt

With the help of json txt you can use your txt file as a json file in a very simple way

## Dependencies 
- re
- filemod `pip install filemod` 

### Installation and Usage

1. use `pip install json_txt`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Select the correct package for your environment:
4. Import the package: ``import json_txt``

### Functions in the module 

1)First load the data of the file using load_txt method you need to load 
data every time you make changes to it as it is using txt as its main source
`json_txt.load_txt(filename)`

2)extract_keys method helps you extract all the keys from the txt file , and returns them all in the list
`json_txt.extract_keys(data).`

3)extract_values method helps you extract all the values from the specific keys in sequence from the txt file , and returns them in the list.
`json_txt.extract_keys(data).`

4)extract_data method helps you extract all the key value pairs from the txt file to dict
`json_txt.extract_data(filename)`

5)edit_data method helps you edit key's value pair , it takes filename ,key, and a value to change.
`jason_txt.edit_data(filename,key,value_to_change)` 

6)Helps you detect weather the var is int or not returs bool
`json_txt.number_detect(letter)`




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

## Usage/Examples

### way to write your txt

```txt
{ 
settings:3
x:4
truck:32
}

Rules : 
1) Dont make any sub tree to write your data do it under one tree/{}
2) Dont put dummy values as it wont consider
3) Dont use any numericals in variable name
4)strictly use : when assigning values
```

### code

```python
import json_txt

###printing basic dictornary 
file=json_txt.load_txt("main.txt") #load the txt file
print(json_txt.extract_data(file)) #printing key value pairs

#####editing data 
json_txt.edit_data("main.txt","settings",33) #changing value of settings
file=json_txt.load_txt("main.txt")   #again laoding the updated copy
print(json_txt.extract_data(file)) #printing the updated key values

####extracting keys and values separately
print(json_txt.extract_keys(file)) #printing the updated key values
print(json_txt.extract_values(file)) #printing the updated values values

```


### Output

```javascript
{'settings': 3, 'x': 4, 'truck': 32}
{'settings': 33, 'x': 4, 'truck': 32}
['settings', 'x', 'truck']
[33, 4, 32]
```

## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/kshitij1235/Json_txt/blob/main/LICENSE)

  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)

  
