# LongDick interpreter

An [esolang](https://esolangs.org/wiki/LongDick) interpreter written in python.
## Installing
- Python >= 3.5
- `pip install -r requirements.txt`

## Usage
- `main.py [-h] [-g GRAMMAR_FILE] [-l] [-t] [-b] [-r] [--hash-map] source`
- `-h` - display a help message. It's less verbose than what you are reading now.
- `-g GRAMMAR_FILE` - set custom grammar module name (filename without .py). See existing `grammar.py` and `russian_grammar.py`, [lark documentation](https://lark-parser.readthedocs.io/en/latest/grammar.html)
- `-l` - Disable LongDick [varible name restrictions](./examples/name_restrictions.md)
- `-t` - Transpile into Rust instead of interpreting. See [Transpiler section](#Transpiler). By default, emits minimized code into stdout.
- `-b` - Save emitted code into .rs file with same name in the same directory and run `rustfmt SOURCE.rs` and `rustc -C debuginfo=0 -C opt-level=3 --out-dir SOURCE-DIR SOURCE.rs`.
- `-r` - Same as `-b`, but also runs built executable.
- `--hash-map` - Use a HashMap to store variables instead of native variables. Allows to use any valid variable names, including `hand`, in contrast with native variables. Probably slow. Bug: also allows to release into not assigned variables.
- See also: [examples](./examples/examples.md).

## Transpiler
Has a transpiler to Rust, which is simple and does not perform any optimizations. Though the resulting code is simple and should be finely optimized by rustc and llvm.

<sub><sup>Does this count as a compiler?</sup></sub>

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
