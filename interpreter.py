from lark import Tree

class Interpreter:
    def __init__(self, longdick_names, skip_names=False):
        """setting skip_names to true disables check for name legality (for compatability with older Dick)"""
        if skip_names:
            global get_varname
            get_varname = lambda: None
        self.longdick_names = longdick_names
        self.vars = {}
        self.hand = 0

    def check_condition(self, value):
        x = self.get_value(value.children[0])
        y = self.get_value(value.children[1])
        if value.data == "bigger":
            return x > y
        elif value.data == "smaller":
            return x < y
        elif value.data == "equal":
            return x == y

    def check_varname(self, value):
        """Check a varname if it is legal in LongDick"""
        i = 0
        for name in self.longdick_names:
            if name.lower() in value.lower():
                i += 1
        if i == 0:
            raise Exception(f"Variable name {value} is not valid in LongDick!")

    def get_value(self, value):
        """Get the value that value: Tree holds. Takes it from either a dick size literal or the dick stored in held variable"""
        if value.data == "value":
            # unwrap it
            value = value.children[0]
        if value.data == "varname":
            return self.vars[value.children[0]]
        elif value.data == "dick":
            value.children = list(filter(lambda x: isinstance(x, Tree) and x.data == "dickmid", value.children))
            return len(value.children)
        else:
            raise Exception(f"You can't use get_value on a {value.data}")

    def run(self, expr):
        try:
            if expr.type == "WS":
                return
        except:
            pass
        if expr.data == "setdick":
            self.check_varname(expr.children[0].children[0])
            self.vars[expr.children[0].children[0]] = self.get_value(expr.children[1])
        elif expr.data == "grab":
            self.hand = self.get_value(expr.children[0])
        elif expr.data == "release":
            self.vars[expr.children[0].children[0]] = self.hand
            self.hand = 0
        elif expr.data == "longdick":
            self.hand += self.get_value(expr.children[0])
        elif expr.data == "smalldick":
            self.hand -= self.get_value(expr.children[0])
        elif expr.data == "hugedick":
            self.hand *= self.get_value(expr.children[0])
        elif expr.data == "tinydick":
            self.hand /= self.get_value(expr.children[0])
        elif expr.data == "pee":
            print(self.hand, end="")
        elif expr.data == "wee":
            print(chr(self.hand), end="")
        elif expr.data == "conditional":
            if self.check_condition(expr.children[1]):
                for expr in expr.children[2].children:
                    self.run(expr)
        elif expr.data == "while":
            while self.check_condition(expr.children[1]):
                for expr in expr.children[2].children:
                    self.run(expr)
