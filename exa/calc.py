import ply.lex as lex

# definir tokens
tokens  = ('IDENTIFICADOR', 'CONST', 'MAS', 'MENOS', 'PUNTOCOMA', 'COMA', 'ABREPAR', 
           'CIERRAPAR', 'ASIGNACION', 'COMEÇO', 'FINAL', 'LER', 'ESCREVER')

# definir patrones
t_MAS        = r'\+'
t_MENOS      = r'\-'
t_PUNTOCOMA  = r'\;'
t_COMA       = r'\,'
t_ABREPAR    = r'\('
t_CIERRAPAR  = r'\)'
t_ASIGNACION = r'\::='
t_COMEÇO     = r'começo'
t_FINAL      = r'final'
t_LER        = r'ler'
t_ESCREVER   = r'escrever'

def t_IDENTIFICADOR(t):
    r'L | L(L | \d) | L(L | \d | \_)(L | \d) | L (LL | L\d | \dL | \d\d | \_L | \_\d | L\_ | \d\_)(L | \d)'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# construir scanner
lexer = lex.lex()
lexer.input('começo A ::= 1; final')
while 1:
    tok = lexer.token()
    if not tok: break
    print(tok)
