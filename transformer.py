from lark import Tree, visitors, Token

class Transformer(visitors.Transformer):
    def __init__(self, longdick_names, skip_names=False):
        """setting skip_names to true disables check for name legality (for compatability with older Dick)"""
        self.skip_names = skip_names
        self.longdick_names = longdick_names

    def check_varname(self, value):
        """Check a varname if it is legal in LongDick"""
        i = 0
        for name in self.longdick_names:
            if name.lower() in value.lower():
                i += 1
        if i == 0:
            raise Exception(f"Variable name {value} is not valid in LongDick!")

    def dick(self, value):
        return Tree('dick', [len(value)])

    def varname(self, value):
        if not self.skip_names:
            self.check_varname(value[0])
        return Tree('varname', [value[0]])
