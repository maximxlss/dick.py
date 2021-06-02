import argh
from argh import arg
from interpreter import Interpreter
from grammar import grammar, required_words_in_varnames
from lark import Lark

def main(source: "Path to the source code file to execute", legacy_vars: "Disable LongDick varible name restrictions"=False):
    with open(source) as f:
        i = Interpreter(required_words_in_varnames, legacy_vars)
        parser = Lark(grammar)
        for expr in parser.parse(f.read()).children:
            i.run(expr)

argh.dispatch_command(main)

