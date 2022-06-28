from rply import LexerGenerator

class LexicalAnalyzer:
     
     def __init__(self, file_path):

          self.file_path = file_path
          self.lg = LexerGenerator()

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
          self.lg.add('SUBARRAY', r'SUBARRAY')

          # Operations
          self.lg.add('PLUS', r'\+')
          self.lg.add('MINUS', r'\-')
          self.lg.add('MULTIPLY', r'\*')
          self.lg.add('DIVIDE', r'\/')
          self.lg.add('MODULOUS', r'\%')
          self.lg.add('COLON', r'\:')
          self.lg.add('SEMICOLON', r'\;')

          # Comparison
          self.lg.add('EQUAL', r'\=')
          self.lg.add('NOT_EQUAL', r'\!\=')
          self.lg.add('GREATER_EQUAL', r'\>\=')
          self.lg.add('LESSER_EQUAL', r'\<\=')

          # Data Types
          self.lg.add('BOOLEAN', r'TRUE|FALSE')
          self.lg.add('NUMBERS', r'\d+')
          self.lg.add('STRINGS', r'\'[a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*\'')
          self.lg.add('ARRAY', r'ARRAY')
          self.lg.add('NIL', r'NIL')

          # User Define
          self.lg.add('IDENTIFIERS', r'[A-Za-z_][A-Za-z0-9]*')
          self.lg.add('ARGUMENTS', r'\([a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*\)')
          self.lg.add('INDEX', r'\[[a-zA-Z_0-9]*\]')

          # Strings Features
          self.lg.add('NEWLINE', r'\n')
          self.lg.add('TABSPACE', r'\t')
          
          # Ignore Whitespace 
          self.lg.ignore(r'\s')
          # Ignore Comments
          self.lg.ignore(r'\/\/[ a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*')

     def get_tokens(self) -> list:

          Tokens = list()

          lexer = self.lg.build()

          file = open(self.file_path)

          for elm in lexer.lex(file.read()):
               Tokens.append(elm)

          file.close()

          return Tokens


     def print_tokens(self) -> None:

          lexer = self.lg.build()

          file = open(self.file_path)

          for elm in lexer.lex(file.read()):
               print(elm)

          file.close()


if __name__ == "__main__":
     l = LexicalAnalyzer("Source\main.SCREAM")
     #l.print_tokens()
     tokens = l.get_tokens()
     print(len(tokens))
     print(tokens)
