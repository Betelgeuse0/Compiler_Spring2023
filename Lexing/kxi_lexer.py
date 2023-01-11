from sly import Lexer


class KxiLexer(Lexer):
    tokens = {
        BOOL, BREAK, CASE, CLASS, CHAR, CIN, COUT, DEFAULT, ELSE,
        FALSE, IF, INT, KXI2022, NEW, NULL, PUBLIC, PRIVATE, RETURN,
        STRING, SWITCH, TRUE, VOID, WHILE,

        COLON, SCOLON, LCURLY, RCURLY, LPAREN, RPAREN, LSQARE, RSQUARE, EQUAL,
        CEQUAL, NEQUAL, GEQUAL, LEQUAL, GREAT, LESS, AND, OR,
        NOT, PLUS, MINUS, TIMES, DIVIDE, PEQUAL, MEQUAL, TEQUAL, DEQUAL,
        LSHIFT, RSHIFT, DOT, COMMA,

        ID, CHAR_LITERAL, STRING_LITERAL, INT_LITERAL
    }


    @_(r'//.*(\r|\n|\r\n)*')
    def ignore_comment(self, t):
        self.lineno += t.value.count('\n')

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    ignore_space = r'\s+'

    # KEYWORDS

    BOOL = 'bool'
    BREAK = 'break'
    CASE = 'case'
    CLASS = 'class'
    CHAR = 'char'
    CIN = 'cin'
    COUT = 'cout'
    DEFAULT = 'default'
    ELSE = 'else'
    FALSE = 'false'
    IF = 'if'
    INT = 'int'
    KXI2022 = 'kxi2022'
    NEW = 'new'
    NULL = 'null'
    PUBLIC = 'public'
    PRIVATE = 'private'
    RETURN = 'return'
    STRING = 'string'
    SWITCH ='switch'
    TRUE = 'true'
    VOID = 'void'
    WHILE = 'while'

    # PUNCTUATION

    COLON = r':'
    SCOLON = r';'
    LCURLY = r'{'
    RCURLY = r'}'
    LPAREN = r'\('
    RPAREN = r'\)'
    LSQARE = r'\['
    RSQUARE = r'\]'

    # must be above equal
    PEQUAL = r'\+='
    MEQUAL = r'-='
    TEQUAL = r'\*='
    DEQUAL = r'/='
    CEQUAL = r'=='
    NEQUAL = r'!='
    GEQUAL = r'>='
    LEQUAL = r'<='

    EQUAL = r'='

    # must be above LESS and GREAT
    LSHIFT = r'<<'
    RSHIFT = r'>>'

    GREAT = r'>'
    LESS = r'<'
    AND = r'&&'
    OR = r'\|\|'
    NOT = '!'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    DOT = r'\.'
    COMMA = r','

    # OTHER TERMINALS

    ID = r'([A-Za-z]|_)([A-Za-z]|_|[0-9])*'
    CHAR_LITERAL = r"'(((?![\"'\\])[\x20-\x7F]|\\r|\\n|\\t|\\)|\"|\\')'"
    STRING_LITERAL = r'"((?!["])[\x20-\x7F]|\\r|\\n|\\t|\\|\'|\\")*"'
    INT_LITERAL = f'[0-9]+'

    def error(self, t):
        self.index += 1
        t.type = 'UNKNOWN'
        t.value = t.value[0]
        return t
