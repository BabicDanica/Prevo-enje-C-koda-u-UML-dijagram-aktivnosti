from generated.SimpleCSharpLexer import SimpleCSharpLexer
from generated.SimpleCSharpParser import SimpleCSharpParser
from generated.SimpleCSharpParserListener import SimpleCSharpParserListener


#class ActivityDiagramGenerator(SimpleCSharpListener):
class ActivityDiagramGenerator(SimpleCSharpParserListener):
    def __init__(self):
        # Trenutna metoda koju analiziramo
        self.current_method = None
        self.diagrams = {}  # Skladišti dijagrame: ime_metode -> lista linija PlantUML koda
        self.stack = []     # Stack koji prati ugnježdene petlje i grananja (npr. while, for, do-while)
        self.if_else_stack = []  # Stack za praćenje if/else-if/else struktura

    def enterMethodDecl(self, ctx: SimpleCSharpParser.MethodDeclContext):
        # Ulazak u deklaraciju metode - otvara novi dijagram
        method_name = None
        if ctx.IDENT() is not None:
            method_name = ctx.IDENT().getText()
        if method_name:
            self.current_method = method_name
            self.diagrams[method_name] = ["@startuml", "start"]

    def exitMethodDecl(self, ctx: SimpleCSharpParser.MethodDeclContext):
        # Izlazak iz metode - zatvaranje dijagrama
        if self.current_method and self.current_method in self.diagrams:
            self.diagrams[self.current_method].append("stop")
            self.diagrams[self.current_method].append("@enduml")
            self.current_method = None

    def enterReturnStatement(self, ctx: SimpleCSharpParser.ReturnStatementContext):
        # Dodaje liniju sa return komandom u activity dijagram
        if self.current_method and self.current_method in self.diagrams:
            text = "return"
            if ctx.expression() is not None:
                try:
                    expr_text = ctx.expression().getText()
                    text = f"return {expr_text}"
                except Exception:
                    text = "return <expr>"
            self.diagrams[self.current_method].append(f":{text};")

    def enterExpressionStatement(self, ctx: SimpleCSharpParser.ExpressionStatementContext):
        # Svaka obična naredba (npr. x++; foo();) se dodaje kao linija
        if self.current_method and self.current_method in self.diagrams:
            expr = None
            if ctx.expression() is not None:
                try:
                    expr = ctx.expression().getText()
                except Exception:
                    expr = "<expr>"
            if expr:
                self.diagrams[self.current_method].append(f":{expr};")

    def enterIfStatement(self, ctx: SimpleCSharpParser.IfStatementContext):
        # Ulazak u if blok, dodajemo "if" grananje u dijagram
        if self.current_method and self.current_method in self.diagrams:
            condition = None
            if ctx.expression() is not None:
                try:
                    condition = ctx.expression().getText()
                except Exception:
                    condition = "<condition>"
            if condition:
                # Dodajemo if uslov i pushujemo u stack za else-if/else praćenje
                self.diagrams[self.current_method].append(f"if ({condition}) then (true)")
                self.if_else_stack.append('if')

    def exitIfStatement(self, ctx: SimpleCSharpParser.IfStatementContext):
        # Završava if/else blok u zavisnosti da li postoji else ili else-if
        if self.current_method and self.current_method in self.diagrams and self.if_else_stack:
            # Proveravamo da li postoji ELSE ili ELSE IF
            else_ctx = ctx.ELSE()
            # ANTLR možda razlikuje ELSE IF tako što je IF unutar ELSE bloka, pa mozemo proveravati deeper

            # Detekcija da li se unutar else-a nalazi još jedan if (else-if)
            has_else_if = False
            if else_ctx is not None:
                # Ako ELSE ima IF kao dete, to je else-if
                else_child = None
                for i in range(ctx.getChildCount()):
                    if ctx.getChild(i).getText() == "else":
                        # sledeće dete je else blok
                        if i+1 < ctx.getChildCount():
                            else_child = ctx.getChild(i+1)
                            break
                if else_child is not None and else_child.getText().startswith("if"):
                    has_else_if = True

            if has_else_if:
                # Umesto da zatvaramo if, pustimo da else-if blok to nastavi
                self.diagrams[self.current_method].append("else (false)")
                # Ne skidamo sa stacka, jer else-if nastavlja if
            else:
                if else_ctx is not None:
                    self.diagrams[self.current_method].append("else (false)")
                    self.diagrams[self.current_method].append(":else block;")
                self.diagrams[self.current_method].append("endif")
                self.if_else_stack.pop()

    def enterWhileStatement(self, ctx: SimpleCSharpParser.WhileStatementContext):
        # Petlja while - dodajemo "while" blok
        if self.current_method and self.current_method in self.diagrams:
            condition = None
            if ctx.expression() is not None:
                try:
                    condition = ctx.expression().getText()
                except Exception:
                    condition = "<condition>"
            if condition:
                self.diagrams[self.current_method].append(f"while ({condition}) is (true)")
                self.stack.append("while")

    def exitWhileStatement(self, ctx: SimpleCSharpParser.WhileStatementContext):
        # Zatvaranje while petlje
        if self.current_method and self.stack and self.stack[-1] == "while":
            self.diagrams[self.current_method].append("endwhile")
            self.stack.pop()

    def enterDoWhileStatement(self, ctx: SimpleCSharpParser.DoWhileStatementContext):
        # Otvara do-while blok sa "repeat"
        if self.current_method and self.current_method in self.diagrams:
            self.diagrams[self.current_method].append("repeat")
            self.stack.append("do-while")

    def exitDoWhileStatement(self, ctx: SimpleCSharpParser.DoWhileStatementContext):
        # Zatvara do-while petlju
        if self.current_method and self.stack and self.stack[-1] == "do-while":
            condition = None
            if ctx.expression() is not None:
                try:
                    condition = ctx.expression().getText()
                except Exception:
                    condition = "<condition>"
            else:
                condition = "<condition>"

            self.diagrams[self.current_method].append(f"repeat while ({condition})")
            self.stack.pop()

    def enterForStatement(self, ctx: SimpleCSharpParser.ForStatementContext):
        # Ulaz u for petlju (prikazuje uslov petlje)
        if self.current_method and self.current_method in self.diagrams:
            try:
                init = ctx.getChild(2).getText() if ctx.getChildCount() > 2 else "<init>"
                cond = ctx.getChild(4).getText() if ctx.getChildCount() > 4 else "<condition>"
                update = ctx.getChild(6).getText() if ctx.getChildCount() > 6 else "<update>"
            except Exception:
                init, cond, update = "<init>", "<condition>", "<update>"

            # Može se ispisati i init/update ako želiš, za sad samo uslov za petlju
            self.diagrams[self.current_method].append(f"repeat while ({cond})")
            self.stack.append("for")

    def exitForStatement(self, ctx: SimpleCSharpParser.ForStatementContext):
        # Izlazak iz for petlje
        if self.current_method and self.stack and self.stack[-1] == "for":
            self.diagrams[self.current_method].append("repeat while (false)")
            self.stack.pop()

    def enterLocalVariableDeclaration(self, ctx: SimpleCSharpParser.LocalVariableDeclarationContext):
        if self.current_method:
            # Proveri da li postoji const modifikator
            # Ovo je primer kako možeš proveriti decu ctx
            is_const = False
            for child in ctx.children:
                if child.getText() == "const":
                    is_const = True
                    break

            var_type = ctx.type().getText() if ctx.type() else "var"
            # VarDecl je lista promenljivih, uzmi prvu ili obradi sve
            for var_decl in ctx.varDecl():
                var_name = var_decl.IDENT().getText()
                expr = ""
                if var_decl.expression():
                    expr = self.expression_to_string(var_decl.expression())
                prefix = "const" if is_const else var_type
                if expr:
                    self.diagrams[self.current_method].append(f":{prefix} {var_name} = {expr};")
                else:
                    self.diagrams[self.current_method].append(f":{prefix} {var_name};")


    def get_all_diagrams(self):
        # Vraća sve generisane PlantUML dijagrame
        return self.diagrams
