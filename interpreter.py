from lark import Tree, visitors

class Interpreter(visitors.Interpreter):
    def __init__(self):
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

    def get_value(self, value):
        """Get the value that value: Tree holds. Takes it from either a dick size literal or the dick stored in held variable"""
        if value.data == "value":
            # unwrap it
            value = value.children[0]
        if value.data == "varname":
            return self.vars[value.children[0]]
        elif value.data == "dick":
            return value.children[0]
        else:
            raise Exception(f"You can't use get_value on a {value.data}")

    def setdick(self, expr):
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
