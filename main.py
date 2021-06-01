import argh
from argh import arg
from interpreter import Interpreter
from grammar import grammar, required_words_in_varnames
from lark import Lark

@arg('source', help='Path to the source code file to execute')
def main(source: str):
    with open(source) as f:
        i = Interpreter(required_words_in_varnames)
        parser = Lark(grammar)
        for expr in parser.parse(f.read()).children:
            i.run(expr)

argh.dispatch_command(main)

