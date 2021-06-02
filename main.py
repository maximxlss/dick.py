import argh
from argh import arg
from interpreter import Interpreter
from lark import Lark
import importlib

def main(source: "Path to the source code file to execute", grammar_file: "Custom grammar file without .py"="grammar", legacy_vars: "Disable LongDick varible name restrictions"=False):
    with open(source) as f:
        grammar_file = importlib.import_module(grammar_file)
        i = Interpreter(grammar_file.required_words_in_varnames, legacy_vars)
        parser = Lark(grammar_file.grammar)
        for expr in parser.parse(f.read()).children:
            i.run(expr)

argh.dispatch_command(main)

