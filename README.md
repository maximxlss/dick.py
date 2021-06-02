# LongDick interpreter

An [esolang](https://esolangs.org/wiki/LongDick) interpreter written in python.
## Installing
- Python >= 3.5
- `pip install -r requirements.txt`

## Usage
- `main.py [-h] [-g GRAMMAR_FILE] [-l] source`
- See `main.py -h` for help

## Features
- Working interpreter
- Support for custom grammar (russian translation included!)
- Compatable with Dick

### Custom grammar
- You can create custom grammar files. See existing `grammar.py` and `russian_grammar.py`, [lark documentation](https://lark-parser.readthedocs.io/en/latest/grammar.html)

## Example: Factorial
```
DICK schlong 8============D

DICK resulting_cock 8=D
COCK GO FAST IF schlong IS BIGGER THAN 8=D!
    GRAB resulting_cock
    HUGEDICK schlong
    RELEASE resulting_cock
    GRAB schlong
    SMALLDICK 8=D
    RELEASE schlong
ALRIGHT, STOP COCKING AROUND

GRAB resulting_cock
PEE
```

## Some background
I wanted to try creating a simple interpreter and stumbled across this esoteric gem. First version made in literally one evening. Code is not very good. As everything here.
