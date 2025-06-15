lexer grammar SimpleCSharpLexer;

// --- Ključne reči - kontrolne strukture ---
IF       : 'if';
ELSE     : 'else';
WHILE    : 'while';
FOR      : 'for';
DO       : 'do';
SWITCH   : 'switch';
CASE     : 'case';
DEFAULT  : 'default';
BREAK    : 'break';
CONTINUE : 'continue';
RETURN   : 'return';
TRY      : 'try';
CATCH    : 'catch';
FINALLY  : 'finally';
THROW    : 'throw';
GOTO     : 'goto';

// --- Ključne reči - tipovi i definicije ---
INT      : 'int';
FLOAT    : 'float';
DOUBLE   : 'double';
CHAR     : 'char';
STRING   : 'string';
BOOL     : 'bool';
VOID     : 'void';
OBJECT   : 'object';
VAR      : 'var';
NULL     : 'null';

// --- Ključne reči - klase, pristup, itd. ---
CLASS     : 'class';
STRUCT    : 'struct';
INTERFACE : 'interface';
ENUM      : 'enum';
NAMESPACE : 'namespace';
USING     : 'using';

PUBLIC     : 'public';
PRIVATE    : 'private';
PROTECTED  : 'protected';
INTERNAL   : 'internal';
STATIC     : 'static';
VIRTUAL    : 'virtual';
OVERRIDE   : 'override';
ABSTRACT   : 'abstract';
SEALED     : 'sealed';
READONLY   : 'readonly';
CONST      : 'const';
NEW        : 'new';
THIS       : 'this';
BASE       : 'base';
IN         : 'in';
OUT        : 'out';
REF        : 'ref';
PARAMS     : 'params';
IS         : 'is';
AS         : 'as';
TYPEOF     : 'typeof';

// --- Boolean literal ---
TRUE       : 'true';
FALSE      : 'false';

// --- Identifikatori ---
IDENT
    : [_A-Za-z] [_A-Za-z0-9]*
    ;

// --- Brojevi ---
INTEGER
    : [0-9]+
    ;

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?
    ;

// --- String i char literal ---
STRING_LITERAL
    : '"' (~["\\] | '\\' .)* '"'
    ;

CHAR_LITERAL
    : '\'' (~["\\] | '\\' .) '\''
    ;


// --- Operatori ---
PLUS        : '+';
MINUS       : '-';
STAR        : '*';
DIV         : '/';
MOD         : '%';

ASSIGN      : '=';
PLUS_ASSIGN : '+=';
MINUS_ASSIGN: '-=';
MUL_ASSIGN  : '*=';
DIV_ASSIGN  : '/=';
MOD_ASSIGN  : '%=';

EQUAL       : '==';
NOTEQUAL    : '!=';
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';

AND         : '&&';
OR          : '||';
NOT         : '!';

BIT_AND     : '&';
BIT_OR      : '|';
BIT_XOR     : '^';
BIT_NOT     : '~';
LSHIFT      : '<<';
RSHIFT      : '>>';

INCREMENT   : '++';
DECREMENT   : '--';

NULL_COALESCING : '??';
TERNARY_COND    : '?';
COLON           : ':';

// --- Specijalni simboli ---
SEMICOLON : ';';
COMMA     : ',';
DOT       : '.';
LPAREN    : '(';
RPAREN    : ')';
LBRACE    : '{';
RBRACE    : '}';
LBRACK    : '[';
RBRACK    : ']';


// --- Komentari ---
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

// --- Whitespace ---
WS
    : [ \t\r\n]+ -> skip
    ;
