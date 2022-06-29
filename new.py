from Lexical import lexer
from Parser import parser

import warnings

warnings.filterwarnings("ignore", category=Warning)

lexer = lexer.Lexer().get_lexer()

pg = parser.Parser()
pg.parse()
parser = pg.get_parser()

filepath = "Source\\trial.SCREAM"
file = open(filepath)

for line in file:
     if line == '\n':
          continue
     tokens = lexer.lex(line)
     parser.parse(tokens).eval()

file.close()


