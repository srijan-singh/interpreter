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
          'NOT',
          'GREATER',
          'SMALLER',

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
     
     # Strings
     @self.pg.production('expression : STRINGS')
     def expression_string(p):
          # p is a list of the pieces matched by the right hand side of the
          # rule
          return ast.String(p[0].getstr())

     # Numbers
     @self.pg.production('expression : NUMBERS')
     def expression_number(p):
          # p is a list of the pieces matched by the right hand side of the
          # rule
          return ast.Number(int(p[0].getstr()))
     
     # Identifiers
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

     # Single Operator
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression PLUS expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression MINUS expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression MULTIPLY expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression DIVIDE expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression MODULOUS expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression GREATER expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression SMALLER expression CLOSE_SMALL_BRACKET')
     def expression_binop(p):
          left = p[1]
          right = p[3]

          if (isinstance(left.value, int) and isinstance(right.value, int)):

               if p[2].gettokentype() == 'PLUS':
                    return ast.Add(left, right)

               elif p[2].gettokentype() == 'MINUS':
                    return ast.Sub(left, right)

               elif p[2].gettokentype() == 'MULTIPLY':
                    return ast.Mul(left, right)

               elif p[2].gettokentype() == 'DIVIDE':
                         if(right.value != 0):
                              return ast.Div(left, right)
                         raise AssertionError('Division by zero not possible!')
               
               elif p[2].gettokentype() == 'MODULOUS':
                         return ast.Mod(left, right)

               elif p[2].gettokentype() == 'GREATER':
                    
                    if(left.value > right.value):                         
                         return ast.TRUE()
                    
                    else:
                         return ast.FALSE()

               elif p[2].gettokentype() == 'SMALLER':
                    
                    if(left.value < right.value):                         
                         return ast.TRUE()
                    
                    else:
                         return ast.FALSE()

               else:
                    raise AssertionError('Oops, this should not be possible!')

          elif (isinstance(left.value, str) and isinstance(right.value, str)):

               if p[2].gettokentype() == 'PLUS':
                    return ast.Concat(left, right)

               else:
                    raise AssertionError('Oops, this should not be possible in string!')

          else:
               raise AssertionError('Oops, No operation!')

     # Double Operator
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression EQUAL EQUAL expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression GREATER EQUAL expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression SMALLER EQUAL expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression NOT EQUAL expression CLOSE_SMALL_BRACKET')
     def expression_comparison(p):
          left = p[1]
          right = p[4]

          if (isinstance(left.value, int) and isinstance(right.value, int)):

               if p[2].gettokentype() == 'EQUAL' and p[3].gettokentype() == 'EQUAL':
               
                    if(left.value == right.value):                         
                         return ast.TRUE()
                    
                    else:
                         return ast.FALSE()

               elif p[2].gettokentype() == 'GREATER' and p[3].gettokentype() == 'EQUAL':
                    
                    if(left.value >= right.value):                         
                         return ast.TRUE()
                    
                    else:
                         return ast.FALSE()

               elif p[2].gettokentype() == 'SMALLER' and p[3].gettokentype() == 'EQUAL':
                    
                    if(left.value <= right.value):                         
                         return ast.TRUE()
                    
                    else:
                         return ast.FALSE()

               elif p[2].gettokentype() == 'NOT' and p[3].gettokentype() == 'EQUAL':
                    
                    if(left.value != right.value):                         
                         return ast.TRUE()
                    
                    else:
                         return ast.FALSE()

               else:
                    raise AssertionError('Oops, this should not be possible!')

          elif (isinstance(left.value, str) and isinstance(right.value, str)):

               if p[2].gettokentype() == 'EQUAL' and p[3].gettokentype() == 'EQUAL':
                    
                    if(left.value == right.value):
                         
                         return ast.TRUE()
                    else:
                         return ast.FALSE()

               else:
                    raise AssertionError('Oops, this should not be possible in string!')

          else:
               raise AssertionError('Oops, No operation!')

     # Declaring Variable
     @self.pg.production('expression : VARIABLE IDENTIFIERS expression SEMICOLON')
     def variable_dec(p):
          key = p[1]
          value = p[2]

          if key.value in VAR:
               raise AssertionError("Variable Already Declared!")

          VAR[key.value] = value.value

          if key.value in VAR:
               
               if(isinstance(VAR[key.value], int)):
                    return ast.Number(VAR[key.value])

               elif(isinstance(VAR[key.value], str)):
                    return ast.String(VAR[key.value])

     # Updating Variable
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

     # Without Braces
     @self.pg.production('expression : PRINT expression PLUS expression SEMICOLON')
     @self.pg.production('expression : PRINT expression MINUS expression SEMICOLON')
     @self.pg.production('expression : PRINT expression MULTIPLY expression SEMICOLON')
     @self.pg.production('expression : PRINT expression DIVIDE expression SEMICOLON')
     @self.pg.production('expression : PRINT expression MODULOUS expression SEMICOLON')
     def print_binop(p):
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

     # Print
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

     # Error
     @self.pg.error
     def error_handle(token):
          raise ValueError("Ran into an error where it wasn't expected", token.gettokentype())

    def get_parser(self):
     return self.pg.build()

