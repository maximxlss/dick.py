import argh
from argh import arg
from interpreter import Interpreter
from transformer import Transformer
from lark import Lark
import importlib

def main(source: "Path to the source code file to execute", grammar_file: "Custom grammar file without .py"="grammar", legacy_vars: "Disable LongDick varible name restrictions"=False):
    with open(source, encoding="UTF-8") as f:
        grammar_file = importlib.import_module(grammar_file)
        i = Interpreter()
        t = Transformer(grammar_file.required_words_in_varnames, legacy_vars)
        parser = Lark(grammar_file.grammar, parser="lalr", transformer=t, propagate_positions=True)
        i.visit(parser.parse(f.read()))

argh.dispatch_command(main)

