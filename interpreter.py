from lark import Tree, visitors

class Interpreter(visitors.Interpreter):
    def __init__(self, longdick_names, skip_names=False):
        """setting skip_names to true disables check for name legality (for compatability with older Dick)"""
        self.skip_names = skip_names
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
            return len(value.children)
        else:
            raise Exception(f"You can't use get_value on a {value.data}")

    def setdick(self, expr):
        if not self.skip_names:
            self.check_varname(expr.children[0].children[0])
        self.vars[expr.children[0].children[0]] = self.get_value(expr.children[1])
    
    def grab(self, expr):
        self.hand = self.get_value(expr.children[0])

    def release(self, expr):
        self.vars[expr.children[0].children[0]] = self.hand
        self.hand = 0
    
    def longdick(self, expr):
        self.hand += self.get_value(expr.children[0])

    def smalldick(self, expr):
        self.hand -= self.get_value(expr.children[0])
    
    def hugedick(self, expr):
        self.hand *= self.get_value(expr.children[0])

    def tinydick(self, expr):
        self.hand /= self.get_value(expr.children[0])
        self.hand = int(self.hand)
    
    def pee(self, expr):
        print(self.hand, end="")
    
    def wee(self, expr):
        print(chr(self.hand), end="")

    def conditional(self, expr):
        if self.check_condition(expr.children[1]):
            self.visit(expr.children[2])
    
    def while_loop(self, expr):
        while self.check_condition(expr.children[1]):
            self.visit(expr.children[2])
