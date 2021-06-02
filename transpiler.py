from lark import Tree, visitors, Token

class Transpiler(visitors.Transformer):
    def __init__(self, hash_map):
        self.hash_map = hash_map

    def start(self, expr):
        if self.hash_map:
            return "#![allow(unused_assignments, unused_mut)]use std::collections::HashMap;fn main(){let mut hand: i64 = 0;let mut vars: HashMap<&str, i64> = HashMap::new();" + "".join(expr) + "}"
        else:
            return "#![allow(unused_assignments, unused_mut)]fn main(){let mut hand: i64 = 0;" + "".join(expr) + "}"

    def value(self, expr):
        return expr[0]

    def dick(self, expr):
        return expr[0]

    def varname(self, expr):
        if self.hash_map:
            return f'*vars.entry("{expr[0]}").or_insert(0)'
        else:
            return expr[0]

    def setdick(self, expr):
        if self.hash_map:
            return f'{expr[0]} = {expr[1]};'
        else:
            return f'let mut {expr[0]}: i64 = {expr[1]};'

    def grab(self, expr):
        return f"hand = {expr[0]};"

    def release(self, expr):
        return f"{expr[0]} = hand;hand = 0;"

    def longdick(self, expr):
        return f"hand += {expr[0]};"

    def smalldick(self, expr):
        return f"hand -= {expr[0]};"

    def hugedick(self, expr):
        return f"hand *= {expr[0]};"

    def tinydick(self, expr):
        return f"hand /= {expr[0]};"

    def pee(self, expr):
        return 'print!("{}", hand);'

    def wee(self, expr):
        return 'print!("{}", hand as u8 as char);'

    def conditional(self, expr):
        return expr[0] + expr[1] + expr[2]

    while_loop = conditional

    def cockblock(self, expr):
        return "{" + "".join(expr) + "}"

    def startif(self, expr):
        return "if "
    
    def startwhile(self, expr):
        return "while "

    def bigger(self, expr):
        return f'{expr[0]} > {expr[1]}'

    def smaller(self, expr):
        return f'{expr[0]} < {expr[1]}'

    def equal(self, expr):
        return f'{expr[0]} == {expr[1]}'
