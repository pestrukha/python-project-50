### Hexlet tests and linter status:
[![Actions Status](https://github.com/pestrukha/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/pestrukha/python-project-50/actions)
[![Python CI](https://github.com/pestrukha/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/pestrukha/python-project-50/actions/workflows/pyci.yml)
### Code Climate 
[![Maintainability](https://api.codeclimate.com/v1/badges/9fe27a511695c1c8de16/maintainability)](https://codeclimate.com/github/pestrukha/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9fe27a511695c1c8de16/test_coverage)](https://codeclimate.com/github/pestrukha/python-project-50/test_coverage)
### Description
**_GENDIFF:_** this program designed to show the differences between two data structures.

+ `gendiff -h`: help message

+ `gendiff *first_file* *second_file*`: diff is a dictionary tree structure. 

+ `gendiff *first_file* *second_file* -f plain`: diff is multiline text.

+ `gendiff *first_file* *second_file* -f json`: diff is a json object.
### Requirements
| Tools  | Version |
|:------:|:-------:|
| python |  ^3.10  |
| poetry | ^1.8.2  |
| flake8 | ^6.1.0  |
| pyyaml |  ^6.0   |
| pytest | ^7.4.3  |
| pytest-cov | ^5.0.0  |
### Installation
```
pip install --user git+https://github.com/pestrukha/python-project-50
```
### Demo
#### JSON files
[![asciicast](https://asciinema.org/a/659771.svg)](https://asciinema.org/a/659771)
#### YAML files
[![asciicast](https://asciinema.org/a/661798.svg)](https://asciinema.org/a/661798)
#### Nested files
[![asciicast](https://asciinema.org/a/663237.svg)](https://asciinema.org/a/663237)
#### Plain output
[![asciicast](https://asciinema.org/a/xkAUx8YoDL6lhILILw1P4jaFS.svg)](https://asciinema.org/a/xkAUx8YoDL6lhILILw1P4jaFS)
#### JSON output
[![asciicast](https://asciinema.org/a/PBbUXYbfoSgfgENIcT66WUxyy.svg)](https://asciinema.org/a/PBbUXYbfoSgfgENIcT66WUxyy)
