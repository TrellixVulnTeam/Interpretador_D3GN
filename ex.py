import lex as lex

class Compiler:
    def __init__(self, sData=None):
        # List of token names.   This is always required
        reserved = {
           'VAR' : 'VAR',
           'PRINT': 'PRINT',
           'IF' : 'IF',
           'FOR' : 'FOR',      
           'WHILE' : 'WHILE',
           'FUNCTION' : 'FUNCTION',
           'ELSE' : 'ELSE',   
           'PROGRAM': 'PROGRAM'      
        }

        tokens = [
            'COMANDO',
            'STRING',
            'ID',    
            'NUM',
            'DECIMAL',
            'SOMA',
            'SUBTRACAO',
            'MULTIPLICAO',
            'DIVISAO',
            'LPAREN',
            'RPAREN',        
            'PONTOEVIRGULA',
            'POTENCIA',
            'MAIOR',
            'MENOR',
            'IGUAL',
            'MAIORIGUAL',
            'MENORIGUAL',
            'DIFERENTE',
            'ATRIBUICAO',
            'VIRGULA',
            'ASPAS'    

        ] + list(reserved.values())

        # Regular expression rules for simple tokens
        t_SOMA        = r'\+'
        t_SUBTRACAO   = r'-'
        t_MULTIPLICAO = r'\*'
        t_DIVISAO     = r'/'
        t_LPAREN      = r'\('
        t_RPAREN      = r'\)'
        t_PONTOEVIRGULA = r'\;'
        t_POTENCIA    = r'\^'
        t_MAIOR       = r'\>'
        t_MENOR       = r'\<'
        t_IGUAL       = r'\=='
        t_MAIORIGUAL  = r'\>='
        t_MENORIGUAL  = r'\<='
        t_DIFERENTE   = r'\!='
        t_ATRIBUICAO  = r'\='
        t_VIRGULA     = r'\,'
        t_ASPAS       = r'\"'

        def t_COMANDO(t):
            r'[A-Z_]+'
            t.type = reserved.get(t.value,'COMANDO')    # Check for reserved words
            return t

        def t_STRING(t):
            r'"[a-zA-Z_0-9]*"'        
            return t

        def t_ID(t):
            r'[i|s|b|f|d|c|o][a-zA-Z_][a-zA-Z_0-9]*'                    
            return t

        # A regular expression rule with some action code
        def t_NUM(t):
            r'\d+'
            t.value = int(t.value)    
            return t

        # Define a rule so we can track line numbers
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        # A string containing ignored characters (spaces and tabs)
        t_ignore  = ' \t'

        # Error handling rule
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)

        # Build the lexer
        lexer = lex.lex()
            
        # Give the lexer some input
        lexer.input(sData)

        oArquivo = open('tokens.ttop', 'w')

        # Tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input

            oArquivo.write(str(tok)+'\n')

        oArquivo.close()

        import yacc as yacc
        import classes as classes
        import classes.pilha as Pilha
        import classes.factor as Factor
        import classes.term as Term
        import classes.expression as Expression

        lista = list()
        pilha = Pilha.Pilha()

        def p_expreg_soma(p):
            'expreg : expreg SOMA term'
            objeto1 = pilha.desempilha()
            objeto2 = pilha.desempilha()
            pilha.empilha(Expression.Expression(objeto2, "+", objeto1))
        #p[0] = Expression(p[1], "+", p[3])

        def p_expreg_subtracao(p):
            'expreg : expreg SUBTRACAO term'
            #p[0] = p[1] - p[3]

        def p_expreg_term(p):
            'expreg : term'
            objeto = pilha.desempilha()
            pilha.empilha(Expression.Expression(None,None,objeto))
            #p[0] = Expression(None, None, p[1]) 

        def p_term_factor(p):
            'term : factor'
            objeto = pilha.desempilha()
            pilha.empilha(Term.Term(None, None, objeto))

        def p_factor_num(p):
            'factor : NUM'
            pilha.empilha(Factor.Factor(None, p[1], None))
            #p[0] = Term(None, None, Factor(None, p[1], None))

        def p_error(p):
            print("Syntax error in input!")

        parser = yacc.yacc()

        # Test it out
        sCaminhoImg = 'run.top'
        oArquivo = open(sCaminhoImg)

        sData = ''
        with oArquivo as oInfo:
            for sLine in oInfo.readlines():
                if not sLine:
                    continue
                parser.parse(sLine)
        
