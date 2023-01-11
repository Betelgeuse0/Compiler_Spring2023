from Lexing.kxi_lexer import KxiLexer

def lexing(fname):
    with open(fname) as f:
        data = f.read()

    lexer = KxiLexer()
    for t in lexer.tokenize(data):
        print(f'{t.type:<20} {t.lineno:<10} {t.value:<15}')

if __name__ == '__main__':
    lexing('Lexing/lexer_test.txt')
