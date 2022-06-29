from Lexical import lexer
from Parser import parser

from rply import Token

import warnings

warnings.filterwarnings("ignore", category=Warning)

lexer = lexer.Lexer().get_lexer()

pg = parser.Parser()
pg.parse()
parser = pg.get_parser()

filepath = "Source\\trial.SCREAM"
file = open(filepath)

lines = []

CONDITION = False

for line in file:
     if line == '\n':
          continue

     keyword = line.strip()

     if(keyword == 'BEGIN' and output == 0):
          CONDITION = True
          print('shi pakde hai')

     if(CONDITION):
          if(keyword == 'END'):
               CONDITION = False
          continue

     tokens = lexer.lex(line)

     output = parser.parse(tokens).eval()

file.close()


