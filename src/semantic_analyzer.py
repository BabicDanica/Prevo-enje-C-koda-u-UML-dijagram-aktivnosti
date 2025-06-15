from generated.SimpleCSharpParserListener import SimpleCSharpParserListener as SimpleCSharpListener
from generated.SimpleCSharpParser import SimpleCSharpParser
from generated.SimpleCSharpLexer import SimpleCSharpLexer

class SemanticAnalyzer(SimpleCSharpListener):
    def __init__(self):
        # Lista rečnika (stack) koja čuva varijable u aktuelnim opsezima (scope-ovima)
        self.scopes = [{}]
        # Lista za beleženje semantičkih grešaka
        self.errors = []
        # Trenutno analizirana metoda (po imenu)
        self.current_method = None
        # Rečnik metoda u trenutnoj klasi: ime -> {'return_type': ..., 'params': {...}}
        self.methods = {}
        # Rečnik klasa (nije korišćeno u ovom primeru, ali može služiti za širu analizu)
        self.classes = {}

    def enterBlock(self, ctx: SimpleCSharpParser.BlockContext):
        # Ulazak u novi blok koda - otvaramo novi opseg za promenljive
        self.scopes.append({})

    def exitBlock(self, ctx: SimpleCSharpParser.BlockContext):
        # Izlazak iz bloka - zatvaramo aktuelni opseg (scope)
        self.scopes.pop()

    def enterClassDecl(self, ctx: SimpleCSharpParser.ClassDeclContext):
        # Ulazak u deklaraciju klase - resetujemo metode jer je nova klasa
        self.methods.clear()

    def enterMethodDecl(self, ctx: SimpleCSharpParser.MethodDeclContext):
        # Ulazak u deklaraciju metode
        ident_token = ctx.IDENT()
        if ident_token is not None:
            self.current_method = ident_token.getText()
        else:
            self.current_method = None

        # Tip povratne vrednosti metode
        ret_type = ctx.type_().getText()

        # Prikupljanje parametara metode (ime -> tip)
        params = {}
        if ctx.parameterList():
            for p in ctx.parameterList().parameter():
                p_name_token = p.IDENT()
                p_type_ctx = p.type_()
                if p_name_token and p_type_ctx:
                    params[p_name_token.getText()] = p_type_ctx.getText()

        # Čuvamo metodu i njene informacije
        self.methods[self.current_method] = {'return_type': ret_type, 'params': params}
        # Otvaramo novi opseg koji sadrži parametre kao deklarisane promenljive
        self.scopes.append(params.copy())

    def exitMethodDecl(self, ctx: SimpleCSharpParser.MethodDeclContext):
        # Izlazak iz metode - zatvaramo njen opseg i resetujemo trenutnu metodu
        self.scopes.pop()
        self.current_method = None

    def enterVarDecl(self, ctx: SimpleCSharpParser.VarDeclContext):
        # Analiza deklaracije promenljive
        ident_token = ctx.IDENT()
        if ident_token is None:
            self.errors.append("Greška: očekivan identifikator u deklaraciji promenljive.")
            return
        var_name = ident_token.getText()
        var_type = ctx.type_().getText()
        current_scope = self.scopes[-1]

        # Provera da li je promenljiva već deklarisana u ovom opsegu
        if var_name in current_scope:
            self.errors.append(f"Greška: promenljiva '{var_name}' je već deklarisana u ovom opsegu.")
            return

        # Dodavanje promenljive u trenutni opseg
        current_scope[var_name] = var_type

        # Ako postoji dodela vrednosti prilikom deklaracije, proveravamo tip kompatibilnosti
        if ctx.expression():
            expr_type = self._infer_expression_type(ctx.expression())
            if expr_type is not None and not self._types_compatible(var_type, expr_type):
                self.errors.append(f"Greška: nekompatibilni tipovi u dodeli promenljivoj '{var_name}': {var_type} i {expr_type}.")

    def _get_ident_from_expr(self, ctx):
        # Pomoćna funkcija koja pokušava da izvuče identifikator iz izraza
        if ctx is None:
            return None

        # Pokušaj da pronađeš IDENT token u ovom kontekstu
        ident_token = ctx.getToken(SimpleCSharpLexer.IDENT, 0)
        if ident_token:
            return ident_token.getText()

        # Ako nema direktnog IDENT, pokušaj rekurzivno u decom
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'getToken'):
                ident = self._get_ident_from_expr(child)
                if ident:
                    return ident

        return None

    def enterIfStatement(self, ctx: SimpleCSharpParser.IfStatementContext):
        # Provera da li uslov u if naredbi ima tip bool
        cond_type = self._infer_expression_type(ctx.expression())
        print(f"DEBUG: If condition expression: '{ctx.expression().getText()}', inferred type: {cond_type}")
        if cond_type != 'bool':
            self.errors.append(f"Greška: uslov u if izrazu nije bool, već {cond_type}.")

    def enterWhileStatement(self, ctx: SimpleCSharpParser.WhileStatementContext):
        # Provera da li uslov u while petlji ima tip bool
        cond_type = self._infer_expression_type(ctx.expression())
        if cond_type != 'bool':
            self.errors.append(f"Greška: uslov u while izrazu nije bool, već {cond_type}.")

    def enterForStatement(self, ctx: SimpleCSharpParser.ForStatementContext):
        # Provera da li uslov u for petlji ima tip bool
        if ctx.expression(0):
            cond_type = self._infer_expression_type(ctx.expression(0))
            if cond_type != 'bool':
                self.errors.append(f"Greška: uslov u for izrazu nije bool, već {cond_type}.")

    def enterAssignmentExpr(self, ctx: SimpleCSharpParser.AssignmentExprContext):
        # Analiza izraza dodele vrednosti promenljivoj
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '=':
            left_expr = ctx.getChild(0)
            print(f"DEBUG: Left expression text: {left_expr.getText()}")
            var_name = self._get_ident_from_expr(left_expr)
            print(f"DEBUG: Extracted var_name: {var_name}")
            if var_name is None:
                self.errors.append("Greška: očekivan identifikator u izrazu dodele.")
                return

            # Provera da li je promenljiva deklarisana pre upotrebe
            var_type = self._lookup_variable_type(var_name)
            if var_type is None:
                self.errors.append(f"Greška: promenljiva '{var_name}' nije deklarisana pre upotrebe.")
                return

            expr_ctx = ctx.getChild(2)
            expr_type = self._infer_expression_type(expr_ctx)
            if expr_type is not None and not self._types_compatible(var_type, expr_type):
                self.errors.append(f"Greška: nekompatibilni tipovi u dodeli promenljivoj '{var_name}': {var_type} i {expr_type}.")
        else:
            # Nije dodela, ne prijavljuj grešku ovde
            pass

    def _lookup_variable_type(self, var_name):
        # Pretraga tipa promenljive u trenutnim opsezima, od najdubljeg ka spoljnjem
        for scope in reversed(self.scopes):
            if var_name in scope:
                return scope[var_name]
        return None

    def _lookup_method(self, method_name):
        # Pronalaženje metode po imenu u aktuelnom skupu metoda
        return self.methods.get(method_name, None)

    def _types_compatible(self, declared_type, expr_type):
        # Provera kompatibilnosti tipova (primitivni primer)
        if declared_type == expr_type:
            return True
        if declared_type == 'var':
            return True
        if declared_type == 'float' and expr_type == 'int':
            return True
        return False

    def _infer_expression_type(self, ctx):
        # Rekurzivno određivanje tipa izraza na osnovu konteksta i tokena
        if ctx is None:
            return None

        print(f"DEBUG: Inferring type for expression text: '{ctx.getText()}' with children count {ctx.getChildCount()}")

        # Ako je leaf node - literal ili identifikator
        if ctx.getChildCount() == 1:
            child = ctx.getChild(0)
            token_type = None
            if hasattr(child, 'getSymbol'):
                token_type = child.getSymbol().type
                # Prepoznavanje literalnih tipova
                if token_type == SimpleCSharpLexer.INTEGER:
                    return 'int'
                elif token_type == SimpleCSharpLexer.FLOAT_LITERAL:
                    return 'float'
                elif token_type == SimpleCSharpLexer.STRING_LITERAL:
                    return 'string'
                elif token_type == SimpleCSharpLexer.CHAR_LITERAL:
                    return 'char'
                elif token_type == SimpleCSharpLexer.TRUE or token_type == SimpleCSharpLexer.FALSE:
                    return 'bool'
                elif token_type == SimpleCSharpLexer.NULL:
                    return 'null'
        
            # Ako nije literal, može biti identifikator ili složen izraz (npr. x>5 kao jedan token)
            ident_token = ctx.getToken(SimpleCSharpLexer.IDENT, 0)
            if ident_token:
                # pokušaj da vratiš tip promenljive
                return self._lookup_variable_type(ident_token.getText())
        
            # Ako je složeniji izraz skriven u jednom čvoru, pokušaj da dalje razložiš
            # (ovo je ključno da dodaš!)
            if ctx.getChildCount() == 1 and hasattr(child, 'getChildCount') and child.getChildCount() > 0:
                return self._infer_expression_type(child)

            return None

        # Ako je složeniji izraz sa više dece, pokušaj da identifikuješ operator i rekurzivno pozoveš levo i desno dete
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2)

            left_type = self._infer_expression_type(left)
            right_type = self._infer_expression_type(right)

            if op in ['+', '-', '*', '/', '%']:
                # Operacije nad celobrojnim i realnim brojevima
                if left_type == 'int' and right_type == 'int':
                    return 'int'
                elif 'float' in (left_type, right_type):
                    return 'float'
            elif op in ['<', '>', '<=', '>=', '==', '!=']:
                # Operatori poređenja uvek vraćaju bool
                return 'bool'
            elif op in ['&&', '||']:
                # Logički operatori vraćaju bool
                return 'bool'

       # Obrada izraza u zagradama: (expr)
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            return self._infer_expression_type(ctx.getChild(1))

        # Unarni operatori, npr. +x, -x, !x
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expr = ctx.getChild(1)
            expr_type = self._infer_expression_type(expr)
            if op in ['+', '-']:
                return expr_type
            if op == '!':
                if expr_type == 'bool':
                    return 'bool'
                else:
                    return None

       # Poziv metode/funkcije: npr. methodName(...)
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '(':
            method_name = ctx.getChild(0).getText()
            method_info = self._lookup_method(method_name)
            if method_info:
                return method_info['return_type']
            return None

        # Ako ništa od navedenog ne odgovara, vraća None
        return None

    def has_errors(self):
        # Proverava da li postoje semantičke greške
        return len(self.errors) > 0

    def get_errors(self):
        # Vraća listu semantičkih grešaka
        return self.errors
