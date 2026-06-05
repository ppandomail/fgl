import ply.lex as lex

reserved = {
   'começo' : 'COMECO',
   'final' : 'FINAL',
   'ler' : 'LER',
   'escrever' : 'ESCREVER'
}

# definir tokens
tokens  = ['MAS', 'MENOS', 'PUNTOCOMA', 'COMA', 'ABREPAR', 'CIERRAPAR', 'ASIGNACION', 'ID', 'CONST'] + list(reserved.values())

# definir patrones
t_MAS        = r'\+'
t_MENOS      = r'-'
t_PUNTOCOMA  = r'\;'
t_COMA       = r'\,'
t_ABREPAR    = r'\('
t_CIERRAPAR  = r'\)'
t_ASIGNACION = r'::='

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_ç]*'
    # Si coincide con palabra reservada, cambia tipo
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CONST(t):
    r'[0-9]+'
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
