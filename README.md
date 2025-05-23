# AnyUnit - Universal unit converter

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple and convenient library for converting physical units.

## Installation
```bash
pip install anyunit
```

## Examples
Convert length
```python
from anyunit import convert_length

result = convert_length(1, "kilometer", "meter")
print(result) # 1000.0
```

Convert weight
```python
from anyunit import convert_weight

result = convert_weight(1, "kilogram", "gram")
print(result) # 1000.0
```

Convert area
```python
from anyunit import convert_area

result = convert_area(1, "kilometer", "mile")
print(result) # 0.38610215859253505
```