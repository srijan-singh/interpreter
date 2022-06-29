from rply import LexerGenerator

class Lexer():
     
     def __init__(self):
          self.lg = LexerGenerator()

     def _add_tokens(self):

          # Statements
          self.lg.add('VARIABLE', r'VAR')
          self.lg.add('LET', r'LET')
          self.lg.add('BEGIN', r'BEGIN')
          self.lg.add('END', r'END')
          self.lg.add('FUNCTION', r'FUNC')
          self.lg.add('IF', r'IF')
          self.lg.add('ELSE', r'ELSE')
          self.lg.add('WHILE', r'WHILE')
          self.lg.add('RETURN', r'RETURN')
          self.lg.add('HALT', r'HALT')

          # Builtins
          self.lg.add('PRINT', r'PRINT')
          self.lg.add('APPEND', r'APPEND')
          self.lg.add('LEN', r'LEN')
          self.lg.add('SUBARRAY', r'SUBARRAY')

          # Operations
          self.lg.add('PLUS', r'\+')
          self.lg.add('MINUS', r'\-')
          self.lg.add('MULTIPLY', r'\*')
          self.lg.add('DIVIDE', r'\/')
          self.lg.add('MODULOUS', r'\%')

          # Comparison
          self.lg.add('EQUAL', r'\=')
          self.lg.add('NOT', r'\!')
          self.lg.add('GREATER', r'\>')
          self.lg.add('SMALLER', r'\<')

          # Data Types
          self.lg.add('BOOLEAN', r'TRUE|FALSE')
          self.lg.add('NUMBERS', r'\d+')
          self.lg.add('STRINGS', r'\'[a-zA-Z0-9 \!\,]*\'')
          self.lg.add('ARRAY', r'ARRAY')
          self.lg.add('NIL', r'NIL')

          # Identifiers
          self.lg.add('IDENTIFIERS', r'[_A-Za-z][_A-Za-z0-9]*')
          self.lg.add('COMMA', r'\,')
          self.lg.add('COLON', r'\:')
          self.lg.add('SEMICOLON', r'\;')
          self.lg.add('OPEN_SMALL_BRACKET', r'\(')
          self.lg.add('CLOSE_SMALL_BRACKET', r'\)')
          self.lg.add('OPEN_BIG_BRACKET', r'\[')
          self.lg.add('CLOSE_BIG_BRACKET', r'\]')

          # Strings Features
          self.lg.add('NEWLINE', r'\n')
          self.lg.add('TABSPACE', r'\t')
          
          # Ignore Whitespace 
          self.lg.ignore(r'\s')
          # Ignore Comments
          self.lg.ignore(r'\/\/[ a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*')

     def get_value(self, token):
          token.value

     def get_lexer(self):
          self._add_tokens()
          return self.lg.build()

