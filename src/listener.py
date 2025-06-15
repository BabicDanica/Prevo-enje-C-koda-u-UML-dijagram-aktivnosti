# U ANTLR4, kada definišeš parser, možeš generisati listener klase koje prate kretanje kroz sintaksno stablo (parse tree) 
# prilikom parsiranja koda. Listener se ponaša kao "slušač" događaja — pozivaju se njegove metode kada parser
#  uđe u neko pravilo i kada izađe iz tog pravila.

from generated.SimpleCSharpParser import SimpleCSharpParser
from generated.SimpleCSharpParserListener import SimpleCSharpParserListener

class ActivityDiagramListener(SimpleCSharpParserListener):
    def __init__(self):
        super().__init__()
        self.current_method = None
        self.diagrams = {}
        self.in_if_chain = False
        self.in_else_branch = False
        self.else_printed = False
        self.last_if_was_else_if = False
        self.stack = []
        self.in_switch = False
        self.case_count = 0
        self.switch_expr = None

    def expression_to_string(self, expr_ctx):
        # Pretvori expression kontekst u string, možeš prilagoditi za kompleksnije izraze
        if expr_ctx is None:
            return ""
        return expr_ctx.getText()

    def enterMethodDecl(self, ctx):
        self.current_method = ctx.IDENT().getText()
        self.diagrams[self.current_method] = ["@startuml", "start"]
        self.in_if_chain = False
        self.in_else_branch = False
        self.else_printed = False
        self.last_if_was_else_if = False

    def exitMethodDecl(self, ctx):
        if self.in_if_chain:
            self.diagrams[self.current_method].append("endif")
        self.diagrams[self.current_method].append("stop")
        self.diagrams[self.current_method].append("@enduml")
        self.current_method = None
        self.in_if_chain = False
        self.in_else_branch = False
        self.else_printed = False
        self.last_if_was_else_if = False
    
    def enterIfStatement(self, ctx):
        condition = self.expression_to_string(ctx.expression())
        parent = ctx.parentCtx

        is_else_if = False
        if isinstance(parent, SimpleCSharpParser.IfStatementContext):
            else_stmt = parent.statement(1) if parent.ELSE() else None
            if else_stmt == ctx:
                is_else_if = True

        if not self.in_if_chain:
            self.diagrams[self.current_method].append(f"if ({condition}) then (yes)")
            self.in_if_chain = True
            self.in_else_branch = False
            self.else_printed = False
            self.last_if_was_else_if = False
        else:
            self.diagrams[self.current_method].append(f"(no) elseif ({condition}) then (yes)")
            self.in_else_branch = False
            self.last_if_was_else_if = True

    def _append_code_line(self, ctx):
        if not self.current_method:
            return
        if self.in_else_branch and not self.else_printed:
            self.diagrams[self.current_method].append("else (nothing)")
            self.else_printed = True
        text = ctx.getText()
        self.diagrams[self.current_method].append(f": {text};")
    
    def _append(self, text):
        if self.current_method not in self.diagrams:
            self.diagrams[self.current_method] = []
        self.diagrams[self.current_method].append(text)
    
    def enterExpressionStatement(self, ctx):
        if not self.current_method:
            return

        try:
            expr_text = self.expression_to_string(ctx.expression())
            if "missing" in expr_text or "<" in expr_text and ">" in expr_text:
                # Izbegni generisanje oblačića sa greškama
                return
            self._append(f": {expr_text};")
        except Exception as e:
            # Ako dođe do greške, samo je ignoriši ili zapiši kao komentar
            print(f"DEBUG: expression parse error: {e}")

    def enterVarDecl(self, ctx: SimpleCSharpParser.VarDeclContext):
        if not self.current_method:
            return

        try:
            # Tip promenljive (npr. "int")
            var_type = ctx.type_().getText()  # ili ctx.type().getText(), zavisno od parsera
            # Ime promenljive (npr. "a")
            var_name = ctx.IDENT().getText()

            # Konstrukcija izraza ako postoji
            if ctx.expression():
                # Bolje je koristiti helper funkciju koja lepo vraća string izraza,
                # a ne getText() koji samo spaja sve bez razmaka
                expr = self.expression_to_string(ctx.expression())
                line = f"{var_type} {var_name} = {expr};"
            else:
                line = f"{var_type} {var_name};"

            # Dodaj u diagram (pretpostavljam da imaš funkciju za to)
            self._append(f": {line}")
        except Exception as e:
            print(f"DEBUG EXCEPTION in enterVarDecl: {e}")
            # Ako nešto krene po zlu, dodaj sirov tekst iz konteksta
            self._append(f": {ctx.getText()}")

    def enterReturnStatement(self, ctx):
        self._append_code_line(ctx)

    def enterBreakStatement(self, ctx):
        self._append_code_line(ctx)

    def enterStatement(self, ctx):
        parent = ctx.parentCtx
        if isinstance(parent, SimpleCSharpParser.IfStatementContext):
            stmts = parent.statement()
            if len(stmts) == 2 and ctx == stmts[1]:
                # Ovo je else grana roditeljskog if
                # Provera da li je else if (tj. da li else sadrži if)
                children = list(ctx.children)
                if children and isinstance(children[0], SimpleCSharpParser.IfStatementContext):
                    # Ovo je else if, ne generiši "else (nothing)"
                    self.in_else_branch = True
                    self.else_printed = False
                    return
                if not self.else_printed:
                    self.diagrams[self.current_method].append("else (nothing)")
                    self.else_printed = True
                self.in_else_branch = True

    def exitIfStatement(self, ctx):
        parent = ctx.parentCtx
        is_else_if = False
        if isinstance(parent, SimpleCSharpParser.IfStatementContext):
            else_stmt = parent.statement(1) if parent.ELSE() else None
            if else_stmt == ctx:
                is_else_if = True
        if not is_else_if and self.in_if_chain:
            self.diagrams[self.current_method].append("endif")
            self.in_if_chain = False
            self.in_else_branch = False
            self.else_printed = False
            self.last_if_was_else_if = False
    
    def enterWhileStatement(self, ctx):
        if not self.current_method:
            return

        try:
            condition = ""
            if ctx.expression():
                condition = self.expression_to_string(ctx.expression())

            self.diagrams[self.current_method].append(f"while ({condition})")
            self.stack.append("while")

        except Exception as e:
            self.diagrams[self.current_method].append(f": // Greška u while petlji: {str(e)}")

    
    def exitWhileStatement(self, ctx):
        if self.current_method and self.stack and self.stack[-1] == "while":
            self.diagrams[self.current_method].append("endwhile")
            self.stack.pop()

    def enterDoWhileStatement(self, ctx):
        if not self.current_method:
            return
        self.diagrams[self.current_method].append("repeat")
        self.stack.append("do-while")

    def exitDoWhileStatement(self, ctx):
        if self.current_method and self.stack and self.stack[-1] == "do-while":
            condition = ""
            if ctx.expression():
                condition = self.expression_to_string(ctx.expression())
            self.diagrams[self.current_method].append(f"repeat while ({condition})")
            self.stack.pop()

    def enterForStatement(self, ctx):
        if not self.current_method:
            return

        try:
            # Inicijalizacija - prva naredba u for petlji
            init = ""
            if hasattr(ctx, 'forInit') and ctx.forInit():
                init = ctx.forInit().getText()
            else:
                if len(ctx.children) > 2:
                    init = ctx.children[2].getText()

            # Uslov
            cond = ""
            if ctx.expression() and len(ctx.expression()) > 0:
                cond = ctx.expression(0).getText()

            # Update
            update = ""
            if hasattr(ctx, 'forUpdate') and ctx.forUpdate():
                update = ctx.forUpdate().getText()
            else:
                if len(ctx.children) > 6:
                    update = ctx.children[6].getText()

            # Dodaj inicijalizaciju pre while petlje
            if init:
                self.diagrams[self.current_method].append(f": {init};")

            # Početak while petlje sa uslovom
            self.diagrams[self.current_method].append(f"while ({cond})")

            # Sačuvaj update da bi ga dodao unutar petlje
            self.stack.append(("for", update))

        except Exception as e:
            self.diagrams[self.current_method].append(f": // Greška u for petlji: {str(e)}")

    def exitForStatement(self, ctx):
        if self.current_method and self.stack and self.stack[-1][0] == "for":
            update = self.stack[-1][1]

            # Dodaj update kao akciju pre završetka petlje
            if update:
                self.diagrams[self.current_method].append(f": {update};")

            # Zatvori while petlju
            self.diagrams[self.current_method].append("endwhile")

            self.stack.pop()

    def enterTryCatchStatement(self, ctx):
        if self.current_method:
            self.diagrams[self.current_method].append("group try")

    def exitTryCatchStatement(self, ctx):
        pass

    def enterCatchClause(self, ctx):
        if self.current_method:
            self.diagrams[self.current_method].append("end group")
            try:
                ex_type = ctx.type().getText()
                ex_name = ctx.IDENTIFIER().getText()
            except Exception:
                ex_type = "Exception"
                ex_name = "e"
            self.diagrams[self.current_method].append(f"group catch ({ex_type} {ex_name})")

    def exitCatchClause(self, ctx):
        if self.current_method:
            self.diagrams[self.current_method].append("end group")

    def enterFinallyClause(self, ctx):
        if self.current_method:
            self.diagrams[self.current_method].append("group finally")

    def exitFinallyClause(self, ctx):
        if self.current_method:
            self.diagrams[self.current_method].append("end group")

    def enterSwitchStatement(self, ctx):
        if self.current_method and ctx.expression():
            self.in_switch = True
            self.case_count = 0
            self.switch_expr = self.expression_to_string(ctx.expression())
            # Početak switch bloka u PlantUML-u
            self.diagrams[self.current_method].append(f"switch ({self.switch_expr})")

    def enterSwitchLabel(self, ctx):
        if not (self.current_method and self.in_switch):
            return

        try:
            if ctx.CASE():
                label = ctx.constantExpression().getText() if ctx.constantExpression() else "?"
                self.diagrams[self.current_method].append(f"case ({label})")
                self.case_count += 1

            elif ctx.DEFAULT():
                self.diagrams[self.current_method].append("case (default)")

        except Exception as e:
            self.diagrams[self.current_method].append(f": // Greska u switch labeli: {str(e)}")

    def exitSwitchStatement(self, ctx):
        if self.current_method and self.in_switch:
            self.diagrams[self.current_method].append("endswitch")
            self.in_switch = False
            self.case_count = 0
            self.switch_expr = None

    def get_activity_diagrams(self):
        return self.diagrams

