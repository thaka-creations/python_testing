# Python testing
[ Refer to link for documentation ](https://realpython.com/python-testing/)

## Linting
- Look at your code and comment on it.
- Tips on mistakes you've made, correct trailing spaces and even predict bugs that 
you may have introducted
```
pip install flake8
flake8 test.py
```
- Flake8 is configurable on the command line or inside configuration file in your project.
- Flake8 will inspect .flake8 file in the project folder or a setup.cfg file.
- If you decided to use Tox, you can put the flake8 configuration section inside tox.ini.

```
[flake8]
ignore = E305
exclude = .git,__pycache__
max-line-length = 90
```

- Alternative, can provide this options on the command line:
```
$ flake8 --ignore E305 --exclude .git,__pycache__ --max-line-length=90
```

```
yaml
matrix:
  include:
    - python: "2.7"
      script: "flake8"
```

## Aggressive Linting with Code Formatter
* Flake8 is a passive linter: recommends changes, but you have to go and change code
* More aggressive approach is a code formatter
+ Code formatter will change your code automatically to meet a collection of style and layout practice

```angular2html
pip install black
black test.py
```

## Testing for performance degradation between changes
- Standard library provides timeit module, which can time functions a number of times and give you the distribution.



