# AnyUnit - Universal unit converter

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple and convenient library for converting physical units.

## Installation
```bash
pip install anyunit
```

## Quick start
```python
from anyunit import convert_length, convert_weight

print(convert_length(1, "mile", "kilometer"))  # 1.609344
print(convert_weight(1, "gram", "kilogram"))  # 0.001
```

## License
MIT