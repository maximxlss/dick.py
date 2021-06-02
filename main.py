import argh
from interpreter import Interpreter
from transformer import Transformer
from transpiler import Transpiler
from lark import Lark
import os
import importlib

def main(source: "Path to the source code file to execute",
         grammar_file: "Custom grammar file without .py"="grammar",
         legacy_vars: "Disable LongDick varible name restrictions"=False,
         transpile: "Transpile source into Rust instead of interpreting"=False,
         build: "Automatically compile emitted Rust code with system-wide rustc. Also tries to format the code with rustfmt"=False,
         run: "Build and run"=False,
         hash_map: "Use HashMap in transpiling. Allows to use hand as a variable name but probaly slows things down. Known bug: allows to release into not assigned variables"=False):
    with open(source, encoding="UTF-8") as f:
        src = f.read()
    grammar_file = importlib.import_module(grammar_file)
    t = Transformer(grammar_file.required_words_in_varnames, legacy_vars)
    parser = Lark(grammar_file.grammar, parser="lalr", transformer=t, propagate_positions=True)
    src = "\n" + src + "\n" # to make grammar rules properly ignore spaces in the beginning and the end
    ast = parser.parse(src)
    if transpile or build or run:
        rust_code = transpile_cmd(ast, hash_map)
        if build or run:
            with open(os.path.splitext(source)[0] + ".rs", "w+", encoding="UTF-8") as f:
                f.write(rust_code)
            os.system("rustfmt " + os.path.splitext(source)[0] + ".rs")
            os.system(f"rustc -C debuginfo=0 -C opt-level=3 --out-dir {os.path.dirname(source)} {os.path.splitext(source)[0]}.rs")
            if run:
                if os.name == "nt":
                    os.system(os.path.splitext(source)[0] + ".exe")
                else:
                    os.system(os.path.splitext(source)[0])
        else:
            print(rust_code)
    else:
        interpret_cmd(ast)

def interpret_cmd(source) -> None:
    i = Interpreter()
    i.visit(source)

def transpile_cmd(source, hash_map: bool) -> str:
    t2 = Transpiler(hash_map)
    return t2.transform(source)

argh.dispatch_command(main)

