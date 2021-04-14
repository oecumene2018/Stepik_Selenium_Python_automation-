# Stepik webstore tests
For installing dependencies after cloning project you need to run code
```shell
pip install -r requirements.txt
```
Use PyTest for running tests, for example:
```shell
pytest test_items.py
```

Tests could be run with two options
- browser_name
- language

## browser_name option
`--browser_name=chrome` <br>
Valid value - `chrome` of `firefox`<br>
By default used value 'chrome'

## language option
`--language=es`<br>
By default used value `ru`


## Running Examples
```shell
# for running all test functions in all files
pytest 
```

```shell
# for running all test functions in file test_items.py
pytest test_items.py
```

```shell
# for running all test functions in all files in FireFox browser
pytest --browser_name=firefox
```

```shell
# for running all test functions in file test_items.py with 'fr' language
pytest --language=fr test_items.py
```

```shell
# for runing all test functions in file test_items with 'es' language in chrome browser
pytest --browser_name=chrome --language=es test_items.py
```
