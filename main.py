from Lexical import lexer
from Parser import parser

import warnings

warnings.filterwarnings("ignore", category=Warning)

lexer = lexer.Lexer().get_lexer()

pg = parser.Parser()
pg.parse()
parser = pg.get_parser()

filepath = "Source\\test.SCREAM"
file = open(filepath)

lines = []

CONDITION = False

for line in file:

     if line[:2] == r'//':
          continue

     if line == '\n':
          continue

     keyword = line.strip()

     if(CONDITION):
          if(keyword == 'END'):
               CONDITION = False
          continue

     tokens = lexer.lex(line)

     output = parser.parse(tokens).eval()

     if(keyword == 'BEGIN' and output == 0):
          CONDITION = True

file.close()


