# Computus

A small Python library for historical chronology.

## Author

Ivan Debono



## Features

- Indiction calculation (Anno Domini and Byzantine Anno Mundi)
- Roman numeral conversion



## Installation

### Using pip

```bash
pip install computus
````

### Using uv

```bash
uv add computus
```

Or:

```bash
uv pip install computus
```



## Usage (Python)

```python id="cmd1"
from computus import indiction, arabic_to_roman

i = indiction(525)
print(i)                     # 3
print(arabic_to_roman(i))   # III
```



## Command Line Usage

After installing the package, you can run it directly from the terminal.

### Basic usage

```bash id="cmd2"
computus 525
```

Example output:

```text id="cmd3"
Indiction: 3 (III)
```



### Specify calendar system

```bash id="cmd4"
computus 525 --calendar AD
computus 1000 --calendar AM
```



### Help

```bash id="cmd5"
computus --help
```



## Description

`computus` provides simple tools for working with historical dating systems, inspired by the chronological methods of Late Antiquity and the Middle Ages. It currently supports:

* Calculation of the indiction cycle
* Conversion of integers to Roman numerals



## Roadmap

Future features will include:

* Julian ↔ Gregorian calendar conversion
* Parsing historical date formats
* Support for additional era systems



## License

PolyForm Noncommercial License 1.0.0

Copyright (c) 2026 Ivan Debono

