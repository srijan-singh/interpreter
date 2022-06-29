from rply import ParserGenerator
from Parser import ast

VAR = {}


class Parser():
    def __init__(self):
     self.CONDITION = 1
     self.IF = 1
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
          'LEN',
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

     # Binary Operation
     @self.pg.production('expression : expression PLUS expression')
     @self.pg.production('expression : expression MINUS expression')
     @self.pg.production('expression : expression MULTIPLY expression')
     @self.pg.production('expression : expression DIVIDE expression')
     @self.pg.production('expression : expression MODULOUS expression')
     def binary_op(p):
          left = p[0]
          operator = p[1]
          right = p[2]
          
          if(operator.gettokentype() == 'PLUS'):

               if (type(left.value) == int and type(right.value) == int):
                    result = int(left.value) + int(right.value)
                    return ast.Number(result)

               # Concat
               else:
                    result = left.value[:-1] + right.value[1:]
                    return ast.String(result)
              
          elif(operator.gettokentype() == 'MINUS'):
               result = int(left.value) - int(right.value)
               return ast.Number(result)

          elif(operator.gettokentype() == 'MULTIPLY'):
               result = int(left.value) * int(right.value)
               return ast.Number(result)

          elif(operator.gettokentype() == 'DIVIDE'):
               result = int(left.value) / int(right.value)
               return ast.Number(int(result))

          elif(operator.gettokentype() == 'MODULOUS'):
               result = int(left.value) % int(right.value)
               return ast.Number(result)

          else:
               raise AssertionError('ERROR : BINARY OPERATION!')

     # Bracket
     @self.pg.production('expression : OPEN_SMALL_BRACKET expression CLOSE_SMALL_BRACKET')
     def expression_bracket(p):
          return p[1]

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
          operator = p[2]
          right = p[3]

          if(operator.gettokentype() == 'PLUS'):

               if (type(left.value) == int and type(right.value) == int):
                    result = int(left.value) + int(right.value)
                    return ast.Number(result)

               # Concat
               else:
                    result = left.value[:-1] + right.value[1:]
                    return ast.String(result)

               

          elif(operator.gettokentype() == 'MINUS'):
               result = int(left.value) - int(right.value)
               return ast.Number(result)

          elif(operator.gettokentype() == 'MULTIPLY'):
               result = int(left.value) * int(right.value)
               return ast.Number(result)

          elif(operator.gettokentype() == 'DIVIDE'):
               result = int(left.value) / int(right.value)
               return ast.Number(int(result))

          elif(operator.gettokentype() == 'MODULOUS'):
               result = int(left.value) % int(right.value)
               return ast.Number(result)

          elif operator.gettokentype() == 'GREATER':         
               if(left.value > right.value):                         
                    return ast.TRUE()
               
               else:
                    return ast.FALSE()

          elif operator.gettokentype() == 'SMALLER': 
               if(left.value < right.value):                         
                    return ast.TRUE()
               
               else:
                    return ast.FALSE()


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

               elif p[2].gettokentype() == 'NOT' and p[3].gettokentype() == 'EQUAL':
                    
                    if(left.value != right.value):
                         
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

     # Declaring Array
     @self.pg.production('expression : VARIABLE IDENTIFIERS ARRAY COLON expression SEMICOLON')
     def variable_dec(p):
          key = p[1]
          size = p[4]

          if key.value in VAR:
               raise AssertionError("Variable Already Declared!")

          VAR[key.value] = [None] * int(size.value)

          return ast.Array(VAR[key.value])

     # Array Indexing
     @self.pg.production('expression : LET IDENTIFIERS OPEN_BIG_BRACKET IDENTIFIERS CLOSE_BIG_BRACKET EQUAL NUMBERS SEMICOLON')
     @self.pg.production('expression : LET IDENTIFIERS OPEN_BIG_BRACKET IDENTIFIERS CLOSE_BIG_BRACKET NUMBERS SEMICOLON')
     @self.pg.production('expression : LET IDENTIFIERS OPEN_BIG_BRACKET NUMBERS CLOSE_BIG_BRACKET EQUAL NUMBERS SEMICOLON')
     @self.pg.production('expression : LET IDENTIFIERS OPEN_BIG_BRACKET NUMBERS CLOSE_BIG_BRACKET NUMBERS SEMICOLON')
     def indexing(p):
          key = p[1]
          index = p[3]
          value = p[5]

          if (index.gettokentype() == 'IDENTIFIERS'):
               index.value = VAR[index.value]

          if (value.gettokentype() == 'EQUAL'):
               value = p[6]

          if key.value in VAR:
               arr = VAR[key.value]

               if int(index.value) < len(arr):

                    if(value.gettokentype() == 'NUMBERS'):
                         (VAR[key.value])[int(index.value)] = int(value.value)
                         return ast.Array(VAR[key.value])

                    else:
                         raise AssertionError("NUMBERS only!")

               else:
                    raise AssertionError('Index out of range!')

          else:
               raise AssertionError('Variable not declared!')

     #                                                 Conditional

     # If
     @self.pg.production('expression : IF expression')
     def if_exp(p):
          operator = p[1]
          self.CONDITION = operator.eval()
          self.IF = self.CONDITION
          return p[1]

     # Else
     @self.pg.production('expression : ELSE')
     def else_exp(p):
          if (self.IF == 1):
               self.CONDITION = 0
          else:
               self.CONDITION = 1
          return ast.Number(1)

     # Begin
     @self.pg.production('expression : BEGIN')
     def begin_exp(p):
          if(self.CONDITION == 1):
               #print("begin true")
               return ast.Number(1)
          else:
               #print("begin false")
               return ast.Number(0)

     # End
     @self.pg.production('expression : END')
     def end_exp(p):
          return ast.Number(0)

     #                                                 Inbuilt Functions

     # Print
     @self.pg.production('expression : PRINT expression')     
     @self.pg.production('expression : PRINT expression SEMICOLON')
     def inbuilt_print(p):
          return ast.Print(p[1])

     # Print Var
     @self.pg.production('expression : PRINT IDENTIFIERS')
     @self.pg.production('expression : PRINT IDENTIFIERS SEMICOLON')
     def inbuilt_print(p):
          exp = p[1]
          if exp.value in VAR:
               value = VAR[exp.value]

               if (isinstance(value, int)):
                    return ast.Print(ast.Number(value))

               elif (isinstance(value, str)):
                    return ast.Print(ast.String(value))

               else:
                    return ast.Print(ast.Array(value))

     # Print Index Element
     @self.pg.production('expression : PRINT IDENTIFIERS OPEN_BIG_BRACKET IDENTIFIERS CLOSE_BIG_BRACKET SEMICOLON')
     @self.pg.production('expression : PRINT IDENTIFIERS OPEN_BIG_BRACKET NUMBERS CLOSE_BIG_BRACKET SEMICOLON')
     def get_index_value(p):
          key = p[1]
          index = p[3]

          if(index.gettokentype() == 'IDENTIFIERS'):
               print("Token")
               if index.value in VAR:
                    index = VAR[index.value]

          else:
               index = int(index.value)
               print(index)

          if key.value in VAR:
               if index < len(VAR[key.value]):
                    result = (VAR[key.value])[index]
                    return ast.Print(ast.Number(result))

               else:
                    raise AssertionError("Index out of range!")

          else:
               raise AssertionError("Variable is not declared!")

          # Print DataTypes
     
     # LEN
     @self.pg.production('expression : LEN OPEN_SMALL_BRACKET IDENTIFIERS CLOSE_SMALL_BRACKET') 
     @self.pg.production('expression : LEN OPEN_SMALL_BRACKET IDENTIFIERS CLOSE_SMALL_BRACKET SEMICOLON')
     def get_len(p):
          var = p[2].value
          value = VAR[var]

          # Strings
          if (isinstance(value, str)):
               return ast.Number(len(value)-2)     

          return ast.Number(len(value))

     # Append
     @self.pg.production('expression : APPEND OPEN_SMALL_BRACKET IDENTIFIERS COMMA expression CLOSE_SMALL_BRACKET')
     @self.pg.production('expression : APPEND OPEN_SMALL_BRACKET IDENTIFIERS COMMA expression CLOSE_SMALL_BRACKET SEMICOLON')
     def append(p):
          var = p[2].value
          arr = VAR[var]
          val = p[4].value

          # Strings
          if (isinstance(arr, list)):
               arr.append(val)
               return ast.Array(arr)

          raise AttributeError("No Insertion!")

     #                                            Error
     @self.pg.error
     def error_handle(token):
          raise ValueError("Ran into an error where it wasn't expected", token.gettokentype())

    def get_parser(self):
     return self.pg.build()

