from rply import ParserGenerator
from Parser import ast

VAR = {}

class Parser():
    def __init__(self):
     self.pg = ParserGenerator(
     
     # Keywords
     [
          # RESERVED
          'VARIABLE', 
          'LET',

          'BEGIN', 
          'END', 

          'FUNCTION',
          'RETURN', 
          'HALT',

          'IF', 
          'ELSE',

          'WHILE', 

          # DATATYPES
          'BOOLEAN',
          'NUMBERS', 
          'STRINGS',
          'ARRAY', 
          'NIL', 

          # IDENTIFIERS
          'IDENTIFIERS', 
          'COMMA',
          'COLON', 
          'SEMICOLON',   
          'OPEN_SMALL_BRACKET',
          'CLOSE_SMALL_BRACKET',
          'OPEN_BIG_BRACKET',
          'CLOSE_BIG_BRACKET', 

          #OPERATIONS   
          'PLUS', 
          'MINUS', 
          'MULTIPLY', 
          'DIVIDE', 
          'MODULOUS', 

          # COMPARISONS
          'EQUAL',
          'NOT_EQUAL',
          'GREATER',
          'SMALLER',
          'GREATER_EQUAL',
          'LESSER_EQUAL',

          # INBUILT

          'PRINT',
          'APPEND',
          'SUBARRAY',

          # ADDITIONAL FEATURE
          'NEWLINE',
          'TABSPACE'
          
     ],
     # A list of precedence rules with ascending precedence, to
     # disambiguate ambiguous production rules.
     precedence=[
          ('left', ['FUNCTION',]), 
          ('left', ['LET',]), 
          ('left', ['=']), 
          ('left', ['[',']',',']), 
          ('left', ['IF', 'ELSE']),
          ('left', ['==', '!=', '>=','>', '<', '<=',]), 
          ('left', ['PLUS', 'MINUS']),
          ('left', ['MULTIPLY', 'DIVIDE'])
     ])

    def parse(self):
     @self.pg.production('expression : STRINGS')
     def expression_string(p):
          # p is a list of the pieces matched by the right hand side of the
          # rule
          return ast.String(p[0].getstr())

     @self.pg.production('expression : NUMBERS')
     def expression_number(p):
          # p is a list of the pieces matched by the right hand side of the
          # rule
          return ast.Number(int(p[0].getstr()))
     
     @self.pg.production('expression : IDENTIFIERS')
     def get_identifiers_value(p):
          key = p[0]

          if key.value in VAR:
               
               if(isinstance(VAR[key.value], int)):
                    return ast.Number(VAR[key.value])

               elif(isinstance(VAR[key.value], str)):
                    return ast.String(VAR[key.value])

          else:
               raise AssertionError("Variable is not declared!")

     @self.pg.production('expression : VARIABLE IDENTIFIERS expression SEMICOLON')
     def variable_dec(p):
          key = p[1]
          value = p[2]

          VAR[key.value] = value.value

          if key.value in VAR:
               
               if(isinstance(VAR[key.value], int)):
                    return ast.Number(VAR[key.value])

               elif(isinstance(VAR[key.value], str)):
                    return ast.String(VAR[key.value])

     @self.pg.production('expression : LET IDENTIFIERS EQUAL expression SEMICOLON')
     @self.pg.production('expression : LET IDENTIFIERS expression SEMICOLON')
     def variable_dec(p):
          key = p[1]
          value = p[2]

          if(value.value == '='):
               value = p[3]

          if key.value in VAR:

               VAR[key.value] = value.value
               
               if(isinstance(VAR[key.value], int)):
                    return ast.Number(VAR[key.value])

               elif(isinstance(VAR[key.value], str)):
                    return ast.String(VAR[key.value])

          raise AssertionError("Variable not declared!")

     @self.pg.production('expression : PRINT expression PLUS expression SEMICOLON')
     @self.pg.production('expression : PRINT expression MINUS expression SEMICOLON')
     @self.pg.production('expression : PRINT expression MULTIPLY expression SEMICOLON')
     @self.pg.production('expression : PRINT expression DIVIDE expression SEMICOLON')
     @self.pg.production('expression : PRINT expression MODULOUS expression SEMICOLON')
     def expression_binop(p):
          left = p[1]
          right = p[3]

          if (isinstance(left.value, int) and isinstance(right.value, int)):

               if p[2].gettokentype() == 'PLUS':
                    return ast.Print(ast.Add(left, right))

               elif p[2].gettokentype() == 'MINUS':
                    return ast.Print(ast.Sub(left, right))

               elif p[2].gettokentype() == 'MULTIPLY':
                    return ast.Print(ast.Mul(left, right))

               elif p[2].gettokentype() == 'DIVIDE':
                         if(right.value != 0):
                              return ast.Print(ast.Div(left, right))
                         raise AssertionError('Division by zero not possible!')
               
               elif p[2].gettokentype() == 'MODULOUS':
                         return ast.Print(ast.Mod(left, right))

               else:
                    raise AssertionError('Oops, this should not be possible!')

          elif (isinstance(left.value, str) and isinstance(right.value, str)):

               if p[2].gettokentype() == 'PLUS':
                    return ast.Print(ast.Concat(left, right))

               else:
                    raise AssertionError('Oops, this should not be possible in string!')

          else:
               raise AssertionError('Oops, No operation!')

     
     @self.pg.production('expression : PRINT expression SEMICOLON')
     def inbuilt_print(p):
          return ast.Print(p[1])

     @self.pg.production('expression : PRINT IDENTIFIERS SEMICOLON')
     def inbuilt_print(p):
          exp = p[1]
          if exp.value in VAR:
               value = VAR[exp.value]

               if (isinstance(value, int)):
                    return ast.Print(ast.Number(value))

               elif (isinstance(value, str)):
                    return ast.Print(ast.String(value))


     @self.pg.error
     def error_handle(token):
          raise ValueError("Ran into an error where it wasn't expected", token.gettokentype())

    def get_parser(self):
     return self.pg.build()

