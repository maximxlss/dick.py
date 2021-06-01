from lark import *
from grammar import grammar

l = Lark(grammar)
with open("test.dick") as f:
    t = l.parse(f.read())

print(t)
