import kuy_lexer
import kuy_parser
import kuy_interpreter

from sys import *

lexer = kuy_lexer.BasicLexer()
parser = kuy_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    kuy_interpreter.BasicExecute(tree, env)
