parser grammar SimpleCSharpParser;

options { tokenVocab=SimpleCSharpLexer; }

// --- Početna tačka ---  omogućava parsiranje niza using direktiva, namespace-ova i klasa
compilationUnit
    : (usingDirective | namespaceDecl | classDecl)* EOF
    ;

// --- Using direktiva --- Parsira using direktivu kao: using System.Text;
usingDirective
    : USING IDENT (DOT IDENT)* SEMICOLON
    ;

// --- Deklaracija namespace-a ---  Parsira namespace definiciju i njen sadržaj (npr. namespace MyApp { class ... })
namespaceDecl
    : NAMESPACE IDENT (DOT IDENT)* LBRACE classDecl* RBRACE
    ;

// --- Klasa ---  Parsira definiciju klase sa opcionalnim modifikatorima pristupa
classDecl
    : (PUBLIC | PRIVATE | PROTECTED | INTERNAL)? CLASS IDENT LBRACE classMember* RBRACE
    ;

// Pristupni modifikatori
accessModifier
    : PUBLIC
    | PRIVATE
    | PROTECTED
    | INTERNAL
    ;

// Član klase može biti metoda, konstruktor ili promenljiva, sa opcionalnim modifikatorom pristupa
classMember
    : accessModifier? methodDecl
    | accessModifier? constructorDecl
    | accessModifier? varDecl
    ;

// Konstruktor (ime kao ime klase)
constructorDecl
    : IDENT LPAREN parameterList? RPAREN block
    ;

// --- Metoda ---  Definicija metode sa tipom, imenom, parametrima i blokom
methodDecl
    : type IDENT LPAREN parameterList? RPAREN block
    ;

// Lista parametara metode
parameterList
    : parameter (COMMA parameter)*
    ;

// Jedan parametar (tip + ime)
parameter
    : type IDENT
    ;

// --- Deklaracija promenljive --- Definicija promenljive sa opcionalnom inicijalizacijom
// Varijabla može imati opcioni const modifikator
varDecl
    : (CONST)? type IDENT (ASSIGN expression)? SEMICOLON
    ;

// --- Tipovi ---  Definiše tipove koji se mogu koristiti
type
    : INT
    | FLOAT
    | DOUBLE
    | BOOL
    | CHAR
    | STRING
    | VOID
    | VAR
    | IDENT // korisnički definisani tip
    ;

// --- Naredbe --- Različite naredbe unutar tela funkcije/bloka
statement
    : block
    | ifStatement
    | forStatement
    | whileStatement
    | doWhileStatement
    | switchStatement          
    | tryCatchStatement   
    | returnStatement
    | breakStatement
    | varDecl
    | expressionStatement
    ;

// Blok naredbi unutar {}
block
    : LBRACE statement* RBRACE
    ;

breakStatement
    : BREAK SEMICOLON
    ;

// Izraz kao naredba (npr. poziv funkcije ili dodela)
expressionStatement
    : expression SEMICOLON
    ;

// --- If --- Grananje if-else
ifStatement
    : IF LPAREN expression RPAREN statement (ELSE statement)?
    ;

// --- For --- Petlja for sa inicijalizacijom, uslovima i inkrementacijom
forStatement
    : FOR LPAREN forInit? SEMICOLON expression? SEMICOLON expression? RPAREN statement
    ;

forInit
    : type IDENT ASSIGN expression        #varInit
    | expression                          #exprInit
    ;

// --- While ---
whileStatement
    : WHILE LPAREN expression RPAREN statement
    ;

// --- Do-While ---
doWhileStatement
    : DO statement WHILE LPAREN expression RPAREN SEMICOLON
    ;

// --- Switch ---
switchStatement
    : 'switch' '(' expression ')' switchBlock
    ;

switchBlock
    : '{' switchSection* '}'
    ;

switchSection
    : switchLabel+ statement+
    ;

switchLabel
    : 'case' constantExpression ':'
    | 'default' ':'
    ;

// --- Try-catch-finally ---
tryCatchStatement
    : TRY block catchClause+ finallyClause?
    ;

catchClause
    : CATCH LPAREN type IDENT RPAREN block
    ;

finallyClause
    : FINALLY block
    ;

// --- Return ---
returnStatement
    : RETURN expression? SEMICOLON
    ;

// --- Izrazi ---
expression
    : assignmentExpr
    ;

assignmentExpr
    : postfixExpr ASSIGN expression
    | logicExpr
    ;

logicExpr
    : logicExpr OR equalityExpr
    | logicExpr AND equalityExpr
    | equalityExpr
    ;

equalityExpr
    : equalityExpr (EQUAL | NOTEQUAL) relationalExpr
    | relationalExpr
    ;

relationalExpr
    : relationalExpr (LT | LE | GT | GE) additiveExpr
    | additiveExpr
    ;

additiveExpr
    : additiveExpr (PLUS | MINUS) multExpr
    | multExpr
    ;

multExpr
    : multExpr (STAR | DIV | MOD) unaryExpr
    | unaryExpr
    ;

// Unary expression: prefiks operatori + postfixExpr
unaryExpr
    : (PLUS | MINUS | NOT | '++' | '--') unaryExpr
    | postfixExpr
    ;

// Postfix expression: primary + postfix operators (0 or more)
postfixExpr
    : primaryExpr ('++' | '--')*
    ;

// Primary expression: literal, identifikator, member access, method call, or grouped expression
primaryExpr
    : literal
    | IDENT
    | IDENT DOT IDENT
    | IDENT LPAREN argumentList? RPAREN
    | LPAREN expression RPAREN
    ;

literal
    : INTEGER
    | FLOAT_LITERAL
    | STRING_LITERAL
    | CHAR_LITERAL
    | TRUE
    | FALSE
    | NULL
    ;

constantExpression
    : expression
    ;

argumentList
    : expression (COMMA expression)*
    ;