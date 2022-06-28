from rply import LexerGenerator

lg = LexerGenerator()

# Statements
lg.add('VARIABLE', r'VAR')
lg.add('LET', r'LET')
lg.add('BEGIN', r'BEGIN')
lg.add('END', r'END')
lg.add('FUNCTION', r'FUNC')
lg.add('IF', r'IF')
lg.add('ELSE', r'ELSE')
lg.add('WHILE', r'WHILE')
lg.add('RETURN', r'RETURN')
lg.add('HALT', r'HALT')

# Builtins
lg.add('PRINT', r'PRINT')
lg.add('APPEND', r'APPEND')
lg.add('SUBARRAY', r'SUBARRAY')

# Operations
lg.add('PLUS', r'\+')
lg.add('MINUS', r'\-')
lg.add('MULTIPLY', r'\*')
lg.add('DIVIDE', r'\/')
lg.add('MODULOUS', r'\%')
lg.add('COLON', r'\:')
lg.add('SEMICOLON', r'\;')

# Comparison
lg.add('EQUAL', r'\=')
lg.add('NOT_EQUAL', r'\!\=')
lg.add('GREATER_EQUAL', r'\>\=')
lg.add('LESSER_EQUAL', r'\<\=')

# Data Types
lg.add('BOOLEAN', r'TRUE|FALSE')
lg.add('NUMBERS', r'\d+')
lg.add('STRINGS', r'\'[a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*\'')
lg.add('ARRAY', r'ARRAY')
lg.add('NIL', r'NIL')

# User Define
lg.add('IDENTIFIERS', r'[A-Za-z_][A-Za-z0-9]*')
lg.add('ARGUMENTS', r'\([a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*\)')
lg.add('INDEX', r'\[[a-zA-Z_0-9]*\]')

# Strings Features
lg.add('NEWLINE', r'\n')
lg.add('TABSPACE', r'\t')
 
# Ignore Whitespace 
lg.ignore(r'\s')
# Ignore Comments
lg.ignore(r'\/\/[ a-zA-Z0-9~`!@#$%^&*()-+=_ \{\[\]\}\|\:\;\"\'\,\<\.\>\/\?]*')
 
lexer = lg.build()

code = """
     VAR A 5;
     VAR B 10;
     PRINT A+B; // prints '15'
     PRINT A*B; // prints '50'
     PRINT B/A; // prints '2'
     PRINT B-A; // prints '5'
     PRINT B%A; // prints '0'
     LET A 'Hello, ';
     LET B 'World!';
     PRINT A+B; // prints: 'Hello, World!'
     PRINT B+A; // prints: 'World!Hello, '
     LET A = 3;
     LET B = 5;
     IF (A > B)
     BEGIN
     PRINT '3 is greater than 5';
     END
     ELSE
     BEGIN
     PRINT '5 is greater than 3';
     END
     VAR FACTORIAL 1;
     VAR NUM 1;
     WHILE(NUM <= 5)
     BEGIN
     LET FACTORIAL (FACTORIAL * NUM);
     LET NUM (NUM+1);
     END
     PRINT FACTORIAL; // prints 120
     VAR ITEMS ARRAY:5;
     PRINT ITEMS; // prints [NIL, NIL, NIL, NIL, NIL]
     LET NUM 0;
     WHILE (NUM < 5)
     BEGIN
     LET ITEMS[NUM] (NUM * 2);
     LET NUM (NUM + 1);
     END
     PRINT ITEMS; // prints [0, 2, 4, 6, 8]
     FUNC SQUARE_SUM(NUM1, NUM2)
     BEGIN
     RETURN (NUM1 * NUM1) + (NUM2 * NUM2);
     END
     LET A = 3;
     LET B = 5;
     VAR C = SQUARE_SUM(A, B);
     PRINT C; // prints '34'
"""

source_code = open('Source\main.SCREAM')

for elm in lexer.lex(source_code.read()):
     print(elm)

source_code.close()

