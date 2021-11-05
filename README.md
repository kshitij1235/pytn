## json txt

With the help of json txt you can use your txt file as a json file in a very simple way

### Installation and Usage

1. use `pip install json_txt`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Select the correct package for your environment:
4. Import the package: ``import json_txt``

### Functions in the module 

1) extract_data method helps you extract all the key value pairs from the txt file to dict
`json_txt.extract_data(filename)`

2) Helps you detect weather the var is int or not returs bool
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

| functions            | processs| args|
| ----------------- | ---|----------|
| extract_data(filename)|Extracts key value pair| filename|    



## Usage/Examples

### way to write your txt

```javascript
{
    sence:3
    height:5
    marks:23
}

//dont make any sub tree to write your data do it under one tree/{}
```

### code

```javascript
import json_txt

json_txt.extract_data('demo_file.txt')
```


### Output

```javascript
{'sence': 3, 'height': 5, 'marks': 23}
```

## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/kshitij1235/Json_txt/blob/main/LICENSE)

  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)

  
